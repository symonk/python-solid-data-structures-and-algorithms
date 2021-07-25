"""
This document outlines everything to do with sets, specifically in python however a lot of the content
and venn diagrams etc apply to general set theory and provide a generic understanding.

Python sets:
    * Unordered, non indexable mutable collections of distinct immutable, hashable elements.
    * Come in two flavours, :class:`set` and :class:`frozenset`.
"""

# -------------------------------------------------------------------------------------------------------

"""
Creating a set:

    >>> empty_set = set()
    >>> set_from_iter = set(range(10))
    >>> s = {"s", "o"}
    
    Strings themselves are also iterable:
    >>> unique_chars = set("example")
    >>> {"e", "x", "a", "m", "p", "l"}
    
    Care is advised when trying to make an empty set via the `{}` syntax
    as by default python will create a dictionary.
    
    >>> s = {}
    >>> type(s)
    >>> dict
"""

# -------------------------------------------------------------------------------------------------------
