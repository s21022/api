def lt(a, b):
    return a < b


def gt(a, b):
    return b < a


def max(a, b):
    return a if gt(a, b) else b


def min(a, b):
    return a if lt(a, b) else b


def mymax(array):
    acc = array[0]
    for i in array[1:]:
        if acc < i:
            acc = i
    return acc


def mymin(array):
    acc = array[0]
    for i in array[1:]:
        if acc > i:
            acc = i
    return acc


def mylen(s):
    count = 0


def mysum(array):
    acc = 0
    for i in array:
        acc += i
    return acc


def myslice(s, start, end):
    a = ""
    for i in range(start, end):
        a += s[i]
    return a


def myslice2(s, start, end):
    buf = ""
    for i, c in enumerate(s):
        if i >= end:
            break
        if start <= i < end:
            buf += c
    return buf


p = print
p(myslice("yuu, 1, 3"))
