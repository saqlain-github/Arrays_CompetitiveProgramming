#method 1 O(n), o(n)

from numpy import number
from sympy import re


def countPair(numbers, targetSum):
    set_numbers = set()
    n = len(numbers)
    count = 0
    for i in range(n):
        required_number = targetSum -  numbers[i]
        if required_number in set_numbers:
            count = count +1
        set_numbers.add(numbers[i])
            
    return count

print(countPair([1,5,-1,7,100],6))

# method two O(nlogn), o(1)
def countPair_optimium(numbers,targetSum):
    numbers.sort()
    n = len(numbers)
    l = 0
    r = n-1
    count = 0
    while(l<r):
        current_sum = numbers[l]+numbers[r]
        if current_sum == targetSum:
            count += 1
            l += 1
            r -= 1
        elif current_sum > targetSum:
            r = r-1
            
        else:
            l = l-1
            
    return count

print(countPair_optimium([1,6,-1,7,100],6))