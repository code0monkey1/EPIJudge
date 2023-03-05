from test_framework import generic_test
import math
def add(a:int,b:int)->int:
    return a if b==0 else add(a^b , (b&a)<<1)
    

def multiply(x: int, y: int) -> int:
    # TODO - you fill in here.
    total=0

    while x:
        if x&1:
            total=add(total,y)
        x,y=x>>1,y<<1
    
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
