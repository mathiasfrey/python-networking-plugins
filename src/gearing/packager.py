
class ExternalProcess(object):

    

    def __init__(self, *args, **kwargs):
        
        self._list_of_data = []
        self.gearing_size = kwargs['gearing_size']

    def process(self, data):
        print("Simple gearing mechanism")

        for x in data:

            self._list_of_data.append(x)
                   
            if len(self._list_of_data) >= self.gearing_size:
                yield self._list_of_data
                self._list_of_data = []