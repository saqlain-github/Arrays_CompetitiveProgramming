def sortBinaryArray_BruteForce(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            count += 1
     
    for i in range(len(numbers)):
        if count > 0:
            numbers[i] = 0
            count -= 1
        else:
            numbers[i] = 1
    return numbers       
        
    
    
def sortBinaryArray_Constructive(numbers):
    start = 0
    idx = 0
    while idx < len(numbers):
        if numbers[idx] == 0:
            numbers[idx],numbers[start] = numbers[start],numbers[idx]
            start += 1
        idx += 1
    return numbers    
    
    
print(sortBinaryArray_BruteForce([1,0,1,1,0,1]))
print(sortBinaryArray_Constructive([1,0,1,1,0,1]))