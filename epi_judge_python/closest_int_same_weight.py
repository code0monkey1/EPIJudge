from test_framework import generic_test

def closest_int_same_bit_count(x: int) -> int:
    pass
    # TODO - you fill in here.
    
    # for i in range(63):
        
    #     if ((x>>i&1) ^ (x>>(i+1)&1)):
    #         return x^ (1<<i |1 <<(i+1))
    
    # raise ValueError("All bits are 0 or 1")
        
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
