# Write a program to count the number of bits that are set to 1 in a `non-negative integer`

---
#### Brute Force : 
_See if the rightmost bit is set to 1 in x by doing ( x & 1 ) , count +1 it if it was , then shift the original number one to the right . Do this till the number is non-zero_

`O(n), where n is the number of bits in the original number`
#### Optimization 1 : 

_Do the same by only counting the `set bits`_

> Hint : x&(X-1) gives a number with the first rightmost set-bit removed 
> 
>  Eg: if x= 110 , then x&(X-1) gives 100, i.e the rightmost set-bit is removed