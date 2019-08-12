import json

from src.queue.rq import RedisQueue

class ExternalProcess(object):

    def __init__(self, *args, **kwargs):

        self.q = RedisQueue(
            kwargs['queue_name'],
            host=kwargs['host'],
            port=kwargs['port']
        )

    def process(self, data):
        
        for x in data:
            self.q.put(json.dumps(x))
            yield x
