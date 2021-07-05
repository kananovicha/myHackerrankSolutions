#! /usr/bin/env/ python3

"""""
https://www.hackerrank.com/challenges/python-loops/

Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
"""""

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n): #classic looping in python
        print(i**2)  #python uses ** operator to raise a number to a power