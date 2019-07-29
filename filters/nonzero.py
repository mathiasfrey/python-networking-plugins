class ExternalProcess(object):
    def process(self, data):
        
        for x in data:
            if x < 0:
                continue
            yield x