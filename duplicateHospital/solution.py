# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Create a hashmap of the doctors as keys and number of hospitals they work as values
    count = {}
    sum = 0
    for i in range(len(A)):
        for doctor in list(set(A[i])):
            count[doctor] = count.get(doctor, 0) + 1
    # return keys greater than 1
    for value in count.values():
        if value > 1:
            sum += 1
    return sum
