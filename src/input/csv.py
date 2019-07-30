class ExternalProcess(object):
    def process(self, data):
        print("CSV importer called that was loaded as data NOT code!")
        
        for x in data:
            yield x