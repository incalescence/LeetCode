class Solution {
    public void setZeroes(int[][] matrix) {
        // initalise variables
        int m = matrix.length;
        int n = matrix[0].length;
        boolean firstRowHasZero = false;
        boolean firstColumnHasZero = false;
        
        // check the first column 
        for (int c = 0; c < m; c++) {
            if (matrix[c][0] == 0) {
                firstColumnHasZero = true;
                break;
            }
        }
        
        // check the first row
        for (int c = 0; c < n; c++) {
            if (matrix[0][c] == 0) {
                firstRowHasZero = true;
                break;
            }
        }
        
        // use the first row and the first coloumn to keep track of the zeroes in each row or column 
        for (int row = 1; row < m; row++) {
            for (int column = 1; column < n; column++) {
                if (matrix[row][column] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][column] = 0;
                }
            }
        }
        
        // nullify rows
        for (int i = 1; i < m; i++) {
            if (matrix[i][0] == 0) {
                for(int k = 1; k < n; k++) {
                    matrix[i][k] = 0;
                }
            } 
        }
        
        // nullify columns 
        for (int j = 1; j < n; j++) {
            if (matrix[0][j] == 0) {
                for(int k = 1; k < m; k++) {
                    matrix[k][j] = 0;
                }
            } 
        }
        
        // nullify the first row and column if need be 
        if (firstRowHasZero) {
            for (int i = 0; i < n; i++) {
                matrix[0][i] = 0;
            }
            
        }
        if (firstColumnHasZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}