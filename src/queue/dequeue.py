import json
from src.queue.rq import RedisQueue

class ExternalProcess(object):

    def __init__(self, **kwargs):

        self.q = RedisQueue(
            kwargs['queue_name'],
            host=kwargs['host'],
            port=kwargs['port']
        )

    def process(self, data):
        
        while True:
            x = json.loads(self.q.get())
            yield x
