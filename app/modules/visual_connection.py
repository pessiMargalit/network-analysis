import io
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
import mplleaflet
from fastapi.openapi.models import Response


def get_visual_connection(lst_connections: List):
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
    #conn_dvcs_lst = get_connected_devices(network_id)
    conn_dvcs_lst = [(conn["source_MAC"], conn["destination_MAC"]) for conn in lst_connections]
    g = nx.MultiDiGraph()
    g.add_edges_from(conn_dvcs_lst)
    nx.draw_circular(g, with_labels=True)
    # fig = plt.figure()
    buffer = io.BytesIO()
    plt.show()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Clear the plot
    plt.clf()
    # Return the image file as a response
    return {f"content":"buffer.getvalue()", "media_type": "image/png"}


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
