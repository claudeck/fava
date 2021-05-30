# pylint: disable=missing-docstring,unused-argument,multiple-statements

import datetime
from typing import Any
from typing import NamedTuple
from typing import Optional
from typing import Union

from beancount.core.amount import Amount
from beancount.core.data import Posting
from beancount.core.number import Decimal

class Cost(NamedTuple):
    number: Decimal
    currency: str
    date: datetime.date
    label: Optional[str]

class CostSpec(NamedTuple):
    number_per: Optional[Decimal]
    number_total: Optional[Decimal]
    currency: Optional[str]
    date: Optional[datetime.date]
    label: Optional[str]
    merge: Optional[bool]

# def cost_to_str(cost: Any, dformat: Any, detail: bool = ...): ...

# CURRENCY_ORDER: Any
# NCURRENCIES: Any

class _Position(NamedTuple):
    units: Amount
    cost: Cost

class Position(_Position):
    def __new__(
        cls, units: Amount, cost: Optional[Cost] = ...
    ) -> "Position": ...
    # cost_types: Any = ...
    # def __hash__(self) -> Any: ...
    # def to_string(self, dformat: Any = ..., detail: bool = ...) -> str: ...
    # def __eq__(self, other: Any) -> Any: ...
    # def sortkey(self): ...
    # def __lt__(self, other: Any) -> Any: ...
    # def __copy__(self): ...
    # def currency_pair(self): ...
    # def get_negative(self): ...
    # __neg__: Any = ...
    # def __abs__(self): ...
    # def __mul__(self, scalar: Any): ...
    # def is_negative_at_cost(self): ...
    # @staticmethod
    # def from_string(string: Any): ...
    # @staticmethod
    # def from_amounts(units: Any, cost_amount: Optional[Any] = ...): ...

# from_string: Any
# from_amounts: Any

# def get_position(posting: Any): ...
def to_string(
    pos: Union[Position, Posting], dformat: Any = ..., detail: bool = ...
): ...
