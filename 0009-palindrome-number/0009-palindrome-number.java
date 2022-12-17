class Solution {
    public boolean isPalindrome(int x) {
        char[] xArray = ("" + x).toCharArray();
        int size = xArray.length;
        for(int i = 0; i < size/2; i++) {
            if (xArray[i] != xArray[size - i - 1]) {
                return false;
            }
            
        }
        return true;
    }
}