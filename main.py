a = 5


def my_fn():
    def inner_fn():
        print(a)
        b = 1
    inner_fn()


my_fn()
