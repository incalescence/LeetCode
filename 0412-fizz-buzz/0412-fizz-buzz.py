class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return_array = [""]*n
        for i in range(n):
            if (i+1) % 3 == 0:
                if (i+1) % 5 == 0:
                    return_array[i] = "FizzBuzz"
                    continue
                else:
                    return_array[i] = "Fizz"
                    continue
            elif (i+1) % 5 == 0:
                return_array[i] = "Buzz"
            else:
                return_array[i] = str(i+1)
            
        return return_array
                
        