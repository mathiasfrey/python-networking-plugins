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
    previous = 1

    def process(self, data):
        print("Aloha Fibonacci")

        yield FibonacciInputFaker.fib
        while FibonacciInputFaker.fib < 20:
            yield FibonacciInputFaker.fib
            f = FibonacciInputFaker.fib + FibonacciInputFaker.previous
            FibonacciInputFaker.previous = FibonacciInputFaker.fib
            FibonacciInputFaker.fib = f
