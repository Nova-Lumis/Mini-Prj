# Binary search
## Definition
<p>
  Binary search is a search algorithm to find a certain target value within a sorted array. 
</p>

<p>
  To find the target, the binary search algorithm implemented to determine the middle index at the array. 
  After that, the algorithm will check the condition of the value based on the binary search formula.
</p>

## Pseudocode
The pseudocode of the binary search algorithm:
- Set the total element of number in the sorted array as $n$, and the target as $T$
- Set the $L = 0$, and $R = n - 1$
- Set the loop condition as $L <= R$
- Inside the loop, calculate the middle part, $m$, using formula of $m = L + (floor( R - L ) / 2)$
- If $array[m] < T$: set the $L = m+1$
- If $array[m] > T$: set the $R=m-1$
- Else, return the $m$
- The code will return the index of the target number if the target found inside the sorted array.

## References
1. https://en.wikipedia.org/wiki/Binary_search
