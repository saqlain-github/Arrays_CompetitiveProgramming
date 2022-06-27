# O(n+m) O(1)
def mergeTwoSortedArrays(A,B):
    # gather all elements of A at the start
    idx = 0
    n = len(A)
    for i in range(n):
        if A[i] != 0:
            A[idx] = A[i]
            idx += 1 
    # [2,3,5,6,0,0,0,0]
    # merge A and B using merge sort condition
    i = idx - 1
    j = len(B) - 1
    k = len(A) - 1
    while i >= 0 and j >= 0:
        if B[j] > A[i]:
            A[k] = B[j]
            j -= 1
            k -= 1
        else:
            A[k] = A[i]
            k -= 1
            i -= 1
    # check for left elements in array B
    while (j >= 0):
        A[k] = B[j]
        k -= 1
        j -= 1
    
    return A

 
print(mergeTwoSortedArrays([2,0,3,5,0,0,6,0,0],[1,7,8,15,17]))