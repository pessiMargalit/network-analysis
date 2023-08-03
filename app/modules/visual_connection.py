import asyncio
import io
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

from data.db_service import get_from_db


async def get_visual_connection(lst_connections: List, network_id):
    G = nx.DiGraph()
    edge_labels = {}
    info = get_information_about_network(network_id)
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
    plt.title(
        f"""network id: {network_id}  client: {info[0]['client']}   premise: {info[0]['premise']}   data-taken: {info[0]['date']}""",
        fontsize=10, fontweight='light', color='black')
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # plt.show()
    plt.clf()
    return buffer


@get_from_db
def get_information_about_network(network_id):
    query = """
        SELECT network.id, client.name AS client, network.premise, network.date
    FROM network
    JOIN client ON client.id = network.client_id
    WHERE network.id = %s;
    """
    return query, network_id
