import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:

    l=0

    for i in range(len(A)):
        if A[i]%2==0:
            A[l],A[i]=A[i],A[l]
            l+=1
    
    
    # e,o=0,len(A)-1

    # while e<o:
    #    if A[e]%2==0:
    #        e+=1
    #    else:
    #        A[e],A[o]=A[o],A[e]
    #        o-=1



@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
