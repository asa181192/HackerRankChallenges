#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):

    aux = 0
    result = 0
    distint = []
    cloneAr = ar.copy()

    for i, item in enumerate(ar):
        if(not (ar[i] in distint)):
            distint.append(ar[i])
            cloneAr.remove(ar[i])

    for i,item in enumerate(distint):
        for j,item in enumerate(cloneAr):
            if distint[i] == cloneAr[j] :
                aux = aux +1 
    
        if not (aux == 0) :
            aux = aux + 1



        if aux % 2 == 0 and aux != 0 :
            result = result + (aux / 2 )
        elif aux != 0 :
            result = result + (( aux - 1) / 2)
        
        aux = 0
    
    return result


if __name__ == "__main__":
    n = 15
    ar = [10, 10, 40, 40, 50, 30, 30, 40, 15, 18, 19, 30, 17,40,50,18]
    result = sockMerchant(n, ar)
    print(result)
