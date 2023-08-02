import asyncio
import io
from typing import List
import networkx as nx
import matplotlib.pyplot as plt


async def get_visual_connection(lst_connections: List):
    G = nx.DiGraph()
    edge_labels = {}

    for connection in lst_connections:
        source_mac = connection["source_MAC"]
        destination_mac = connection["destination_MAC"]

        G.add_edge(source_mac, destination_mac)
        G.nodes[source_mac]['label'] = connection["source_ip"]
        G.nodes[destination_mac]['label'] = connection["destination_ip"]
        edge_labels[(source_mac, destination_mac)] = connection['protocol']

    # Draw nodes with labels
    node_labels = nx.get_node_attributes(G, 'label')
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, labels=node_labels, with_labels=True, node_size=3000, font_size=9, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, width=2.0, alpha=0.7)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5, font_size=8)

    plt.axis('off')
    # Save the plot to a BytesIO buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # plt.show()
    plt.clf()
    return buffer
