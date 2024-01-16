from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:

    for i in range(63):
       r=x>>i
       l=x>>(i+1)

       if (l&1) ^ (r&1):
           mask= 1<<i| 1<<(i+1)
           x^=mask 
           return x          

    # Raise error if all bits of x are 0 or 1.
    raise ValueError('All bits are 0 or 1')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
