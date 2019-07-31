# Stubs for pytorch_transformers.file_utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

torch_cache_home: Any
default_cache_path: Any
PYTORCH_PRETRAINED_BERT_CACHE: Any
logger: Any

def url_to_filename(url: Any, etag: Optional[Any] = ...): ...
def filename_to_url(filename: Any, cache_dir: Optional[Any] = ...): ...
def cached_path(url_or_filename: Any, cache_dir: Optional[Any] = ...): ...
def split_s3_path(url: Any): ...
def s3_request(func: Any): ...
def s3_etag(url: Any): ...
def s3_get(url: Any, temp_file: Any) -> None: ...
def http_get(url: Any, temp_file: Any) -> None: ...
def get_from_cache(url: Any, cache_dir: Optional[Any] = ...): ...
