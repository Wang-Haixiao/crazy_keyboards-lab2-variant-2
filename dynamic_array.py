class DynamicArray(object):
    def __init__(self, lst=[], capacity=0):
        self._capacity = capacity
        self._size = len(lst)
        self._GrowthFactor = 2
        if self._capacity < self._size:
            DynamicArray.__grow__(self)
        self._items = [None for i in range(self._capacity)]
        for i in range(len(lst)):
            self._items[i] = lst[i]

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < self._size:
            x = self._items[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration

    def __grow__(self):
        while self._capacity < self._size:
            self._capacity += 1
            self._capacity *= self._GrowthFactor

    def __str__(self):
        return str(self._items[0:self._size])

    def __eq__(self, other):
        if (self._size == length(other)) and (type(other) is DynamicArray):
            for i in range(self._size):
                if self.array()[i] != other.array()[i]:
                    return False
            return True
        return False

    def size(self):
        return self._size

    def array(self):
        return self._items[0:self._size]


# 1 Add a new element
def cons(element, arr):
    l = [element] + arr.array()
    new_arr = DynamicArray(l)
    new_arr._size = length(arr) + 1
    return new_arr


# 2 Remove an element by value
def remove(arr, element):
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[0]
    rest_arr = DynamicArray(arr.array()[1:length(arr)])
    if v == element:
        return DynamicArray(arr.array()[1:length(arr)])
    return cons(v, remove(rest_arr, element))


# 3 Size
def length(arr):
    if arr is None:
        return 0
    assert type(arr) is DynamicArray
    return arr.size()


# 4 Is member
def member(arr, element):
    if length(arr) == 0:
        return False
    v = arr.array()[0]
    rest_arr = DynamicArray(arr.array()[1:length(arr)])
    if v == element:
        return True
    return member(rest_arr, element)


# 5 Reverse
def reverse(arr):
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[length(arr) - 1]
    rest_arr = DynamicArray(arr.array()[0:length(arr) - 1])
    return cons(v, reverse(rest_arr))


# 6 Intersection
def intersection(arr1, arr2):
    if length(arr1) == 0:
        return False
    v = arr1.array()[0]
    rest_arr = DynamicArray(arr1.array()[1:length(arr1)])
    if v in arr2.array():
        return True
    return intersection(rest_arr, arr2)


# 7 To built-in list
def to_list(arr):
    res = []

    def builder(lst):
        if length(lst) == 0:
            return res
        v = lst.array()[0]
        rest_arr = DynamicArray(lst.array()[1:length(arr)])
        res.append(v)
        return builder(rest_arr)

    return builder(arr)


# 8 From built-in list
def from_list(lst):
    if len(lst) == 0:
        return DynamicArray()
    return cons(lst[0], from_list(lst[1:]))


# 9 Find element by specific predicate
def find(arr, func=None):
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return False
    v = arr.array()[0]
    rest_arr = DynamicArray(arr.array()[1:length(arr)])
    if func(v):
        return True
    return find(rest_arr, func)


# 10 Filter data structure by specific predicate
def filter(arr, func=None):
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[0]
    rest_arr = DynamicArray(arr.array()[1:length(arr)])
    if func(v):
        return cons(v, filter(rest_arr, func))
    return filter(rest_arr, func)


# 11 Map structure by specific function
def map(arr, func=None):
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return DynamicArray()
    v = arr.array()[0]
    rest_arr = DynamicArray(arr.array()[1:length(arr)])
    return cons(func(v), map(rest_arr, func))


# 12 Reduce process elements and build a value by the function
def reduce(arr, func, initial_state):
    assert callable(func), "The function is not callable."
    if length(arr) == 0:
        return initial_state
    v = arr.array()[0]
    rest_arr = DynamicArray(arr.array()[1:length(arr)])
    state = func(initial_state, v)
    return reduce(rest_arr, func, state)


# 13 Function style iterator
def iterator(arr):
    l = arr
    len = length(l)
    i = 0

    def foo():
        nonlocal l
        nonlocal len
        nonlocal i
        if (i >= len) | (l is None):
            raise StopIteration
        tmp = l.array()[i]
        i += 1
        return tmp

    return foo


# 14 Data structure should be a monoid and implement empty
def mempty():
    return DynamicArray()


# 15 Data structure should be a monoid and implement concat
def concat(arr1, arr2):
    l1 = to_list(arr1)
    l2 = to_list(arr2)
    return DynamicArray(l1 + l2)
