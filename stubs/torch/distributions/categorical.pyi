# Stubs for torch.distributions.categorical (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.distribution import Distribution
from typing import Any, Optional

class Categorical(Distribution):
    arg_constraints: Any = ...
    has_enumerate_support: bool = ...
    probs: Any = ...
    logits: Any = ...
    def __init__(self, probs: Optional[Any] = ..., logits: Optional[Any] = ..., validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    def support(self): ...
    def logits(self): ...
    def probs(self): ...
    @property
    def param_shape(self): ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    def sample(self, sample_shape: Any = ...): ...
    def log_prob(self, value: Any): ...
    def entropy(self): ...
    def enumerate_support(self, expand: bool = ...): ...
