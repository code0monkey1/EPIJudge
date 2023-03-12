from test_framework import generic_test
mem=[0]*2**16

# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, 
# it is 0. 
# For example, the parity of 1011 is 1, and the parity of 10001000 is 0.

# Parity checks are used to detect single bit errors in data storage and communication. 
# It is fairly straightforward to write code that computes the parity of a single 64-bit word.
# How would you compute the parity of a very large number of 64-bit words?

# Hint: lJse a lookup table, but don't use 264 entries!

def pre_compute():
    for i in range(2**16):
        mem[i]=_parity(i)
        
    

def _parity(num):
    result =0
    while num:
        result^=1
        num=(num &(num-1))
    return result
    
# memo = [0]*(2**16)

# def pre_compute():
#     for i in range(2**16):
#         memo[i] =single_parity(i)

# def single_parity(x):
    
#     parity=0
    
#     while x:
#         parity^=1
#         x&=(x-1)
        
#     return parity
    

def parity(x: int) -> int:
    # TODO - you fill in here.
    n=32
     
    while n:
        x^=(x>>n)
        n//=2
    return x&1
        
    
   
    
    # parity=0
    
    # while x:
    #     parity^=(x&1)
    #     x>>=1
    
    # return parity
     
    #  bit_mask=(2**16)-1
     
    #  bit_shift=16
     
     
    #  return mem[x>>bit_shift*3 & bit_mask]^\
    #         mem[x>>bit_shift*2 & bit_mask]^\
    #         mem[x>>bit_shift & bit_mask]^\
    #         mem[x & bit_mask]
     
   
    # bit_mask=(2**16)-1
    # bit_shift=16
    
    # return memo[x>>(bit_shift*3)] ^ memo[(x>>(bit_shift*2))&bit_mask] ^ memo[(x>>bit_shift)&bit_mask] ^ memo[x & bit_mask]
    
    # n =32
    
    # while n:
    #     x ^=(x >>n)
    #     n//=2
    
    # return x&1
        
  

if __name__ == '__main__':
    pre_compute()
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
