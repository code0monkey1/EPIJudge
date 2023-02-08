from test_framework import generic_test

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
   
    # bit_mask=(2**16)-1
    # bit_shift=16
    
    # return memo[x>>(bit_shift*3)] ^ memo[(x>>(bit_shift*2))&bit_mask] ^ memo[(x>>bit_shift)&bit_mask] ^ memo[x & bit_mask]
    
    n =32
    
    while n:
        x ^=(x >>n)
        n//=2
    
    return x&1
        
  

if __name__ == '__main__':
    # pre_compute()
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
