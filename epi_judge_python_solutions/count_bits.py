from test_framework import generic_test


def count_bits(x: int) -> int:

    tot=0

    while x:
        tot+=1
        x&=(x-1)
    
    return tot

    # num_bits = 0
    # while x:
    #     num_bits += x & 1
    #     x >>= 1
    # return num_bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
