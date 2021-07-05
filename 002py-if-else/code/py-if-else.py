#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    reminder = n % 2
    if reminder != 0:
        print("Weird")
    elif reminder ==0 and n <= 5 and n>=2:
        print("Not Weird")
    elif reminder ==0 and n<= 20 and n >=6:
        print("Weird")
    elif reminder == 0 and n > 20:
        print("Not Weird")