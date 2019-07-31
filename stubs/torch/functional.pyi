# Stubs for torch.functional (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def broadcast_tensors(*tensors: Any): ...
def split(tensor: Any, split_size_or_sections: Any, dim: int = ...): ...
def lu_unpack(LU_data: Any, LU_pivots: Any, unpack_data: bool = ..., unpack_pivots: bool = ...): ...
def einsum(equation: Any, *operands: Any): ...
def isfinite(tensor: Any): ...
def isinf(tensor: Any): ...
def meshgrid(*tensors: Any, **kwargs: Any): ...
def stft(input: Any, n_fft: Any, hop_length: Optional[Any] = ..., win_length: Optional[Any] = ..., window: Optional[Any] = ..., center: bool = ..., pad_mode: str = ..., normalized: bool = ..., onesided: bool = ...): ...
def unique(input: Any, sorted: bool = ..., return_inverse: bool = ..., return_counts: bool = ..., dim: Optional[Any] = ...): ...
def unique_consecutive(input: Any, return_inverse: bool = ..., return_counts: bool = ..., dim: Optional[Any] = ...): ...
def tensordot(a: Any, b: Any, dims: int = ...): ...
def cartesian_prod(*tensors: Any): ...
def norm(input: Any, p: str = ..., dim: Optional[Any] = ..., keepdim: bool = ..., out: Optional[Any] = ..., dtype: Optional[Any] = ...): ...
def chain_matmul(*matrices: Any): ...
def pstrf(a: Any, upper: bool = ..., out: Optional[Any] = ...): ...
def potrf(a: Any, upper: bool = ..., out: Optional[Any] = ...): ...
def potri(a: Any, upper: bool = ..., out: Optional[Any] = ...): ...
def potrs(b: Any, u: Any, upper: bool = ..., out: Optional[Any] = ...): ...
def gesv(b: Any, A: Any, out: Optional[Any] = ...): ...
def trtrs(b: Any, A: Any, upper: bool = ..., transpose: bool = ..., unitriangular: bool = ..., out: Optional[Any] = ...): ...
def btrifact(A: Any, pivot: bool = ..., out: Optional[Any] = ...): ...
def btrifact_with_info(A: Any, pivot: bool = ..., out: Optional[Any] = ...): ...
def btriunpack(LU_data: Any, LU_pivots: Any, unpack_data: bool = ..., unpack_pivots: bool = ...): ...
def btrisolve(b: Any, LU_data: Any, LU_pivots: Any, out: Optional[Any] = ...): ...
def lu(A: Any, pivot: bool = ..., get_infos: bool = ..., out: Optional[Any] = ...): ...
