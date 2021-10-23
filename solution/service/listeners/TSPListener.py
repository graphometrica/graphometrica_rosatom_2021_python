import stomp

from ..serialization import Input, Result
from ..solver import solve


class TSPListener(stomp.ConnectionListener):
    def __init__(self, conn, queue):
        self.conn = conn
        self.queue = queue

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)
        input = Input.parse_raw(frame.body)

        result = solve(input.edge_list, input.solver_type, input.router_id)
        print('Sending result "%s"' % result.json())

        self.conn.send(body=result.json(), destination=self.queue)
