# 记忆体化


def memo(func):
    """
    函数记忆体
    """
    cache = {}
    # @wraps(func)

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def f1(n):
    if n < 2:
        return 1
    return f1(n-1) + f1(n-2)


print(f1(100))
print(f1(5))

######################################################################


class Memo():
    """
    类记忆体
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}
        # return self.memo

    def __call__(self, *args):
        # self.cache = {}
        # @wraps(func)
        # def wrap(*args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
        # return wrap


@Memo
def f2(n):
    if n < 2:
        return 1
    return f2(n-1) + f2(n-2)


print(f2(100))
print(f2(5))
