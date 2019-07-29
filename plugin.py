import random

class VoidInput(object):
    def process(self, data):
        while True:
            yield None

class RandomInputFaker(object):
    def process(self, data):
        print("Hello Random!")

        while True:
            yield random.random()


class FibonacciInputFaker(object):

    fib = 1

    def process(self, data):
        print("Aloha Fibonacci")

        yield FibonacciInputFaker.fib
        while FibonacciInputFaker.fib < 10000:
            f = FibonacciInputFaker.fib
            FibonacciInputFaker.fib = f + f
            yield f