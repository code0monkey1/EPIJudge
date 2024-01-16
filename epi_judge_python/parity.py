from test_framework import generic_test

# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, 
# it is 0. 
# For example, the parity of 1011 is 1, and the parity of 10001000 is 0.

# Parity checks are used to detect single bit errors in data storage and communication. 
# It is fairly straightforward to write code that computes the parity of a single 64-bit word.
# How would you compute the parity of a very large number of 64-bit words?

# Hint: Use a lookup table, but don't use 264 entries!

mem=[0]*(2**16)
flag=2**16-1

def pre_compute():
    for i in range(2**16):
        mem[i] = _parity(i)
    

def _parity(x):
    power= 32

    while power:
       x^=(x>>power)
       power//=2
    
    return x&1

def parity(x):
    pow=32

    while pow:
        x^=(x>>pow)
        pow//=2
    
    return x&1


    # res= (_parity(x&(flag)) ^ _parity((x>>16)&(flag)) ^_parity( (x>>(16*2))&(flag)) \
    # ^_parity( (x>>(16*3))&(flag)))
    # return res & 1
 

if __name__ == '__main__':
    pre_compute()
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
