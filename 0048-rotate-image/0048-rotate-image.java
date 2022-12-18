class Solution {
    public void rotate(int[][] matrix) {
        int size =  matrix.length;
        // we want to go through each layer of the matrix from out to in, the layer number is the offset
        for (int layer = 0; layer < size/2 ; layer++) {
            int start = layer; 
            int end = size - 1 - layer;
            
            for (int i = start; i < end; i++) {
                int offset = i - start;
                // temp = top 
                int temp = matrix[start][i];
                
                // top = left
                matrix[start][i] = matrix[end-offset][start];
                
                // left = bottom
                matrix[end-offset][start] = matrix[end][end-offset];
                
                // bottom = right 
                matrix[end][end-offset] = matrix[i][end];
                    
                // right = temp
                matrix[i][end] = temp;
            }
        }
    }
}
    