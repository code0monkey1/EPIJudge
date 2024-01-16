from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    
    tot=0

    while x:
        if x&1:
            tot=add_bits(y,tot)
        x>>=1
        y<<=1
    
    return tot
    
    # res = 0

    # while y: # while there are any set bits in y

    #     if y&1:
    #         res=add_bits(x,res)
        
    #     y>>=1
    #     x<<=1

    # return res

def add_bits(x,y):
    return x if not y else add_bits(x^y,((x&y)<<1))
    # return x if y==0 else add_bits(x^y , (x&y)<<1 )

    # def add(a: int, b: int)->int:
    #     return a if b==0 else add((a^b),(a&b)<<1)
    # total=0
    
    # while x:
    #     if x&1:
    #         total = add(total,y)
    #     x,y=x>>1,y<<1
    # return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
