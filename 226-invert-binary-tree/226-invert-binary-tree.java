/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public TreeNode invertTree(TreeNode root) {
        invertHelper(root);
        return root;
    }
    
    public TreeNode invertHelper(TreeNode node)
    {
        if(node == null)
            return null;

        if(node.left== null && node.right== null)
        {   
            return null;
        }
        
        TreeNode temp;
        temp = node.left;
        node.left = node.right;
        node.right = temp;
        invertHelper(node.left);
        invertHelper(node.right);
        return null;
        
    }
}