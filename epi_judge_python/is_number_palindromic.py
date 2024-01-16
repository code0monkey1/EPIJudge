from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    
    if x<0:
        return False
    
#log10 for zero gives VAlueError , so handle that 
    if x==0:
        return True
    
    divisor=10**(int(math.log10(x)))

    while x:
        f = x//divisor
        l=x%10

        if f!=l:
            return False
        
        x%=divisor
        x//=10
        divisor//=100
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
