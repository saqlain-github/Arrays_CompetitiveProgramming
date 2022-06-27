#Counting O(n) O(1)
def sortArrayofZeroOneTwo_Counting(numbers):
    zeros, ones = 0,0
    for i in numbers:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
    for i in range(len(numbers)):
        if zeros:
            zeros -= 1
            numbers[i] = 0
        elif ones:
            ones -= 1
            numbers[i] = 1
        else:
            numbers[i] = 2
    return numbers  
            

#Counting O(n) O(1)
def sortArrayofZeroOneTwo_DutchFlagAlgo(numbers):
    start = 0
    current = 0
    end = len(numbers)-1
    while(current <= end):
        if numbers[current] == 0:
            numbers[current],numbers[start] = numbers[start],numbers[current] 
            current += 1
            start += 1
        elif numbers[current] == 2:
            numbers[current],numbers[end] = numbers[end],numbers[current]
            end -= 1
        else:
            current += 1
    return numbers  

print(sortArrayofZeroOneTwo_Counting([0,1,0,2,1,2]))
print(sortArrayofZeroOneTwo_DutchFlagAlgo([0,1,0,2,1,2]))