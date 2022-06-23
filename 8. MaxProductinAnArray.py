#O(n*n) O(1)
def maxProductinArray_BruteForce(numbers):
    max_product = float("-inf")
    n = len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            max_product = max(max_product,numbers[i]*numbers[j])
            
    return max_product
    

#O(n Logn) O(1)
def maxProductinArray_Sorting(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])

# O(n) O(1)
def maxProductinArray_4Values(numbers):
    max1, max2 = numbers[0], float("-inf")
    min1 ,min2 = numbers[0], float("inf")
    for i in range(1, len(numbers)):
        if numbers[i] > max1:
            max2 = max1
            max1 = numbers[i]
        elif numbers[i] > max2:
            max2 = numbers[i]
            
        if numbers[i] < min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2:
            min2 = numbers[i]
        
    return max(max1*max2,min1*min2)

print(maxProductinArray_BruteForce([-10,-3,5,6,-2]))
print(maxProductinArray_Sorting([-10,-3,5,6,-2]))
print(maxProductinArray_4Values([-10,-3,5,6,-2]))