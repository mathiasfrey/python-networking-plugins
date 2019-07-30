GEARING_SIZE = 3

class ExternalProcess(object):

    _list_of_data = []

    def process(self, data):
        print("Simple gearing mechanism")

        for x in data:

            ExternalProcess._list_of_data.append(data)
                   
            if len(ExternalProcess._list_of_data) >= GEARING_SIZE:
                yield ExternalProcess._list_of_data
                ExternalProcess._list_of_data = []