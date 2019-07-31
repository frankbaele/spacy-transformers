# Stubs for torch.multiprocessing.queue (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import multiprocessing.queues
from typing import Any

class ConnectionWrapper:
    conn: Any = ...
    def __init__(self, conn: Any) -> None: ...
    def send(self, obj: Any) -> None: ...
    def recv(self): ...
    def __getattr__(self, name: Any): ...

class Queue(multiprocessing.queues.Queue):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class SimpleQueue(multiprocessing.queues.SimpleQueue): ...
