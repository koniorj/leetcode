// Given the root of a binary tree, return the sum of all left leaves.
//
// A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.


#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr) return 0;
        int sum = 0;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty())
        {
            TreeNode* curr = q.front();
            q.pop();

            if (curr->left != nullptr) {
                if ( curr->left->left == nullptr && curr->left->right == nullptr )
                {
                    sum += curr->left->val;
                } else
                {
                    q.push(curr->left);
                }
            }
            if (curr->right != nullptr) {
                q.push(curr->right);
            }
        }
        return sum;
    }
};