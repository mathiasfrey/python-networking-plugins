import random
import time

class VoidInput(object):
    def process(self, data):
        while True:
            yield None

class RangeInputFaker(object):

    def __init__(self, to):
        self.to = to

    def process(self, data):
        for x in range(self.to):
            yield x

class RandomInputFaker(object):

    def __init__(self, lines_per_second=10):
        self.lines_per_second=lines_per_second
    
    LINES_PER_SECOND = 10

    def process(self, data):
        print("Hello Random!")

        while True:
            # time.sleep(1 / RandomInputFaker.LINES_PER_SECOND)
            yield random.random()


class FibonacciInputFaker(object):

    fib = 1
    previous = 1

    def process(self, data):
        print("Aloha Fibonacci")

        yield FibonacciInputFaker.fib
        while FibonacciInputFaker.fib < 10000:
            yield FibonacciInputFaker.fib
            f = FibonacciInputFaker.fib + FibonacciInputFaker.previous
            FibonacciInputFaker.previous = FibonacciInputFaker.fib
            FibonacciInputFaker.fib = f

            time.sleep(1)