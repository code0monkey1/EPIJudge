# Find the parity of a world ( number ) in python : 

1. Parity is 1 if no of set bits is odd ( eg 1011)
2. Parity is 0 if no of set bis is even  ( eg 1010 )


---

# Solution : 

### O(n) , where n is the word size 

<details>
<summary>Hint</summary>

_you could easily count the number of set bits by xoring all bits and return true is the result is 1 (i.e odd number of bits) , if the bits were not odd , the xor would be zero_  

</details>


<details>

<summary> Solution </summary>

```python
    
def parity(x):
      count =0
           
      while x:
            count ^= x&1
            x>>= 1
          
      return count     
```

</details>

--- 
### Optimization 1 :  ( O(k) ) , where k is the number of set bits:

<br/>

<details>
<summary>Hint</summary>

_you could easily count the number of set bits only by using x & (x-1) , which would eliminate 1 set bit each time , you only need to return how many times till x got to zero, if odd , true , if even false_  

</details>


---

<details>

<summary> Solution </summary>


```python
 def parity(x):
    par=0
    while x:
        par^=1
        x&=(x-1)
    return par
       
```

</details>


---

#### Optimization 2 : O ( n/L ) , where n is the word length, and L is the length of the world size used to hash precomputed values

<br/>

<details>
<summary>Hint</summary>

_you could easily count the number of set bits only by using x & (x-1) , which would eliminate 1 set bit each time , you only need to return how many times till x got to zero, if odd , true , if even false_  

</details>


---

<details>

<summary> Solution </summary>


```python
 mem=[0]*(2**16)

def pre_compute():
    for i in range(2**16):
        mem[i] = _parity(i)
    
def _parity(x: int) -> int:
    
    result = 0
    while x:
        x=(x & (x-1))
        result^=1
    return result
  

def parity(num):
    mask = 2**16-1
    shift=16
    return mem[ num>> (shift*3)] ^ \
           mem[ (num>> (shift*2)) & mask] ^ \
           mem[ (num>>shift ) & mask] ^ \
           mem[ num & mask] 
               

if __name__ == '__main__':
    pre_compute() #  pre-compute before running function
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))

```

</details>

---

#### Optimization 2 : O ( n/L ) , where n is the word length, and L is the length of the world size used to hash precomputed values

<br/>

<details>
<summary>Hint</summary>

_you could easily count the number of set bits only by using x & (x-1) , which would eliminate 1 set bit each time , you only need to return how many times till x got to zero, if odd , true , if even false_  

</details>


---

<details>

<summary> Solution </summary>


```python
 def parity(x):
    par=0
    while x:
        par^=1
        x&=(x-1)
    return par
       
```

</details>



