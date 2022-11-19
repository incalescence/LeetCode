originally, I wanted to create an array with size one more than the length of digits as an extra buffer just in case we needed to carry over on the first digit.
But this case is inefficient, because we would have to check for trailing zeroes in most of the cases.

So instead, i left resizing the array for the edge case

We will iterate through digits backwards from the end of the array 
- if the current digit is less than nine we will simply add one, break and return 
- if it is nine we will set the current digit to zero and attempt to carry over 
- if the one before is not nine we will add one to the one before and break and return
- other wise we will keep looping through until we hit the edge case 
- the edge case is when we have to resize the array 
- by 'resizing' i will create a new array one more than the size of the OG array and have the first digit as one. 
- so the first digit is one and the rest of the array is digits [1] [digits]
- return new array 
- or otherwise return digits
