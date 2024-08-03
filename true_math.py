from math import inf
def divide(first, second):
    try:
        first / second
    except ZeroDivisionError:
        return inf
    else:
        return first / second



