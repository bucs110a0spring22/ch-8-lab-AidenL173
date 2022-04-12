# CS 110
## Lab 8 - Creating a String Library

### [Assignment Description](https://docs.google.com/document/d/1y_jvdf4tiNYyqNEkz-w9HXeigK8qQ45d-E4J1fvDBXk/edit?usp=sharing)

***

Replace anything surrounded by the `< >` symbols._

## SUMMARY:
Created a string utility class. Init takes a string as a parameter and stores it as an instance variable. Str returns the internal string itself, unchanged. Vowel(self) returns the amount of vowels in a string unless it's over 5, in which it will return "many" instead. BothEnds(self) return a string made of the first 2 and last 2 chars of the original string, However, if the string length is less than or equal to 2, it returns an empty string. FixStart(self) returns a string where all occurrences of its first char have been changed to '*', except the first char itself, however, if the parameter is length 1 or less, it returns the parameter as is. AsciiSum(self) returns an integer that is the sum of all ascii values in the string. Cipher(self) returns an encoded string by incrementing all letters by the length of the string. It accounts for wrap arounds.

## GRACE DAYS
Grace days used for this assignment: 0

Grace days remaining: 5/5

## KNOWN BUGS AND INCOMPLETE PARTS:
N/A

## REFERENCES:
https://book.pythontips.com/en/latest/ternary_operators.html
https://realpython.com/list-comprehension-python/
https://runestone.academy/ns/books/published/thinkcspy/Strings/toctree.html

## MISCELLANEOUS COMMENTS:
N/A