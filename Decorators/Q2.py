def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)