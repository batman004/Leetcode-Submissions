class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] answer = new int[nums1.length];
        Arrays.fill(answer, -1);
        
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i=0;i<nums2.length;i++)
            map.put(nums2[i],i);
        
        for(int i=0;i<nums1.length;i++)
        {

            int number = nums1[i];

            int j = map.get(number) + 1; 
            
            while(j<nums2.length){
                
                //if i find higher element than number
                if(nums2[j]>number)
                {
                    answer[i]=nums2[j];
                    break;
                }
                
                j++;
            }
        }
        
        return answer;
    }
}