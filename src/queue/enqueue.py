import json

from src.queue.rq import RedisQueue

class ExternalProcess(object):

    q = RedisQueue('radicos', host="127.0.0.1", port=6379)

    def process(self, data):
        
        for x in data:
            ExternalProcess.q.put(json.dumps(x))
            yield x
