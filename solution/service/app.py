import stomp

from .listeners import TSPListener


class Application:
    def __init__(self, user: str, passwd: str, host: str, port: int, queue: str):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.queue

    def _connect(self):
        self.conn = stomp.Connection([(self.host, sefl.port)])
        self.conn.set_listener("tsp", TSPListener(self.conn))
        self.conn.connect(self.user, self.passwd, wait=True)
        self.conn.subscribe(self.queue, id=1)

    def start(self):
        self._connect()

    def stop(self):
        self.conn.disconnect()
