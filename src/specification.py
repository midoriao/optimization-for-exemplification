from typing import TypeVar

from signal_tl import (Always, And, Area, AvAlways, AvEventually, Const,
                       Eventually, Not, Or, Predicate, Until)

Spec = TypeVar("Spec", Always, And, Const, Eventually, Not, Or,
                             Predicate, Until, AvAlways, AvEventually, Area)


def eq(predicate: Predicate, value: float, epsilon: float = 1e-3) -> Predicate:
    """A helper function to specify equality of a variable to a value.
    e.g. `eq(x, 0)` is equivalent to `x == 0`.

    Args:
        predicate: The predicate that represents the variable.
        value: The value to be compared to.
        epsilon: The tolerance of the equality.
    """
    return (predicate > value - epsilon) & (predicate < value + epsilon)
