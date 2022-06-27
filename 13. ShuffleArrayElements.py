from random import randrange

#O(n) O(1)
#fisher Yate
def shuffleArray(numbers):
    n = len(numbers)
    max_value = n
    for i in range(n):
        randon_idx = randrange(max_value)
        numbers[i], numbers[randon_idx] = numbers[randon_idx], numbers[i]
        max_value -= 1
    return numbers
    
print(shuffleArray([1,2,3,4,5]))