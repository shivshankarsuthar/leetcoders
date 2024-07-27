def repeat(times):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(times):
                print(func(*args,**kwargs))
        return wrapper
    return decorator

def uppercase(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper

@repeat(3)
@uppercase
def greet(name):
    return "Hello, "+name

greet("Shiv")