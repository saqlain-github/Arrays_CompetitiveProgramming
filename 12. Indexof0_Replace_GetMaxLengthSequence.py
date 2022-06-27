#O(n) O(1)
def replaceZeroToGetMaxOnesArray(A):
    current_count = 0
    max_count = 0
    prev_zero_idx = -1
    answer_idx = -1
     
    for i in range(len(A)):
        if A[i] == 1:
            current_count +=1 
        else: #A[i] = 0  
            current_count = i - prev_zero_idx
            prev_zero_idx = i
        if current_count > max_count:
            max_count = current_count
            answer_idx = prev_zero_idx
            
    return max_count, answer_idx
     
print(replaceZeroToGetMaxOnesArray([0,1,0,1,0,1,1,1]))