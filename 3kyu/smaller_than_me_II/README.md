# [**How many are smaller than me II?**](https://www.codewars.com/kata/56a1c63f3bc6827e13000006/python)

This is a hard version of [How many are smaller than me?](https://www.codewars.com/kata/56a1c074f87bc2201200002e). If you have troubles solving this one, have a look at the easier kata first.

Write

```
function smaller(arr)
```

that given an array ```arr```, you have to return the amount of numbers that are smaller than ```arr[i]``` to the right.

For example:

```
smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]
```

## Note
Your solution will be tested against inputs with up to 120_000 elements