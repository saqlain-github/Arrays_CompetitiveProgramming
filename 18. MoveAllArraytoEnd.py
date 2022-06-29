def zerosToend(A):
    n = len(A)
    j = 0
    for i in range(n):
        if A[i] != 0:
            A[i], A[j] = A[j], A[i]
            j += 1

    return A

print(zerosToend([5,6,0,8,9,0,2,0,0,3,4]))