GEARING_SIZE = 3

class ExternalProcess(object):

    _list_of_data = []

    def process(self, data):
        print("Simple gearing mechanism")

        for x in data:

            ExternalProcess._list_of_data.append(x)
                   
            if len(ExternalProcess._list_of_data) >= GEARING_SIZE:
                print('>>>', ExternalProcess._list_of_data)
                yield ExternalProcess._list_of_data
                ExternalProcess._list_of_data = []