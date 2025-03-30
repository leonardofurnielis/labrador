from typing import Callable, Dict, List


class Workflow():
    
    _start_methods: List[str] = []
    _steps: Dict[str, tuple[str, List[str]]] = {}
    
    def __init__(self) -> None:
        
        self._methods: Dict[str, Callable] = {}
        
        for method_name in dir(self):
            if not method_name.startswith("_"):
                method = getattr(self, method_name)
                
                # Check for any flow-related attributes
                if (
                    hasattr(method, "__is_start_method__")
                    or hasattr(method, "__trigger_methods__")
                ):
                    # Ensure method is bound to this instance
                    if not hasattr(method, "__self__"):
                        method = method.__get__(self, self.__class__)
                    self._methods[method_name] = method
                    
    def run():
        pass
        