#!/bin/python3

from abc import abstractproperty
import math
import os
import random
import re
import sys

#
# Need to calculate a value without use the operator *
#

def findSmaller(arr):
    smallest = arr[0]
    smallest_index = 0 
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmaller(arr)
        newArr.append(arr.pop(smallest))
        return newArr

def Partition(list, k):

    lessThanK = []
    moreThanK = []
    equalToK  = []

    for i,item in enumerate(list):
        if item< k:
            lessThanK.append(list[i])
        elif item > k: 
            moreThanK.append(list[i])
        else:
            equalToK.append(list[i])

    print (lessThanK)
    print(moreThanK)
    print(equalToK)

if __name__ == '__main__':

    print(selectionSort([5,6,8,1,2,6,10,7,12]))
    # Partition([1,2,3,5,7,8,2,3,4],5)