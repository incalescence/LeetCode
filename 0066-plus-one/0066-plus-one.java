class Solution {
    public int[] plusOne(int[] digits) {
        
        // go through the given array from the back 
        for (int i = digits.length-1; i >= 0; i--) {
            // if less than nine, add one to the number
            if (digits[i] < 9) {
                digits[i] += 1; 
                break;
            } else {
                // cases where we need to carry over one
                digits[i] = 0;
                if (i != 0) {
                    if (digits[i-1] != 9) {
                        digits[i-1] +=1;
                        break;
                    }
                } else {
                    int[] resize = new int[digits.length+1];
                    resize[0] = 1;
                    // copy through the old array 
                    for(int j = 0; j < digits.length; j++) {
                        resize[j+1] = digits[j];
                    }
                    return resize;
                }
            }       
        }   
        return digits;
    }
}