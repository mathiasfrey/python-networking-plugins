class ExternalProcess(object):

    _cnt = 0

    def process(self, data):
        print("HTTP Exporter called that was loaded as data NOT code!")

        for x in data:
            ExternalProcess._cnt += 1
            yield (x / 10.0, ExternalProcess._cnt)