## Count the number of bits that are set to 1 in a `non-negative integer`

#### Brute Force : 
_See if the rightmost bit is set to 1 in x by doing ( x & 1 ) , count +1 it if it was , then shift the original number one to the right . Do this till the number is non-zero_

```python

  def count_bits(x: int) -> int:
       count =0
       
       while x:
           count += x&1
           x>> = 1
      
       return count
      
```

Time Complexity : `O(n), where n is the number of bits in the original number`

---

#### Optimization 1 : 


_Do the same by only counting the `set bits`_

> Hint : x&(X-1) gives a number with the first rightmost set-bit removed from x
> 
>  Eg: if x= 110 , then x&(X-1) gives 100, i.e the rightmost set-bit is removed

```python
  
  def count_bits(x: int) -> int:
       count =0
       
       while x:
           count += 1
           x&=(x-1)
      
       return count
    
```

Time Complexity : `O(Number of Set Bits in (x)) `