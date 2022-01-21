class Solution {
    
    public int findSquare(int n) {
        int res = 0;
        // extract digits
        
        while(n>0) {
            int r = n % 10;
            res = res + r*r;
            n = n/10;
        }
        
        return res;
    }
    
    
    public boolean isHappy(int n) {
        
        int fast, slow;
        fast = n;
        slow = n;
        
        do {
            slow = findSquare(slow);
            fast = findSquare(findSquare(fast));
            
        }while(fast !=slow);
        
        if(slow ==1) {
            return true;
        }
        
        return false;
        
    }
}