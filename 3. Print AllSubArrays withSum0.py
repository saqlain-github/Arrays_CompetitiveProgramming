def allzeroSumSubArrays(numbers):
    hashmap = {}
    n= len(numbers)
    prefix_sum_array = [0]*n
    for i in range(n):
        if i == 0:
            prefix_sum_array[i] = prefix_sum_array[i]
        else:
            prefix_sum_array[i] = prefix_sum_array[i-1] + numbers[i]
    #prefix sum arrayb has been computed
    
    for i in range(n):
        if prefix_sum_array[i] not in hashmap:
            hashmap[prefix_sum_array[i]] = [i]
        else:
            hashmap[prefix_sum_array[i]].append([i])
         
    answers = []
    for key,value in hashmap.items():
        if len(value) > 1 or key == 0:
            if key == 0:
                for val in value:
                    answers.append((0,val))
                for j in range(len(value)-1):
                    for k in range(j+1,len(value)):
                        answers.append((value[j]+1,value[k]))
                        
            else:
                for j in range(len(value)-1):
                    for k in range(j+1,len(value)):
                        answers.append(list([value[j]+1,value[k]]))
                        
    return answers

#TC - O(n*n)  SC - O(n)

print(allzeroSumSubArrays([4,-4,8,0,4,-4]))