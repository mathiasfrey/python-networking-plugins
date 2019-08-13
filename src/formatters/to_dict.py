class ExternalProcess(object):

    def __init__(self, **kwargs):
        pass

    def process(self, data):

        for x in data:
            yield {
                "value": x[0],
                "min": x[1],
                "max": x[2],
                "avg": x[3],
                "mean": x[4],
                }