/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */


public class Solution {
    
    public int lengthCycle(ListNode head) {
    
        ListNode fast;
        ListNode slow;
        fast = head;
        slow = head;
        
        while(fast !=null && fast.next !=null) {
            
            fast = fast.next.next;
            slow = slow.next;
            
            if(fast == slow) {
                // calculate length
                // keep fast const and rotate slow inside cycle till they meet again
                ListNode temp =slow;
                int length = 0;
                do {
                    temp = temp.next;
                    length++;
                }while(temp!=slow);
                return length;
            }
        }
                
    return 0;
    }
    
    public ListNode detectCycle(ListNode head) {
        
        
        ListNode fast;
        ListNode slow;
        int length = 0;
        fast = head;
        slow = head;
        
        while(fast !=null && fast.next !=null) {
            
            fast = fast.next.next;
            slow = slow.next;
            
            if(fast == slow) {
                length = lengthCycle(slow);
                break;
            }
        }
        
        if(length ==0) {
            return null;
        }
        
        // find start node of cycle
        ListNode first;
        ListNode sec;
        
        first = head;
        sec = head;
        
        while(length > 0 ) {
            sec= sec.next;
            length--;
        }
        
        
        while(first !=sec) {
            first = first.next;
            sec = sec.next;
        }
        
        return first;
    }
}