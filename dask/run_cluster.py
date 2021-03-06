from time import sleep
from dask import delayed


def inc(x):
    sleep(1)
    return x + 1


def add(x, y):
    sleep(1)
    return x + y

x = delayed(inc)(1)
y = delayed(inc)(2)
z = delayed(add)(x,y)

z.compute()
z.visualize()