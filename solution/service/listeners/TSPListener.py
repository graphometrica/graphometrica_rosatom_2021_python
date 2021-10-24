import os
import stomp
import time

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

    def on_disconnected(self):
        print("Disconnected... Try to reconnect.")
        user = os.environ["MQ_USER"]
        password = os.environ["MQ_PASSWORD"]
        queue_in = os.environ["MQ_QUEUE_INPUT"]

        attempts = 10
        n = 0
        while n < 10:
            try:
                self.conn.connect(user, password, wait=True, ack="auto")
            except Exception as e:
                n += 1
                print(f"Attempt {n}: exception...")
                time.sleep(5)
                continue
            else:
                print("Reconnection was succesful!")
                self.conn.subscribe(queue_in, id=1)
                break
