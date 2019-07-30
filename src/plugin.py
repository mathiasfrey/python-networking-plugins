import random
import time

class VoidInput(object):
    def process(self, data):
        while True:
            yield None

class RandomInputFaker(object):

    LINES_PER_SECOND = 10

    def process(self, data):
        print("Hello Random!")

        while True:
            time.sleep(1 / RandomInputFaker.LINES_PER_SECOND)
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