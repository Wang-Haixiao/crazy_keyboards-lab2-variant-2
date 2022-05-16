# crazy-keyboards - lab 2 - variant 2

Group Member:

- Haixiao Wang 212320012
- Yu Zhang     212320015

## Variant description

- Dynamic array,

and should check the implementation correctly works with None value.

## Project structure

- `dynamic_array.py` -- implementation of `DynamicArray` immutable version.
   
- `dynamic_array_test.py` -- unit and PBT tests for `DynamicArray`.

## Features

- PBT test: `test_cons`, `test_remove`, `test_length`, `test_member`, `test_reverse`,

`test_intersection`, `test_to_list`, `test_to_list_from_list_equality`, `test_concat`,

`test_monoid_identity`, `test_str`, `test_eq`.

- Other unit test: `test_from_list`, `test_find`, `test_filter`, `test_map`,

`test_reduce`, `test_iterator`, `test_empty`.

- API test: `test_api`.

## Contribution

- Haixiao Wang -- source part and upload the files to github

- Yu Zhang -- test part

## Changelog

- 16.05.2022 - 1
  - Update README. Add formal sections.
  - Fixed some formatting issues
- 12.04.2022 - 0
  - Initial

## Design notes

- By comparing the mutable implementation in Lab1, we find that, unlike directly modifying 
the original data, the immutable implementation uses a new area in memory 
to store the data without changing the original data.
This design is more suitable for multi-threaded programming and provides greater security.

- Implementation restrictions
  - Avoid unnecessary data replication.
  - Use recursion to implement most of your functions, instead of loops.
  - Note the immutability of data structures