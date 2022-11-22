class Solution {
    public boolean containsDuplicate(int[] nums) {
        // create a new hashset 
        HashSet<Integer> seen = new HashSet<>();
        
        // go through the array
        for (Integer i : nums) {
            if(!seen.contains(i)) {
                seen.add(i);
            }
            else {
                return true;
            }
        }
        return false;
        
        
    }
}