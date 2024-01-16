from test_framework import generic_test


def divide(x: int, y: int) -> int:
  pass

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
