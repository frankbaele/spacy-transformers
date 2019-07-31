# Stubs for torch.autograd.profiler (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import defaultdict, namedtuple
from typing import Any, Optional

class EventList(list):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def populate_cpu_children(self): ...
    @property
    def self_cpu_time_total(self): ...
    @property
    def cpu_children_populated(self): ...
    def table(self, sort_by: Optional[Any] = ..., row_limit: int = ...): ...
    def export_chrome_trace(self, path: Any) -> None: ...
    def key_averages(self): ...
    def total_average(self): ...

class profile:
    enabled: Any = ...
    use_cuda: Any = ...
    function_events: Any = ...
    entered: bool = ...
    def __init__(self, enabled: bool = ..., use_cuda: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...
    def table(self, sort_by: Optional[Any] = ..., row_limit: int = ...): ...
    def export_chrome_trace(self, path: Any): ...
    def key_averages(self): ...
    def total_average(self): ...
    @property
    def self_cpu_time_total(self): ...

class emit_nvtx:
    enabled: Any = ...
    entered: bool = ...
    def __init__(self, enabled: bool = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...

def load_nvprof(path: Any): ...
def format_time(time_us: Any): ...
def format_time_share(time_us: Any, total_time_us: Any): ...
def attr_formatter(name: Any): ...

class FormattedTimesMixin:
    cpu_time_str: Any = ...
    cuda_time_str: Any = ...
    cpu_time_total_str: Any = ...
    cuda_time_total_str: Any = ...
    self_cpu_time_total_str: Any = ...
    @property
    def cpu_time(self): ...
    @property
    def cuda_time(self): ...

class Interval:
    start: Any = ...
    end: Any = ...
    def __init__(self, start: Any, end: Any) -> None: ...
    def elapsed_us(self): ...

Kernel = namedtuple('Kernel', ['name', 'device', 'interval'])

class FunctionEvent(FormattedTimesMixin):
    id: Any = ...
    name: Any = ...
    cpu_interval: Any = ...
    thread: Any = ...
    kernels: Any = ...
    count: int = ...
    cpu_children: Any = ...
    def __init__(self, id: Any, name: Any, thread: Any, cpu_start: Any, cpu_end: Any) -> None: ...
    def append_kernel(self, name: Any, device: Any, start: Any, end: Any) -> None: ...
    def append_cpu_child(self, child: Any) -> None: ...
    @property
    def self_cpu_time_total(self): ...
    @property
    def cuda_time_total(self): ...
    @property
    def cpu_time_total(self): ...
    @property
    def key(self): ...

class FunctionEventAvg(FormattedTimesMixin):
    key: Any = ...
    count: int = ...
    cpu_time_total: int = ...
    cuda_time_total: int = ...
    self_cpu_time_total: int = ...
    def __init__(self) -> None: ...
    def __iadd__(self, other: Any): ...

class StringTable(defaultdict):
    def __missing__(self, key: Any): ...

def parse_cpu_trace(thread_records: Any): ...

class EnforceUnique:
    seen: Any = ...
    def __init__(self) -> None: ...
    def see(self, *key: Any) -> None: ...

def parse_nvprof_trace(path: Any): ...
def build_table(events: Any, sort_by: Optional[Any] = ..., header: Optional[Any] = ..., row_limit: int = ...): ...
