import json
from src.queue.rq import RedisQueue

class ExternalProcess(object):

    q = RedisQueue('radicos', host="127.0.0.1", port=6379)

    def process(self, data):
        
        while True:
            x = json.loads(ExternalProcess.q.get())
            yield x
