#O(n) O(n)
from ast import Num


def duplicateElementinRangeArray_Set(numbers):
    numbers_set = set() 
    for i in range(len(numbers)):
        if numbers[i] in numbers_set:
            return (numbers[i],i)
        numbers_set.add(numbers[i])  
    

#O(n) O(1)
def duplicateElementinRangeArray_XOR(numbers):
    xor_out = numbers[0]
    for i in range(1,len(numbers)):
        xor_out = xor_out ^ numbers[i]
          
    for i in range(1,max(numbers)+1):
        xor_out ^= i
        
    return xor_out

print(duplicateElementinRangeArray_Set([1,2,3,2,4]))
print(duplicateElementinRangeArray_XOR([1,2,3,2,4]))

