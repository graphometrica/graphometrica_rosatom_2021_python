import stomp
from ..solver import solve
from ..serialization import EdgeList, Result


class TSPListener(stomp.ConnectionListener):
    def __init__(self, conn, queue):
        self.conn = conn
        self.queue = queue

    def on_error(self, frame):
        print(f"Error: {frame.body}")

    def on_message(self, frame):
        edges = EdgeList.parse_raw(frame.body)
        result = solve(edges)

