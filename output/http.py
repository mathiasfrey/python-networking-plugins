class ExternalProcess(object):
    def process(self, data):
        print("HTTP Exporter called that was loaded as data NOT code!")
        return data + 0.4