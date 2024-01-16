from test_framework import generic_test


def swap_bits(x, i, j): # quite easy
    # TODO - you fill in here.

    if (x>>i &1) ^ (x>>j &1):
        mask = 1<<i | 1<<j
        x^=mask
    
    return x
    # extract the ith bit and the jth bit and xor it to see it they different ( will be  true if different )

    # If the ith and jth bit are different : Next , create a bitmask for ith and jth positions , and xor the original value with it to swap bits 
    
    # if (x>>i)&1 ^ (x>>j)&1:
    #     mask = (1<<i) | (1<<j)
    #     x^=mask 
    
    # return x

      
    # if (x>>i)&1 ^ (x>>j)&1:
    #     x^=(1<<i)| (1<<j)
    # is_different=(x>>i & 1) ^ ( x>>j & 1)
    
    # if is_different:
    #     bit_mask = 1<<i | 1<<j
    #     return x ^ bit_mask
    
    # return x
    
    # is_different=(x>>i & 1) ^ (x>>j & 1)
    
    # if is_different:
    #     bit_mask=1<<i | 1<<j
    #     return x ^ bit_mask
    
    # return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
