# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    b_occurs = False
    for c in S:
        if c == 'b':
            b_occurs = True
        if (c == 'a' and b_occurs):
            return False
    return True
