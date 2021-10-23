import stomp
from ..serialization import EdgeList, Result, as_graph


class TSPListener(stomp.ConnectionListener):
    def __init__(self, conn, queue):
        self.conn = conn
        self.queue = queue

    def on_error(self, frame):
        print(f"Error: {frame.body}")

    def on_message(self, frame):
        edges = EdgeList.parse_raw(frame.body)
        g, nodes_map = as_graph(edges)
