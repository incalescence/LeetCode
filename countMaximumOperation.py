from collections import Counter

def countMaximumOperation(s, t):
    s_dict = Counter(s)
    t_dict = Counter(t)

    count = -1
    while (all(value >= 0 for value in s_dict.values())):
        s_dict.subtract(t_dict)
        count += 1
    return count

s = input("what is s? ")
t = input("what is t? ")
print(countMaximumOperation(s, t))
