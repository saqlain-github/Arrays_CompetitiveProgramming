#method o(n) o(n)
from regex import F
from sympy import N


def zeroSumSubArray(numbers):
    numbers_set = set()
    n = len(numbers)
    prefix_sum_array = [0]*n
    #computing prefix array
    for i in range(n):
        if i == 0:
            prefix_sum_array[i] = numbers[i]
        else : 
            prefix_sum_array[i] = prefix_sum_array[i-1]+numbers[i]
    print(prefix_sum_array)      
    #number set array
    for i in range(n):
        if prefix_sum_array[i] in numbers_set:
            return True
        numbers_set.add(prefix_sum_array[i])
    #edge case
    if 0 in numbers_set:
        return True
    return False

print(zeroSumSubArray([4,2,-3,1,10]))