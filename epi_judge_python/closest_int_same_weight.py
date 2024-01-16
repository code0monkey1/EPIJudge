from test_framework import generic_test

def closest_int_same_bit_count(x: int) -> int:
 unsigned=64

 for i in range(unsigned-1):
    #if ith bit is different from jth bit, wap
    if ( (x>>i) & 1 ) ^ ( (x>>(i+1))&1 ):
       return swap(i,i+1,x)
    
 #Raise error if all bits are zero or one 
 raise ValueError("All bits are 0 or 1")

def swap(i,j,x):
    mask = 1<<i | 1<<j
    x^=mask
    return x




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
