# Stubs for torch.optim.adamax (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .optimizer import Optimizer
from typing import Any, Optional

class Adamax(Optimizer):
    def __init__(self, params: Any, lr: float = ..., betas: Any = ..., eps: float = ..., weight_decay: int = ...) -> None: ...
    def step(self, closure: Optional[Any] = ...): ...
