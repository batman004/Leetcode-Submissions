class Solution {
    public int[] replaceElements(int[] arr) {
        int max = 0;
        int[] result = new int[arr.length];
        for(int i=arr.length-1;i>=0;i--)
        {
            result[i]=max;
            if(max<arr[i])
            {
                max = arr[i];
            }
        }
        
        result[arr.length-1] = -1;
        
        return result;
    }
}