# optimal solution
# 0(n) o(n)
def maxLengthSubArray(numbers,target):
    n = len(numbers)
    prefix_numbers = [0]*n
    for i in range(n):
        if numbers[i]  == 0:
            prefix_numbers[i] = numbers[i]
        else: 
            prefix_numbers[i] = prefix_numbers[i-1] + numbers[i]
            
    hashmap = {}
    max_length = 0
    for i in range(n):
        #edge case
        if prefix_numbers[i] == target:
            max_length = max(max_length,i+1)
        #normal considersation
        if prefix_numbers[i] not in hashmap:
            hashmap[prefix_numbers[i]] = i
        if prefix_numbers[i] - target in hashmap:
            max_length  = max(max_length, i-hashmap[prefix_numbers[i] - target])
        #print(max_length)
            
    return max_length

print(maxLengthSubArray([5,6,-5,5,3,5,3,-2,0],8))