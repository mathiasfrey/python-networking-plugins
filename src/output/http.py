class ExternalProcess(object):

    def __init__(self, **kwargs):
        self.cnt = 0

    def process(self, data):
        print("HTTP Exporter called that was loaded as data NOT code!")

        for x in data:
            self.cnt += 1
            yield ("Counter: %d" % self.cnt, x)