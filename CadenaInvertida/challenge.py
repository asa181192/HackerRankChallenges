#!/bin/python3

import math
import os
import random
import re
import sys

def reverseString(s):

    newArray = []
    i = 0
    while i < len(s):
        newArray.append(s[ (len(s) - 1) - i ])
        i += 1
    
    return newArray
        # LUIS SIUL


if __name__ == '__main__':

    result = reverseString("ASA")
    print (''.join(result))
