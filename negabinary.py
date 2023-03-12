# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def convert_to_binary(number):
    binary = []
    if number == 0:
        return binary

    while number != 0:
        number, remainder = divmod(number, -2)
        if remainder < 0:
            number += 1
            remainder -= -2
        binary.append(remainder)
    return binary

def convert_to_decimal(negabinary):
    if negabinary == "0":
        return 0
    totalsum = 0 
    for i, ch in enumerate(negabinary[::1]):
        totalsum += int(ch)*(-2)**i
    return totalsum
    

def solution(A):
    return convert_to_binary(math.ceil(convert_to_decimal(A)/2))
