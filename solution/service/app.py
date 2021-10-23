import stomp
import os
from time import sleep

from .listeners import TSPListener


class Application:
    def __init__(self):
        self.user = os.environ["MQ_USER"]
        self.password = os.environ["MQ_PASSWORD"]
        self.host = os.environ["MQ_HOST"]
        self.port = os.environ["MQ_PORT"]
        self.queue_in = os.environ["MQ_QUEUE_INPUT"]
        self.queue_out = os.environ["MQ_QUEUE_OUTPUT"]

    def _connect(self):
        self.conn = stomp.Connection([(self.host, self.port)])
        self.conn.set_listener("tsp", TSPListener(self.conn, self.queue_out))
        self.conn.connect(self.user, self.password, wait=True, ack="auto")
        self.conn.subscribe(self.queue_in, id=1)

    def start(self):
        self._connect()

        while True:
            if not self.conn.is_connected():
                self._connect()
            else:
                sleep(2)
