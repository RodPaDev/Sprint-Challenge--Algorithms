#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
  - `a = 0` is a simple operation that takes **O(1)**  
  - `while ( a < n * n * n)` while it looks like it takes **O(n^2)**, in fact it's **O(n)** because the ` n * n * n` is only calculating how many times it should loop in the first place, meaning it will first calculate what n^3 is and then compare a to it, e.g.: `0 < 3^3` or `0 < 9`
  - `a = a + n * n` is also a simple operation and it takes **O(1)**

   **The code in the snippet has a running-time complexity of O(n)**  

b)
  - `sum = 0` is a simple operation that takes **O(1)**
  - `for i in range(n):` this for loop takes **O(n)**
  - `j = 1` is a simple operation that takes **O(1)**
  - `BELOW` The while loop should've taken **O(n)** because it iterates over n. However, `j *= 2` shortens the runtime by a fraction making it **O(log n)**
  ```python
  while j < n:
  j *= 2 
  sum += 1
  ```

  Knowing that the first loop takes **O(n)** and the second **(log n)**, **we can conclude that the whole code snippet has a running time complexity of O(n log n)**

c)
  - `def bunnyEars(bunnies):` is a simple operation that takes **O(1)**
  - `if bunnies == 0:` is a simple operation that takes **O(1)**
  - `return 0` is a simple operation that takes **O(1)**
  - `return 2 + bunnyEars(bunnies-1)` this will take **O(1) * O(n)**

  **The runnig time-complexity is **O(n)** because it is dependent of the size of the input**
## Exercise II

```
Declare variable n = Number of stories in the building
Declare variable f = Limit from which floor the thrown egg will break

for each story in n
  check if the Egg is Broken
    true: increment f by 1
    false: do nothing

end of loop

return f
```


