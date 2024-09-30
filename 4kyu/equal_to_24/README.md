# [**T.T.T.#2: Equal to 24**](https://www.codewars.com/kata/574be65a974b95eaf40008da/python)

This is the simple version of [Fastest Code : Equal to 24](https://www.codewars.com/kata/574e890e296e412a0400149c).

## **Task**
A game I played when I was young: Draw 4 cards from playing cards, use ```+ - * / and ()``` to make the final results equal to 24.

You will coding in function ```equalTo24```. Function accept 4 parameters ```a b c d```(4 cards), value range is 1-13.

The result is a string such as ```"2*2*2*3"``` ,```(4+2)*(5-1)```; If it is not possible to calculate the 24, please return "It's not possible!"

All four cards are to be used, only use three or two cards are incorrect; Use a card twice or more is incorrect too.

You just need to return one correct solution, don't need to find out all the possibilities.

## **Examples**
```
equalTo24(1,2,3,4) // can return "(1+3)*(2+4)" or "1*2*3*4"
equalTo24(2,3,4,5) // can return "(5+3-2)*4" or "(3+4+5)*2"
equalTo24(3,4,5,6) // can return "(3-4+5)*6"
equalTo24(1,1,1,1) // should return "It's not possible!"
equalTo24(13,13,13,13) // should return "It's not possible!"
```