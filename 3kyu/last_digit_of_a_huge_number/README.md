# [**Last digit of a huge number**](https://www.codewars.com/kata/5518a860a73e708c0a000027/python)

For a given list ```[x1, x2, x3, ..., xn]``` compute the last (decimal) digit of ```x1 ^ (x2 ^ (x3 ^ (... ^ xn)))```.

E. g., with the input ```[3, 4, 2]```, your code should return ```1``` because 3<sup>(4<sup>2</sup>)</sup> = 3<sup>16</sup> = 43046721.

Beware: powers grow incredibly fast. For example, 9<sup>(9<sup>9</sup>)</sup> has more than 369 millions of digits. ```lastDigit``` has to deal with such numbers efficiently.

Corner cases: we assume that 0<sup>0</sup> = 1 and that ```lastDigit``` of an empty list equals to 1.

This kata generalizes [Last digit of a large number](https://www.codewars.com/kata/5511b2f550906349a70004e1); you may find useful to solve it beforehand.