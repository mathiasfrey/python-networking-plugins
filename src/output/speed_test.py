import datetime

class ExternalProcess(object):
    """Try to measure the pipeline's speed; more or less a perf. tool for Redis

    """

    def __init__(self, *args, **kwargs):
        
        self.cnt = kwargs['scope']
        self._last_time = datetime.datetime.now()

    def process(self, data):
        print("SPEED TEST")

        for x in data:
            self.cnt += 1
            # only show/yield every 1000 rows
            if (self.cnt >= 1000):
                yield (
                    str(datetime.datetime.now() - self._last_time),
                    self.cnt,
                    x,
                )
                self.cnt = 0
                self._last_time = datetime.datetime.now()