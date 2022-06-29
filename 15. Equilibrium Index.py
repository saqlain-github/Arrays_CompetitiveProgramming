#BruteForce O(n2) O(1)
def equilibrium_BruteForce(A):
    n = len(A)
    for idx in range(n):
        left_sum = 0
        right_sum = 0
        for j in range(idx):
            left_sum += A[j]
        for j in range(idx+1, n):
            right_sum += A[j]
        if right_sum == left_sum:
            return idx
        
    return -1
 
 
#Prefix O(n) O(1)
def equilibrium_Prefix(A):
    n = len(A)
    for i in range(1,n):
       A[i] = A[i] + A[i-1]
    
    for idx in range(n):
        #left hand sum
        right = idx -1
        if idx == 0:
            left_sum = 0
        else:
            left_sum = A[right]
        #right hand sum
        right = n -1
        left = idx + 1
        #edge case last index n-1 +1 out of bound
        if idx == n-1:
            right_sum = 0 
        else:
            right_sum = A[right] - A[left-1]
        #print(idx,left_sum,right_sum)
        if left_sum == right_sum:
            return idx
    return -1
       
print(equilibrium_BruteForce([-3,5,-4,-2,3,1,0,-1]))
print(equilibrium_Prefix([-3,5,-4,-2,3,1,0,-3]))