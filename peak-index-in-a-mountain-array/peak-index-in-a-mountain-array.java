class Solution {
    public int peakIndexInMountainArray(int[] arr) {

        // basically find inflection point. High -> low (max number in array)
        // ex arr = [0,2,1,0]  peak = 2.  0 -> 2 increasing ; 2 - > 0 decreasing
        // brute force : finding max element ; o(n)
        // apply binary search and then compare mid and mid + 1 ; if arr[mid] > arr[mid + 1]
        // you are in decreasing part and vice versa

        int start = 0;
        int end = arr.length - 1;
        
        while(start < end) {
            
            int mid = start + (end - start) /2 ;
            
            if(arr[mid] > arr[mid +1]){
                end = mid;
            }
            
            else {
                
                start = mid + 1;
            }
        }
        
        return start;

    }
}