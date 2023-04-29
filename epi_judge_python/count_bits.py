from test_framework import generic_test

# Do in O(n) , where n is the number of bits to  represent integer (Eg: 12 ( 1100 ) needs 4 
# bits to represent integer , so here n = 4)

def count_bits(x: int) -> int:
 pass


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
