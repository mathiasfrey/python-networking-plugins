import datetime

class ExternalProcess(object):
    """Try to measure the pipeline's speed; more or less a perf. tool for Redis

    """
    _cnt = 0
    _last_time = datetime.datetime.now()

    def process(self, data):
        print("SPEED TEST")

        for x in data:
            ExternalProcess._cnt += 1
            # only show/yield every 1000 rows
            if (ExternalProcess._cnt >= 1000):
                yield (
                    str(datetime.datetime.now() - ExternalProcess._last_time),
                    ExternalProcess._cnt,
                    x,
                )
                ExternalProcess._cnt = 0
                ExternalProcess._last_time = datetime.datetime.now()