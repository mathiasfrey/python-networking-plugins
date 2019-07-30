import json
import time
from src.queue.rq import RedisQueue

CLOCK_RATE = 1

class ExternalProcess(object):

    q = RedisQueue('radicos', host="127.0.0.1", port=6379)

    def process(self, data):
        
        while True:
            time.sleep(CLOCK_RATE)

            while not ExternalProcess.q.empty():
                x = json.loads(ExternalProcess.q.get())
                yield x
