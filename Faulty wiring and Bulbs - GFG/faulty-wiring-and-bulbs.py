#User function Template for python3

class Solution:
    def countFlips(self,a,n):
        #code here
        
        count = 0
        for i in range(n):

            if (a[i] == 1 and count % 2 == 0):
                continue
  
            elif(a[i] == 0 and count % 2 != 0):
                continue
     

            elif (a[i] == 1 and count % 2 != 0):
                count += 1
     

            elif (a[i] == 0 and count % 2 == 0):
                count += 1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.countFlips(a,n))
# } Driver Code Ends