from app.modules.map_connections import get_network_devices_connections as get_network_devices_connections
from app.modules.visual_connection import get_visual_connection as get_visual_connection


async def view_network_map(network_id):
    lst_connection = get_network_devices_connections(network_id)
    network_map = await get_visual_connection(lst_connection)
    return network_map
