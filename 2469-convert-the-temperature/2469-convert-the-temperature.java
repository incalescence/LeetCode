class Solution {
    public double[] convertTemperature(double celsius) {
        double return_array[] = new double[2];
        return_array[0]=celsius+273.15;
        return_array[1]=celsius*1.80+32.00;
        return return_array;
    }
}