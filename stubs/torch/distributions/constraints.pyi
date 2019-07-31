# Stubs for torch.distributions.constraints (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Constraint:
    def check(self, value: Any) -> None: ...

class _Dependent(Constraint):
    def check(self, x: Any) -> None: ...

def is_dependent(constraint: Any): ...

class _DependentProperty(property, _Dependent): ...

class _Boolean(Constraint):
    def check(self, value: Any): ...

class _IntegerInterval(Constraint):
    lower_bound: Any = ...
    upper_bound: Any = ...
    def __init__(self, lower_bound: Any, upper_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _IntegerLessThan(Constraint):
    upper_bound: Any = ...
    def __init__(self, upper_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _IntegerGreaterThan(Constraint):
    lower_bound: Any = ...
    def __init__(self, lower_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _Real(Constraint):
    def check(self, value: Any): ...

class _GreaterThan(Constraint):
    lower_bound: Any = ...
    def __init__(self, lower_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _GreaterThanEq(Constraint):
    lower_bound: Any = ...
    def __init__(self, lower_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _LessThan(Constraint):
    upper_bound: Any = ...
    def __init__(self, upper_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _Interval(Constraint):
    lower_bound: Any = ...
    upper_bound: Any = ...
    def __init__(self, lower_bound: Any, upper_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _HalfOpenInterval(Constraint):
    lower_bound: Any = ...
    upper_bound: Any = ...
    def __init__(self, lower_bound: Any, upper_bound: Any) -> None: ...
    def check(self, value: Any): ...

class _Simplex(Constraint):
    def check(self, value: Any): ...

class _LowerTriangular(Constraint):
    def check(self, value: Any): ...

class _LowerCholesky(Constraint):
    def check(self, value: Any): ...

class _PositiveDefinite(Constraint):
    def check(self, value: Any): ...

class _RealVector(Constraint):
    def check(self, value: Any): ...

dependent: Any
dependent_property: Any
boolean: Any
nonnegative_integer: Any
positive_integer: Any
integer_interval: Any
real: Any
real_vector: Any
positive: Any
greater_than: Any
greater_than_eq: Any
less_than: Any
unit_interval: Any
interval: Any
half_open_interval: Any
simplex: Any
lower_triangular: Any
lower_cholesky: Any
positive_definite: Any
