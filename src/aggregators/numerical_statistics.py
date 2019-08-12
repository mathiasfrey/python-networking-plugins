from statistics import mean
from collections import deque

SCOPE = 1000

class ExternalProcess(object):

    _deque_of_data = deque(maxlen=SCOPE)

    def process(self, data):
        print("Stats on values")

        for x in data:

            ExternalProcess._deque_of_data.append(x)

            # value, min, max, avg, mean 
            yield (
                x,
                min(ExternalProcess._deque_of_data),
                max(ExternalProcess._deque_of_data),
                sum(ExternalProcess._deque_of_data) / SCOPE,
                mean(ExternalProcess._deque_of_data),
            )