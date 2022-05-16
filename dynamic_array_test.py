import unittest
from hypothesis import given
import hypothesis.strategies as st

from dynamic_array import DynamicArray, cons, remove, length
from dynamic_array import member, reverse, intersection, to_list
from dynamic_array import from_list, find, filter, map
from dynamic_array import reduce, iterator, mempty, concat


class TestDynamicArray(unittest.TestCase):
    # 1 cons
    @given(lst=st.lists(st.integers()), num=st.integers())
    def test_cons(self, lst, num):
        arr = from_list(lst)
        lst.insert(0, num)
        self.assertEqual(cons(num, arr), from_list(lst))

    # 2 remove
    @given(lst=st.lists(st.integers()), num=st.integers())
    def test_remove(self, lst, num):
        lst.insert(0, num)
        arr = from_list(lst)
        self.assertNotEqual(remove(arr, num), from_list(lst))
        self.assertEqual(remove(arr, num), from_list(lst[1:]))

    # 3 Size
    @given(lst=st.lists(st.integers()))
    def test_length(self, lst):
        arr = from_list(lst)
        self.assertEqual(length(arr), len(lst))
        self.assertEqual(length(cons(None, arr)), len(lst)+1)

    # 4 Is member
    @given(lst=st.lists(st.integers()), num=st.integers())
    def test_member(self, lst, num):
        arr = from_list(lst)
        if None not in lst:
            self.assertFalse(member(arr, None))
        arr = cons(num, arr)
        self.assertTrue(member(arr, num))

    # 5 Reverse
    @given(lst=st.lists(st.integers()))
    def test_reverse(self, lst):
        arr = from_list(lst)
        lst.reverse()
        self.assertEqual(reverse(arr), from_list(lst))

    # 6 Intersection
    @given(lst1=st.lists(st.integers()), lst2=st.lists(st.text()))
    def test_intersection(self, lst1, lst2):
        arr1 = from_list(lst1)
        arr2 = from_list(lst2)
        if (lst1 != []) | (lst2 != []):
            self.assertFalse(intersection(arr1, arr2))
            self.assertTrue(intersection(cons(None, arr1), cons(None, arr2)))

    # 7 To built-in list
    @given(lst=st.lists(st.integers()))
    def test_to_list(self, lst):
        arr = DynamicArray(lst)
        self.assertEqual(to_list(arr), lst)

    # 8 From built-in list
    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            self.assertEqual(to_list(from_list(e)), e)

    # 7&8 To built-in list & From built-in list
    @given(lst=st.lists(st.integers()))
    def test_to_list_from_list_equality(self, lst):
        self.assertEqual(to_list(from_list(lst)), lst)

    # 9 Find element by specific predicate
    def test_find(self):
        arr = from_list([1, 2, 3])
        self.assertFalse(find(arr, (lambda x: x > 3)))
        self.assertTrue(find(arr, (lambda x: x % 2 == 0)))
        self.assertTrue(find(cons(4, arr), (lambda x: x > 3)))

    # 10 Filter data structure by specific predicate
    def test_filter(self):
        arr = from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(filter(arr, (lambda x: x % 2 == 0)), from_list([2, 4, 6, 8, 10]))
        self.assertEqual(filter(arr, (lambda x: x > 5)), from_list([6, 7, 8, 9, 10]))
        self.assertEqual(filter(arr, (lambda x: x > 10)), from_list([]))

    # 11 Map structure by specific function
    def test_map(self):
        arr = from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(map(arr, (lambda x: x ** 2)), from_list([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))
        self.assertEqual(map(arr, (lambda x: x + 1)), from_list([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
        self.assertEqual(map(arr, (lambda x: x ** 0)), from_list([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

    # 12 Reduce process elements and build a value by the function
    def test_reduce(self):
        arr = from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(reduce(arr, (lambda x, y: x + y), 0), 55)
        self.assertEqual(reduce(arr, (lambda x, y: x + y), 1), 56)
        self.assertEqual(reduce(arr, (lambda x, y: x + y ** 2), 1), 386)
        self.assertEqual(reduce(arr, (lambda x, y: x ** 0 + y), 1), 11)

    # 13 Function style iterator
    def test_iterator(self):
        lst = [1, 2, 3]
        arr = from_list(lst)

        tmp = []
        try:
            get_next = iterator(arr)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(lst, tmp)
        self.assertEqual(to_list(arr), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

    # 14 Data structure should be a monoid and implement empty
    def test_empty(self):
        self.assertEqual(mempty(), DynamicArray())
        self.assertEqual(mempty(), from_list([]))
        self.assertNotEqual(mempty(), None)

    # 15 Data structure should be a monoid and implement concat
    @given(lst1=st.lists(st.integers()), lst2=st.lists(st.integers()))
    def test_concat(self, lst1, lst2):
        arr1 = from_list(lst1)
        arr2 = from_list(lst2)
        self.assertEqual(concat(arr1, arr2), from_list(lst1 + lst2))

    # 14&15 Monoid identity
    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        arr = from_list(lst)
        self.assertEqual(concat(mempty(), arr), arr)
        self.assertEqual(concat(arr, mempty()), arr)

    # 16 String serialization
    @given(lst1=st.lists(st.integers()), lst2=st.lists(st.integers()))
    def test_str(self, lst1, lst2):
        a = from_list(lst1)
        b = from_list(lst1)
        c = from_list(lst2)
        self.assertEqual(str(a), str(lst1))
        self.assertEqual(str(c), str(lst2))
        self.assertEqual(str(a), str(b))

    # 17 Check equality method
    @given(lst1=st.lists(st.integers()), lst2=st.lists(st.integers()))
    def test_eq(self, lst1, lst2):
        a = from_list(lst1)
        b = from_list(lst1)
        c = from_list(lst2)
        self.assertEqual(a, b)
        if lst1 != lst2:
            self.assertNotEqual(a, c)
            self.assertNotEqual(b, c)
        else:
            self.assertEqual(a, c)
            self.assertEqual(b, c)

    # 18 API test
    def test_api(self):
        empty = DynamicArray()
        l1 = cons(None, cons(1, empty))
        l2 = cons(1, cons(None, empty))
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(None, cons(1, empty)))
        self.assertEqual(length(empty), 0)
        self.assertEqual(length(l1), 2)
        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, None)), "[1]")
        self.assertEqual(str(remove(l1, 1)), "[None]")
        self.assertFalse(member(empty, None))
        self.assertTrue(member(l1, None))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))
        self.assertEqual(l1, reverse(l2))
        self.assertEqual(to_list(l1), [None, 1])
        self.assertEqual(l1, from_list([None, 1]))
        self.assertEqual(concat(l1, l2), from_list([None, 1, 1, None]))
        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [None, 1])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])

        '''filter, map, reduce, empty'''
        self.assertEqual(filter(l1, lambda x: type(x) is int), from_list([1]))
        self.assertEqual(filter(l2, lambda x: type(x) is int), from_list([1]))
        self.assertEqual(filter(l1, lambda x: x is None), from_list([None]))
        self.assertEqual(filter(l2, lambda x: x is None), from_list([None]))

        l3 = from_list([1, 2, 3, 4])
        l4 = from_list(['cpu', 'gpu', 'storage', 'input', 'output'])
        self.assertEqual(map(l3, lambda x: x ** 2), from_list([1, 4, 9, 16]))
        self.assertEqual(map(l3, lambda x: x - 1), from_list([0, 1, 2, 3]))
        self.assertEqual(map(l4, lambda x: x[0]), from_list(['c', 'g', 's', 'i', 'o']))
        self.assertEqual(reduce(l3, (lambda x, y: x + y), 0), 10)
        self.assertEqual(reduce(l3, (lambda x, y: x + y), 1), 11)
        self.assertEqual(reduce(l3, (lambda x, y: x ** 2 + y), 0), 148)
        self.assertEqual(reduce(l3, (lambda x, y: x ** 2 + y), 1), 1525)
        self.assertEqual(reduce(l4, (lambda x, y: x + y + '_'), ''), 'cpu_gpu_storage_input_output_')
        self.assertEqual(mempty(), DynamicArray())


if __name__ == '__main__':
    unittest.main()