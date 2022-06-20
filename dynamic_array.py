from typing import Any, Optional, List, Callable, Union


class DynamicArray(object):
    def __init__(self, lst: Optional[List[Any]] = [],
                 capacity: int = 0,
                 growth_factor: int = 2) -> None:
        self._capacity = capacity
        self._size = len(lst)
        self._GrowthFactor = growth_factor
        self._items = [None for i in range(self._capacity)]
        if self._capacity <= self._size:
            DynamicArray.grow(self)
        self._items[0:len(lst)] = lst[0:len(lst)]

    def __iter__(self) -> Any:
        self.a = 0
        return self

    def __next__(self) -> Any:
        if self.a < self._size:
            x = self._items[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration

    def __str__(self) -> str:
        return str(self._items[0:self._size])

    def __eq__(self, other: object) -> bool:
        if (type(other) is DynamicArray) and (self.array() == other.array()):
            return True
        return False

    def grow(self) -> None:
        if self._capacity == 0:
            self._capacity += 1
        while self._capacity < self._size + 1:
            self._capacity *= self._GrowthFactor
        self._items += [None] * (self._capacity - self._size)
        return

    def add(self, ele: Union[int, str, None]) -> None:
        if self._size == self._capacity:
            DynamicArray.grow(self)
        self._items[self._size] = ele
        self._size += 1

    def size(self) -> int:
        return self._size

    def array(self) -> List[Union[int, str, None]]:
        return self._items[0:self._size]


def cons(element: Union[int, str, None], arr: Optional[DynamicArray] = None) -> DynamicArray:
    """1: Add a new element"""
    new_arr = mempty()
    new_arr.add(element)
    for i in range(length(arr)):
        new_arr.add(arr.array()[i])
    return new_arr


def remove(arr: Optional[DynamicArray], element: Union[int, str, None]) -> DynamicArray:
    """2: Remove an element by value"""
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[0]
    rest_arr = from_list(arr.array()[1:length(arr)])
    if v == element:
        return from_list(arr.array()[1:length(arr)])
    return cons(v, remove(rest_arr, element))


def length(arr: Optional[DynamicArray]) -> int:
    """3: Size"""
    if arr is None:
        return 0
    assert type(arr) is DynamicArray
    return arr.size()


def member(arr: Optional[DynamicArray], element: Union[int, str, None]) -> bool:
    """4: Is member"""
    if length(arr) == 0:
        return False
    v = arr.array()[0]
    rest_arr = from_list(arr.array()[1:length(arr)])
    if v == element:
        return True
    return member(rest_arr, element)


def reverse(arr: Optional[DynamicArray]) -> DynamicArray:
    """5: Reverse"""
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[length(arr) - 1]
    rest_arr = from_list(arr.array()[0:length(arr) - 1])
    return cons(v, reverse(rest_arr))


def intersection(arr1: Optional[DynamicArray],
                 arr2: Optional[DynamicArray]) -> bool:
    """6: Intersection"""
    if length(arr1) == 0:
        return False
    v = arr1.array()[0]
    rest_arr = from_list(arr1.array()[1:length(arr1)])
    if v in arr2.array():
        return True
    return intersection(rest_arr, arr2)


def to_list(arr: Optional[DynamicArray]) -> List[Union[int, str, None]]:
    """7: To built-in list"""
    res = []

    def builder(lst):
        if length(lst) == 0:
            return res
        v = lst.array()[0]
        rest_arr = from_list(lst.array()[1:length(arr)])
        res.append(v)
        return builder(rest_arr)

    return builder(arr)


def from_list(lst: List[Union[int, str, None]]) -> DynamicArray:
    """8: From built-in list"""
    if len(lst) == 0:
        return DynamicArray()
    return cons(lst[0], from_list(lst[1:]))


def find(arr: Optional[DynamicArray],
         func: Optional[Callable[..., Any]] = None) -> bool:
    """9: Find element by specific predicate"""
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return False
    v = arr.array()[0]
    rest_arr = from_list(arr.array()[1:length(arr)])
    if func(v):
        return True
    return find(rest_arr, func)


def filter(arr: Optional[DynamicArray],
           func: Optional[Callable[..., Any]] = None) -> DynamicArray:
    """10: Filter data structure by specific predicate"""
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[0]
    rest_arr = from_list(arr.array()[1:length(arr)])
    if func(v):
        return cons(v, filter(rest_arr, func))
    return filter(rest_arr, func)


def map(arr: Optional[DynamicArray],
        func: Optional[Callable[..., Any]] = None) -> DynamicArray:
    """11: Map structure by specific function"""
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[0]
    rest_arr = from_list(arr.array()[1:length(arr)])
    return cons(func(v), map(rest_arr, func))


def reduce(arr: Optional[DynamicArray],
           func: Optional[Callable[..., Any]] = None,
           initial_state: Any = None) -> Any:
    """12: Reduce process elements and build a value by the function"""
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return initial_state
    v = arr.array()[0]
    rest_arr = from_list(arr.array()[1:length(arr)])
    state = func(initial_state, v)
    return reduce(rest_arr, func, state)


def iterator(arr: Optional[DynamicArray]) -> Any:
    """13: Function style iterator"""
    lst = arr
    len = length(lst)
    i = 0

    def foo():
        nonlocal lst
        nonlocal len
        nonlocal i
        if (i >= len) | (lst is None):
            raise StopIteration
        tmp = lst.array()[i]
        i += 1
        return tmp

    return foo


def mempty() -> DynamicArray:
    """14: Data structure should be a monoid and implement empty"""
    return DynamicArray()


def concat(arr1: Optional[DynamicArray],
           arr2: Optional[DynamicArray]) -> DynamicArray:
    """15: Data structure should be a monoid and implement concat"""
    rest_arr = arr1
    new_arr = arr2
    len = length(rest_arr)
    if len == 0:
        return new_arr
    v = rest_arr.array()[len-1]
    new_arr = cons(v, arr2)
    rest_arr = from_list(arr1.array()[0:len-1])
    return concat(rest_arr, new_arr)
