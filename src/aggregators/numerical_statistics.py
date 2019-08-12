from statistics import mean
from collections import deque

class ExternalProcess(object):

    def __init__(self, **kwargs):
        self.scope = kwargs['scope']
        print("Initializing double-ended queue with size %d" % self.scope)
        self._deque_of_data = deque(maxlen=self.scope)

    def process(self, data):
        print("Stats on values")

        for x in data:

            self._deque_of_data.append(x)

            # value, min, max, avg, mean 
            yield (
                x,
                min(self._deque_of_data),
                max(self._deque_of_data),
                sum(self._deque_of_data) / self.scope,
                mean(self._deque_of_data),
            )