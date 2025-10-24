import logging as lg


def disable_function(func):
    def wrapper(*args):
        lg.info(f"Function {func.__name__} is disabled.")
    return wrapper

