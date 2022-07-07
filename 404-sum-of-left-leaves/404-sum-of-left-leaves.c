/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int sumOfLeftLeaves(struct TreeNode* root){
    if (root == NULL) {
        return 0;
    } else if (root->left != NULL && root->left->left == NULL && root->left->right == NULL) {
        return root->left->val + sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    } else {
        return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
}