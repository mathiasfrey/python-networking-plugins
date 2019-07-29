class SimpleProcess:
    def process(self, data):
        print("Hello Simple!")
        for x in data:
            yield x * 2

class AlternativeProcess:
    def process(self, data):
        print("Aloha Alternative")

        for x in data:
            yield x + .55