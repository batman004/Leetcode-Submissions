class Solution {
    
    public int search(int[] nums, int target) {

        
        return bsearch(nums, target, 0, nums.length-1);
        
    }
    
    // recursive binary search
    public int bsearch(int[] nums, int target, int low, int high) {
        
        if(nums == null || low > high)
        {
            return -1;
        }
        
       
        int mid = low + (high - low)/2 ;
        
        if(target > nums[mid])
            return(bsearch(nums, target, mid+1, high));
        else if(target < nums[mid])
            return(bsearch(nums, target, low, mid-1));
        else
            return(mid);
        
    }
}