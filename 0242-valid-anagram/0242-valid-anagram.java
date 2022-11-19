class Solution {
    public boolean isAnagram(String s, String t) {
        // check the lengths 
        if (s.length() != t.length()) {
            return false;
        }
        
        // change s and t to 
        char[] sArray=s.toCharArray();
        char[] tArray=t.toCharArray();  

        // have an array of all the possible characters 
        int[] alphabetBuffer = new int[26];

        // go through the first string increment the character array
        for (char c : sArray) {
            alphabetBuffer[c-'a'] += 1;
        }

        // decrease going through the second string
        for (char c : tArray) {
            alphabetBuffer[c-'a'] -= 1;
            if (alphabetBuffer[c-'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}