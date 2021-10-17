// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        
        long int start=1;
        long int end=n;
        long int mid;
        
        while(start<=end )
        {
            mid = (start + end )/2;
            
            // if mid and m-1 is good then mid is first bad value
            if(isBadVersion(mid) && !isBadVersion(mid-1))
            {
                return mid;
            }
            
            // if mid and mid-1 both are bad then all values after mid are also bad 
            else if(isBadVersion(mid) && isBadVersion(mid-1))
            {
                end = mid -1;
                
            }
            
            // if both mid and mid-1 are not bad, it means bad ver starts after mid
            else
            {
                start = mid +1;
            }
            
        
        }
        
                            
        return mid;
    }
};