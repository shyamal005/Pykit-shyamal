
import time
from functools import wraps

def memoize(func):
   
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        
        key = (args, frozenset(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        
        return cache[key]
        
    return wrapper



def retry(tries=3, delay=1, backoff=2):
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"'{func.__name__}' failed with {e}. Retrying in {_delay} seconds...")
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
           
            return func(*args, **kwargs)
        return wrapper
    return decorator



def timer(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished '{func.__name__}' in {run_time:.4f} secs")
        return result

    return wrapper
