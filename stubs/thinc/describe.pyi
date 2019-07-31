# Stubs for thinc.describe (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class AttributeDescription:
    name: Any = ...
    text: Any = ...
    value: Any = ...
    def __init__(self, text: Any, value: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, attr: Any, model: Any) -> None: ...
    def __get__(self, obj: Any, type: Optional[Any] = ...): ...
    def __set__(self, obj: Any, val: Any) -> None: ...

class Dimension(AttributeDescription):
    def __get__(self, obj: Any, type: Optional[Any] = ...): ...
    def __set__(self, obj: Any, value: Any) -> None: ...

class Weights(AttributeDescription):
    name: Any = ...
    text: Any = ...
    get_shape: Any = ...
    init: Any = ...
    def __init__(self, text: Any, get_shape: Any, init: Optional[Any] = ...) -> None: ...
    def __get__(self, obj: Any, type: Optional[Any] = ...): ...
    def __set__(self, obj: Any, val: Any) -> None: ...

class Gradient(AttributeDescription):
    name: Any = ...
    text: Any = ...
    param_name: Any = ...
    def __init__(self, param_name: Any) -> None: ...
    def __get__(self, obj: Any, type: Optional[Any] = ...): ...
    def __set__(self, obj: Any, val: Any) -> None: ...

class Synapses(Weights): ...
class Biases(Weights): ...
class Moment(Weights): ...

def attributes(**specs: Any): ...
def on_init(*callbacks: Any): ...
def on_data(*callbacks: Any): ...
def input(getter: Any): ...
def output(getter: Any): ...
