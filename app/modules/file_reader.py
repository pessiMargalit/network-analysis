from mac_vendor_lookup import AsyncMacLookup
from scapy.all import rdpcap
from scapy.libs.six import BytesIO


async def read_file(capture_file_content):
    try:
        # TODO: Match cases for each type of capture files
        return await extract_devices_and_connections(capture_file_content)

    except FileNotFoundError:
        print(f"File not found: {capture_file_content}")
    except Exception as e:
        print(f"Error occurred: {e}")


async def get_device_vendor_by_mac_address(mac_address, ip_address):
    try:
        device_vendor = await AsyncMacLookup().lookup(mac_address)
    except KeyError as e:
        device_vendor = "UNKNOWN"
    return {'ip_address': ip_address, 'vendor': device_vendor, 'destinations': {}}


async def extract_devices_and_connections(pcap_file_content):
    devices = {}
    connections = {}
    pcap_file = BytesIO(pcap_file_content)
    packets = rdpcap(pcap_file)
    for packet in packets:
        if 'Ether' in packet:
            src_mac = packet['Ether'].src
            dst_mac = packet['Ether'].dst
        if 'IP' in packet:
            src_ip = packet['IP'].src
            dst_ip = packet['IP'].dst

        if 'TCP' in packet:
            protocol = packet['TCP'].name
        elif 'UDP' in packet:
            protocol = packet['UDP'].name
        elif 'ARP' in packet:
            protocol = packet['ARP'].name
        elif 'ICMP' in packet:
            protocol = packet['ICMP'].name
        else:
            protocol = 'Unknown'

        if src_mac not in devices:
            devices[src_mac] = await get_device_vendor_by_mac_address(src_mac, src_ip)

        if dst_mac not in devices:
            devices[src_mac] = await get_device_vendor_by_mac_address(dst_mac, dst_ip)

        if dst_mac not in devices[src_mac]['destinations']:
            devices[src_mac]['destinations'][dst_mac] = set()

        devices[src_mac]['destinations'][dst_mac].add(protocol)

    for src_mac, connections_info in devices.items():
        for dst_mac, protocols in connections_info['destinations'].items():
            connections[(src_mac, dst_mac)] = list(protocols)
    print(devices)
    print(connections)
    return devices, connections
