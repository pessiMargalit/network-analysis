from typing import List
import networkx as nx
import matplotlib.pyplot as plt


def get_visual_connection(lst_connections: List):
    G = nx.Graph()
    # for connection in lst_connections:
    #     G.add_edge(connection["source_ip"], connection['destination_ip'])
    for connection in lst_connections:
        source_ip = connection["source_ip"]
        destination_ip = connection["destination_ip"]
        source_mac = connection["source_mac"]
        destination_mac = connection["destination_mac"]
        G.add_edge(source_mac,destination_mac)
        G.nodes[source_mac]['label'] = source_ip
        G.nodes[destination_mac]['label'] = destination_ip
        G.edge_labels[(source_mac, destination_mac)] = f"{source_ip} to {destination_ip}"
    nx.draw_spring(G, with_labels=True)
    return plt.show()


"""
this code from network x that create graph and show it.....s
"""

# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.Graph()
#
# G.add_edge("y", "d")
# G.add_edge("t", "y")
# G.add_edge("p", "t" )
# G.add_node("hi")
# nx.draw_spring(G)
# plt.show()
