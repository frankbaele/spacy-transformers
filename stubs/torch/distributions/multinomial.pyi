# Stubs for torch.distributions.multinomial (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.distribution import Distribution
from typing import Any, Optional

class Multinomial(Distribution):
    arg_constraints: Any = ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    total_count: Any = ...
    def __init__(self, total_count: int = ..., probs: Optional[Any] = ..., logits: Optional[Any] = ..., validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    def support(self): ...
    @property
    def logits(self): ...
    @property
    def probs(self): ...
    @property
    def param_shape(self): ...
    def sample(self, sample_shape: Any = ...): ...
    def log_prob(self, value: Any): ...
