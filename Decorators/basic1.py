def outer():
    a=5
    def inner():
        print(a)
    return inner
a=outer()
a()    