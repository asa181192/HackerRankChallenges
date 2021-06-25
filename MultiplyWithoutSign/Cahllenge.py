#!/bin/python3

import math
import os
import random
import re
import sys

#
# Need to calculate a value without use the operator * 
#


def Multiply(a, b):
    i = 0
    result = 0
    
    while i < abs(b):

        result = result + a
        i += 1
    
    if b < 0 and a < 0:
        return abs (result)
    elif b < 0: 
        return - result   
    else:
        return result


if __name__ == '__main__':

    a = 2.5
    b = 2.5
    number = Multiply(a, b)
    print(number)
