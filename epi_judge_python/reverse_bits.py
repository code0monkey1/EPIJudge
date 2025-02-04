
from test_framework import generic_test
arr = [0]*(2**16)
# memo =[0]*2**16
def rev_bits(n:int)->int:
        res = 0
        for i in range(16):
            res<<=1
            if n&1:
                res+=1
            n>>=1
        return res

def pre_compute():
        for i in range(2**16):
            arr[i]=rev_bits(i)
    
# def swap_bits(digit,j,k):
#     if ( ((digit>>j )&1 )^ ((digit>>k) &1) ):
#         digit^= 1<<j | 1<<k
#     return digit


# def reverse(digit):
#     for i in range(8):
#         digit= swap_bits(digit,i,16-i-1)
#     return digit

# def reverse_16_bits(x)->int:
#     for i in range(8):
#         x=swap_bits(x,i,16-i-1)
#     return x
 
# def memoize():
#     for i in range(2**16):
#         memo[i]=reverse(i)

def reverse_bits(n):
    
    res=0
    for i in range(4):
        temp = n>>(16*i)
        mask = arr[temp & ((2**16)-1)]
        res = (res<<16) | mask
        
    return res

    #  res=0
    #  for _i in range(64):
    #      res<<=1 
    #      res+=(digit&1)
    #      digit>>=1
    #  return res


# memo =[0]*(2**16)
 
# def memoise():
#     for i in range(1,2**16):
#         memo[i] =reverse_16_bits(i)
        
    
# def reverse_bits(x:int)->int:
#     bit_mask=2**16-1
#     bit_shift=16
    
#     return memo[x&bit_mask]<<bit_shift*3|\
#            memo[(x>>bit_shift)&bit_mask]<<bit_shift*2|\
#            memo[(x>>(bit_shift*2))&bit_mask]<<bit_shift|\
#            memo[(x>>(bit_shift*3))&bit_mask]


# def swap_bits(x,i,j)->int:
#     if ( (x>>i)&1 ^ (x>>j)&1 ):
#         x^=(1<<i) | (1<<j)
#     return x

# def reverse_16_bits(x)->int:
#     for i in range(8):
#         x=swap_bits(x,i,16-i-1)
#     return x
 
# rev_memo =[0]* (2**16)

# def pre_compute_rev():
    
#     for i in range(2**16):
#       rev_memo[i] =  _reverse_bits(i)


# def swap_bits(x,i,j):
    
#      bits_different=( (x>>i) &1) ^ ((x>>j)&1)
     
#      if ( bits_different ):
#         bit_mask=1<<i | 1<<j
#         return x ^ bit_mask
    
#      return x
 
# def _reverse_bits(x: int) -> int:
#     # TODO - you fill in here.
#     #swap bits at each index from 0 to len-1, sequentially
    
#     for i in range(8):
#         j = i
#         k = 16 - i-1
#         x=swap_bits(x,j,k)    
    
#     return x

# def reverse_bits(x:int) -> int:
    
#     bit_shift=16
#     bit_mask=(2**16)-1
    
#     return rev_memo[x&bit_mask]<<(bit_shift*3) |\
#            rev_memo[(x>>bit_shift)&bit_mask]<<(bit_shift*2)|\
#            rev_memo[(x>>(bit_shift*2))&bit_mask]<<bit_shift|\
#            rev_memo[(x>>(bit_shift*3))&bit_mask]      
    


if __name__ == '__main__':
    pre_compute()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
