import random
import time

class VoidInput(object):
    def process(self, data):
        while True:
            yield None

class RangeInputFaker(object):

    def __init__(self, **kwargs):
        self.to = kwargs['to']

    def process(self, data):
        for x in range(self.to):
            yield x

class RandomInputFaker(object):

    def __init__(self, **kwargs):
        
        try:
            self.lines_per_second_limit = int(kwargs['lines_per_second_limit'])
            print("Initialize random with lines per second limit: %d per sec" % self.lines_per_second)
        except:
            self.lines_per_second_limit = None
            print("Go unlimited!")

    def process(self, data):
        print("Hello Random!")

        while True:
            if self.lines_per_second_limit:
                time.sleep(1 / int(self.lines_per_second_limit))

            yield random.random()


class FibonacciInputFaker(object):

    def __init__(self, **kwargs):
        self.fib = 1
        self.previous = 1

        try:
            self.limit = int(kwargs['limit'])
        except:
            self.limit = None

    def process(self, data):
        print("Aloha Fibonacci")

        yield self.fib
        while self.limit == None or self.fib < self.limit:
            yield self.fib
            f = self.fib + self.previous
            self.previous = self.fib
            self.fib = f

            time.sleep(1)