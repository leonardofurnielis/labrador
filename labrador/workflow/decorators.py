from typing import Callable


def start(*args) -> Callable:
        
    def decorator(func: Callable) -> Callable:
        func.__is_start_method__ = True
        
        return func
        
    if len(args):
        # The decorator was used without parentheses, i.e. `@start`
        func = args[0]
        decorator(func)
        return func
    
    return decorator

def step(condition: str) -> Callable:
        
    def decorator(func: Callable) -> Callable:
        if isinstance(condition, str):
            func.__trigger_methods__ = [condition]
        else:
            raise ValueError("condition must be string")
        
        return func
        
    return decorator
