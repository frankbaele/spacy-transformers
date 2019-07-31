# Stubs for thinc.extra.hpbff (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def minibatch(train_X: Any, train_y: Any, size: int = ..., nr_update: int = ...) -> None: ...

class BestFirstFinder:
    queue: Any = ...
    limit: int = ...
    params: Any = ...
    best_acc: float = ...
    best_i: int = ...
    i: int = ...
    j: int = ...
    best_model: Any = ...
    temperature: float = ...
    def __init__(self, **param_values: Any) -> None: ...
    @property
    def configs(self) -> None: ...
    def enqueue(self, model: Any, train_acc: Any, check_acc: Any) -> None: ...
    def __iter__(self) -> None: ...
    @property
    def best(self): ...

def resample_hyper_params(hparams: Any, temperature: Any): ...
def resample(curr: Any, min_: Any, max_: Any, temperature: Any): ...
def train_epoch(model: Any, sgd: Any, hparams: Any, train_X: Any, train_y: Any, dev_X: Any, dev_y: Any, device_id: int = ..., temperature: float = ...): ...

class DevicePool:
    devices: Any = ...
    def __init__(self, n: Any) -> None: ...
    def acquire(self): ...
    def release(self, i: Any) -> None: ...
