class ExternalProcess(object):

    # 
    cnt = 0

    def process(self, data):
        print("HTTP Exporter called that was loaded as data NOT code!")

        for x in data:
            ExternalProcess.cnt += 1
            yield (x / 10.0, ExternalProcess.cnt)