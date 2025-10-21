

from collections.abc import Iterable
import collections

def flatten(items):
    
    def _flatten_generator(items_to_flatten):
        for item in items_to_flatten:
            if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                yield from _flatten_generator(item)
            else:
                yield item

    return list(_flatten_generator(items))
    

def unique(items):
    
    return list(dict.fromkeys(items))

def chunk(items, size):
    
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    for i in range(0, len(items), size):
        yield items[i:i + size]


 

from functools import reduce
def get_nested(data, key_path, default=None):
    keys = key_path.split('.')
    try:
        return reduce(lambda d, key: d[key], keys, data)
    except (KeyError, TypeError):
        return default       
    


def invert_dict(data):
    
    if len(set(data.values())) == len(data.values()):
        return {value: key for key, value in data.items()}
    else:
        inverted = collections.defaultdict(list)
        for key, value in data.items():
            inverted[value].append(key)
        return dict(inverted)