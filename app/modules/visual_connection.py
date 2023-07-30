from typing import List


async def get_visual_connection(lst_connections: List):
    pass

"""
its code from network x that create graph and show it.....s
"""
import networkx as nx
import matplotlib.pyplot as plt
import mynetworkx

G = nx.Graph()

G.add_edge("y", "d")
G.add_edge("t", "y")
G.add_edge("p", "t")
G.add_node("hi")
nx.draw_spring(G)
plt.show()
