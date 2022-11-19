class Solution {
    public String toLowerCase(String s) {
        // change the string to an array 
        char[] sArray = s.toCharArray();

        // iterate through the array and if the character is lowercase make it uppercase 
        for(int i = 0; i < s.length(); i++) {
            if (Character.isUpperCase(sArray[i])) {
                sArray[i] = Character.toLowerCase(sArray[i]);
            }
        }

        String string = new String(sArray);
        return string;
    }
}