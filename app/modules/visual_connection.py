import asyncio
import io
from typing import List
import networkx as nx
import matplotlib.pyplot as plt


async def get_visual_connection(lst_connections: List):
    G = nx.Graph()
    # for connection in lst_connections:
    #     G.add_edge(connection["source_ip"], connection['destination_ip'])
    # for connection in lst_connections:
    #     source_ip = connection["source_ip"]
    #     destination_ip = connection["destination_ip"]
    #     source_mac = connection["source_MAC"]
    #     destination_mac = connection["destination_MAC"]
    #     G.add_edge(source_mac,destination_mac)
    #     G.nodes[source_mac]['label'] = source_ip
    #     G.nodes[destination_mac]['label'] = destination_ip
    #     edge_labels[(source_mac, destination_mac)] = f"{connection['protocol']}"
    # nx.draw_spring(G, with_labels=True)
    # return plt.show()
    # conn_dvcs_lst = get_connected_devices(network_id)
    conn_devices_lst = [(conn["source_MAC"], conn["destination_MAC"]) for conn in lst_connections]
    g = nx.MultiDiGraph()
    g.add_edges_from(conn_devices_lst)
    nx.draw_circular(g, with_labels=True)
    # fig = plt.figure()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Clear the plot
    plt.clf()
    await asyncio.sleep(0.1)
    # Return the image file as a response
    value = buffer.getvalue()
    return {"content": value, "media_type": "image/png"}
