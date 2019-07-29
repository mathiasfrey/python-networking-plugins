
def nothing(sequence):
    yield from sequence

def double(sequence):
    for x in sequence:
        yield x * 2

def quadruple(sequence):
    for i in sequence:
        yield 4 * i

def negate(sequence):
    for i in sequence:
        yield -i


def triple(func):
    def wrapper():
        func_ret = func()
        output = func_ret * 3
        return output
    return wrapper


if __name__ == '__main__':
    """Just showcase the magic of iterators"""

    #for x in range(5):
    #    for f in functions:
    #        x = f(x)

    print(list(quadruple(double(range(4)))))

    # functions = (triple,)
    # for x in range(3):
    #     print(triple(range(3))())