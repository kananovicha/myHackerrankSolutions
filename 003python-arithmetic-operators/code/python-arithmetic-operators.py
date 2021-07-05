#! /usr/bin/env python3

"""""
Hackerrank problem 
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?h_r=next-challenge&h_v=zen

Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

"""""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b) #print the sum of the numbers
    print(a - b) #print the difference of the two numbers
    print(a * b) #print the product of the two numbers