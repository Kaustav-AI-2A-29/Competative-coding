#!/bin/python3  # Environment shebang for Unix-based systems

import math
import os
import random
import re
import sys

# Function to reverse the array
def reverseArray(a):
    return a[::-1]  # List slicing to reverse the list

if __name__ == '__main__':
    arr_count = int(input().strip())  # Input: number of elements
    
    arr = list(map(int, input().rstrip().split()))  # Input: array elements as list of ints

    res = reverseArray(arr)  # Function call to reverse

    print(' '.join(map(str, res)))  # Output: space-separated reversed list
