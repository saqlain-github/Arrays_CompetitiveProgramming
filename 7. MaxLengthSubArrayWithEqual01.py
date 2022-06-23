# optimal solution
# 0(n) o(n)
def maxLengthSubArraywith0and1(numbers):
    n = len(numbers)
    prefix_numbers = [0]*n
    for i in range(n):
        if numbers[i] == 0:
            numbers[i] = -1
            
    for i in range(n):
        if numbers[i]  == 0:
            prefix_numbers[i] = numbers[i]
        else: 
            prefix_numbers[i] = prefix_numbers[i-1] + numbers[i]
            
    hashmap = {}
    max_length = 0
    for i in range(n):
        #edge case
        if prefix_numbers[i] == 0:
            max_length = max(max_length,i+1)
        #normal considersation
        if prefix_numbers[i] in hashmap:
            max_length  = max(max_length, i-hashmap[prefix_numbers[i]])
        if prefix_numbers[i] not in hashmap:
            hashmap[prefix_numbers[i]] = i
        
        #print(max_length)
            
    return max_length

print(maxLengthSubArraywith0and1([0,0,1,0,1,0,0]))