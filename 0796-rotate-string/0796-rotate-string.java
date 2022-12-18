class Solution {
    public boolean rotateString(String s, String goal) {
        // check the lengths of the strings
        if (s.length() != goal.length()) {
            return false;
        }
        
//         int size = goal.length();
        
//         // change the strings to character arrays
//         char[] sArray = s.toCharArray();
//         char[] goalArray = goal.toCharArray();
    
        
//         // find the offset
//         int offset = 0;
//         for (;offset < size; offset++) {
//             if (goalArray[offset] == sArray[0]) {
//                 break;
//             }
//         }
        
        
//         // check the string is correctly offsetted
//         for (int i = 0; i < size; i++) {
//             if (sArray[i] != goalArray[(i+offset)%size]) {
//                 return false;
//             }
//         }
        
//         // else return true
//         return true;
        return (s+s).contains(goal);
        
        
    }
}