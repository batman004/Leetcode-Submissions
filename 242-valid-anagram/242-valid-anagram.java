import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        
        if(s.length()!=t.length()) return false;

        s.toLowerCase();
        t.toLowerCase();

        char[] tArray = t.toCharArray();
        char[] sArray = s.toCharArray();


        Arrays.sort(tArray);
        Arrays.sort(sArray);

        boolean result = Arrays.equals(tArray, sArray);
        
        return result;
        
    }
}