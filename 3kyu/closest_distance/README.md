# [**Closest pair of points in linearithmic time**](https://www.codewars.com/kata/5376b901424ed4f8c20002b7/python)

Given a number of points on a plane, your task is to find two points with the smallest distance between them in linearithmic O(n log n) time.

## **Example**

```
  1  2  3  4  5  6  7  8  9
1  
2    . A
3                . D
4                   . F       
5             . C
6              
7                . E
8    . B
9                   . G
```

For the plane above, the input will be:

```
(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
=> closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
(both answers are valid. You can return a list of tuples too)
```

The two points that are closest to each other are D and F.
Expected answer should be an array with both points in any order.

## **Goal**
The goal is to come up with a function that can find two closest points for any arbitrary array of points, in a linearithmic time.

**Note**: Don't use ```math.hypot```, it's too slow...

---

More information on [wikipedia](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem).