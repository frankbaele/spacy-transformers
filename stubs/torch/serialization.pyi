# Stubs for torch.serialization (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._utils import _import_dotted_name
from typing import Any, Optional

DEFAULT_PROTOCOL: int
LONG_SIZE: Any
INT_SIZE: Any
SHORT_SIZE: Any
MAGIC_NUMBER: int
PROTOCOL_VERSION: int
STORAGE_KEY_SEPARATOR: str

class SourceChangeWarning(Warning): ...

def mkdtemp() -> None: ...
def register_package(priority: Any, tagger: Any, deserializer: Any) -> None: ...
def validate_cuda_device(location: Any): ...
def location_tag(storage: Any): ...
def default_restore_location(storage: Any, location: Any): ...
def normalize_storage_type(storage_type: Any): ...
def storage_to_tensor_type(storage: Any): ...
def save(obj: Any, f: Any, pickle_module: Any = ..., pickle_protocol: Any = ...): ...
def load(f: Any, map_location: Optional[Any] = ..., pickle_module: Any = ..., **pickle_load_args: Any): ...
