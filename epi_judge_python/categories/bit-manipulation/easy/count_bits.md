## Count the number of bits that are set to 1 in a `non-negative integer`

`count_bits`
#### Brute Force [ O(n) , where n is the number of bits used to represent the number ]

<details>
<summary>Hint</summary>

_See if the rightmost bit is set to 1 in x by doing ( x & 1 ) , count +1 it if it was , then shift the original number one to the right . Do this till the number is non-zero_  

</details>

<details>
<summary> Bruite Force Solution </summary>

```python   
    
      def count_bits(x: int) -> int:
           count =0
           
           while x:
               count += x&1
               x>> = 1
          
           return count
          
```
</details>

Time Complexity : `O(n), where n is the number of bits needed to represent the integer. Eg: 4 bits are needed to represent the integer 12 ( 1100 )`

---

#### Optimization 1 [O(m) , where m is the number of set bits] : 


_Do the same by only counting the `set bits`_

<details>
<summary> Hint 1 </summary>

 _x&(x-1) drops the lowest set bit of x_

_Eg: if x= 110 , then x&(X-1) gives 100, i.e the rightmost set-bit is removed_

</details>

>  

```python
  
  def count_bits(x: int) -> int:
       count =0
       
       while x:
           count += 1
           x&=(x-1)
      
       return count
    
```

Time Complexity : `O(Number of Set Bits in (x)) `