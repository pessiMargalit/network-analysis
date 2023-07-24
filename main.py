# from scapy.all import *
# from scapy.layers.inet import UDP, IP
# from scapy.layers.l2 import ARP, Ether
#
# packets = rdpcap("evidence01.pcap")
# packets.summary()
#
# for packet in packets:
#     if packet.haslayer(UDP):
#         print(packet.summary())
#
#
# def packet_callback(packet):
#     if IP in packet:
#         ttl_value = packet[IP].ttl
#         print(f"TTL Value: {ttl_value}")
#
#
# # Sniff packets on the network
# sniff(filter="ip", prn=packet_callback, count=10)
