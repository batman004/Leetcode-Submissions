// { Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class gfg
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int n =sc.nextInt();
            int a[] = new int[n];
            
            int i = 0;
            for(i = 0; i < n; i++)
              a[i] = sc.nextInt();
              
            int[] s = new Solution().calculateSpan(a, n);
            
            for(i = 0; i < n; i++)
            {
                System.out.print(s[i] + " ");
            }
            
            System.out.println();
        }
    }
    
    
    
}// } Driver Code Ends



class Solution
{
    //Function to calculate the span of stockâ€™s price for all n days.
    public static int[] calculateSpan(int price[], int n)
    {

       int [] sol = new int[n];
    
        Stack <Integer> st = new Stack<>();
        
        st.push(0);
        
        sol[0] = 1;
        
        for(int i = 1; i<n; i++)
        {
         
            if(!st.isEmpty() && price[st.peek()] > price[i])
                sol[i] = i- st.peek();
                
            else if(!st.isEmpty() && price[st.peek()] <= price[i])
            {
                while(!st.isEmpty() && price[st.peek()] <= price[i])
                {
                    st.pop();
                }
                
                if(st.isEmpty())
                    sol[i] = i + 1;
                else
                    sol[i] = i - st.peek();
            }
            
            st.push(i);
    
        }
        
        
        return sol;
        
                
        
    }
    
}