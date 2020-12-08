def function_one(d):
    sum = 0
    for k, v in d.items():
        sum += v
    return sum / len(d)


def function_two(d):
    sum = 0
    for k, v in d.items():
        sum += v
    return sum


def function_three(d):
    n = None
    for k, v in d.items():
        if n == None or n < v:
            n = v
    return n


def function_four(d):
    n = None
    for k, v in d.items():
        if n == None or n > v:
            n = v
    return n

