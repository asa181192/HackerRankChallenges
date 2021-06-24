#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
   
    steps = 0 
    i = 0 
    while i < len(c) - 1:
        if i == len(c) - 2:
            if c[i + 1] == 0:
                steps += 1
                i += 1
            else:
                i += 1
        else:            
            if c[i+1] == 0 and c[i+2] == 0:
                steps += 1
                i = i + 2;
            elif c[i+1] == 0:
                steps += 1
                i = i + 1 ;
            else:
                steps += 1
                i += 2 
    return steps



if __name__ == '__main__':
  
  c = [0,0,0,1,0,0,1,0,0,0,1,0]

  print(jumpingOnClouds(c));
