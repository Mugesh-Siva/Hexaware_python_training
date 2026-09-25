import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Function: {func.__name__}")
        print(f"Execution Time: {execution_time:.2f} seconds")
        # :.2f break down
        # : is the seperator from the variable and .2f is as we know formatting the float from .2 points
        
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

result = calculate_sum(1000000)
print("Result:", result)