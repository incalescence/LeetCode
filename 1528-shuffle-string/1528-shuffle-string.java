class Solution {
    public String restoreString(String s, int[] indices) {
        // convert the string to a char array
        char[] sArray = s.toCharArray();
        
        // have a new char buffer with the same size 
        char[] newString = new char[s.length()];
        
        // go through both the sarray and the indices and store the new string
        for (int i=0; i < s.length(); i++) {
            newString[indices[i]] = sArray[i];
        }
        
        // return new string
        return new String(newString);
        
    }
}