import asyncio

from app.modules.map_connections import get_network_devices_connections as get_network_devices_connections
from app.modules.visual_connection import get_visual_connection as get_visual_connection


def view_network_map(network_id):
    lst_connection = get_network_devices_connections(network_id)
    print(lst_connection)
    network_map = get_visual_connection(lst_connection)
    return network_map

    # TODO: return network_map


res = view_network_map(2)
print(res)