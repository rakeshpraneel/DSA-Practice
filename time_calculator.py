import time

def timer_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken for function to execute::: {end-start}")
        return output
    return wrapper