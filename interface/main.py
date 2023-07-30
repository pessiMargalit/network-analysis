import uvicorn
from fastapi import FastAPI

# from scapy.all import *
# from scapy.layers.inet import UDP, IP
# from scapy.layers.l2 import ARP, Ether
# import fastapi
# curr_path = os.path.dirname(__file__)
# root_path = os.path.join(curr_path, "..")
# sys.path.append(root_path)
# # print(sys.path)
app = FastAPI()
import routes.network_route

#
# packets = rdpcap("../capture_files/evidence01.pcap")
# packets.summary()

# for packet in packets:
#     if packet.haslayer(UDP):
#         print(packet.summary())


# def packet_callback(packet):
#     if IP in packet:
#         ttl_value = packet[IP].ttl
#         print(f"TTL Value: {ttl_value}")


# Sniff packets on the network
# sniff(filter="ip", prn=packet_callback, count=10)
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
