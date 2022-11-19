class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int num = 0; 
        for (String s : operations) {
            if (isAdd(s)) {
                num++;
            }
            if (isSubtract(s)) {
                num--;
            }
        }
        return num;
    }

    private boolean isAdd(String s) {
        return s.equals("X++") || s.equals("++X");
    }

    private boolean isSubtract(String s) {
        return s.equals("X--") || s.equals("--X");
    }
}