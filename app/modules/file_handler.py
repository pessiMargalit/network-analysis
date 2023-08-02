from mac_vendor_lookup import AsyncMacLookup
from scapy.all import rdpcap
from scapy.libs.six import BytesIO


async def is_pcap(file_content):
    # Check if the file content matches the PCAP magic number
    pcap_magic_number = b"\xd4\xc3\xb2\xa1"  # little-endian
    return file_content.startswith(pcap_magic_number)


async def is_pcapng(file_content):
    # Check if the file content matches the PCAPNG magic number
    pcapng_magic_number = b"\x0a\x0d\x0d\x0a\x00\x00\x00\x01"
    return file_content.startswith(pcapng_magic_number)


async def read_file(capture_file_content):
    if await is_pcap(capture_file_content) or await is_pcapng(capture_file_content):
        pcap_file = BytesIO(capture_file_content)
        packets = rdpcap(pcap_file)
        return await extract_devices_and_connections(packets)
    raise FileNotFoundError("Only capture files must be uploaded")


async def get_device_vendor_by_mac_address(mac_address, ip_address):
    try:
        device_vendor = await AsyncMacLookup().lookup(mac_address)
    except KeyError as e:
        device_vendor = "UNKNOWN"
    return {'ip_address': ip_address, 'vendor': device_vendor, 'destinations': {}}


def get_protocol(packet):
    if 'TCP' in packet:
        return packet['TCP'].name
    if 'UDP' in packet:
        return packet['UDP'].name
    if 'ARP' in packet:
        return packet['ARP'].name
    if 'ICMP' in packet:
        return packet['ICMP'].name
    return 'Unknown'


def get_devices_connections(devices):
    connections = {}
    for src_mac, connections_info in devices.items():
        for dst_mac, protocols in connections_info['destinations'].items():
            connections[(src_mac, dst_mac)] = list(protocols)
    return connections


def find_router(devices, mac_address, ip_address):
    if devices[mac_address]['ip_address'] != ip_address:
        devices[mac_address]['ip_address'] = 'None'


async def extract_devices_and_connections(packets):
    devices = {}
    connections = {}
    for packet in packets:
        if 'Ether' in packet:
            src_mac = packet['Ether'].src
            dst_mac = packet['Ether'].dst
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst

        protocol = get_protocol(packet)

        if src_mac not in devices:
            devices[src_mac] = await get_device_vendor_by_mac_address(src_mac, src_ip)
        # elif protocol != 'ARP':
        #     find_router(devices, src_mac, src_ip)

        if dst_mac not in devices:
            devices[src_mac] = await get_device_vendor_by_mac_address(dst_mac, dst_ip)
        # elif protocol != 'ARP':
        #     find_router(devices, dst_mac, dst_ip)

        if dst_mac not in devices[src_mac]['destinations']:
            devices[src_mac]['destinations'][dst_mac] = set()

        devices[src_mac]['destinations'][dst_mac].add(protocol)
    connections = get_devices_connections(devices)
    return devices, connections
