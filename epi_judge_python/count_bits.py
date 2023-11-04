from test_framework import generic_test

# Basic : Do in O(n) , where n is the number of bits to  represent integer (Eg: 12 ( 1100 ) needs 4 bits to represent integer , so here n = 4)

# Optimized 1 : Do in O(m) , where m is the number of set bits in integer ( Eg : 12 ( 1110 ) has 2 set bits , so m = 2 )

# Optimized 3 : Do in O(m) * k

def count_bits(x: int) -> int:
    count =0
    while x:
        count+=(x&1)
        x>>= 1
    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
