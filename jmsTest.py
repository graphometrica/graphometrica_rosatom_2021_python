import time
import sys
import os

import stomp

from solution.service.serialization import EdgeList
from solution.service.solver import solve


class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)
        edgeList = EdgeList.parse_raw(frame.body)
        solveResult =solve(edgeList)
        print('Sending result "%s"' % solveResult.json())
        conn.send(body=solveResult.json(), destination='/queue/rosatom.tsp.output')

os.environ["QBOARD_TOKEN"] = ""
os.environ["QBOARD_SOLVER"] = "remote:simcim"
os.environ["QBOARD_SERVER"] = "https://remote.qboard.tech"

conn = stomp.Connection([('52.149.226.198', 61613)])
conn.set_listener('', MyListener())
conn.connect('admin', 'password', wait=True)
conn.subscribe(destination='/queue/rosatom.tsp.input', id=1, ack='auto')
while True:
    time.sleep(1)
conn.disconnect()

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)
