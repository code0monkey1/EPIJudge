from test_framework import generic_test

rev_memo =[0]* (2**16)

def pre_compute_rev():
    
    for i in range(2**16):
      rev_memo[i] =  _reverse_bits(i)


def swap_bits(x,i,j):
    
     bits_different=( (x>>i) &1) ^ ((x>>j)&1)
     
     if ( bits_different ):
        bit_mask=1<<i | 1<<j
        return x ^ bit_mask
    
     return x
 
def _reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    #swap bits at each index from 0 to len-1, sequentially
    
    for i in range(8):
        j = i
        k = 16 - i-1
        x=swap_bits(x,j,k)    
    
    return x

def reverse_bits(x:int) -> int:
    
    bit_shift=16
    bit_mask=(2**16)-1
    
    return rev_memo[x&bit_mask]<<(bit_shift*3) |\
           rev_memo[(x>>bit_shift)&bit_mask]<<(bit_shift*2)|\
           rev_memo[(x>>(bit_shift*2))&bit_mask]<<bit_shift|\
           rev_memo[(x>>(bit_shift*3))&bit_mask]      
    



if __name__ == '__main__':
    pre_compute_rev()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
