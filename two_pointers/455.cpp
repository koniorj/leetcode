// Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
//
// Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int content_children = 0;
        int i = g.size() - 1;
        int j = s.size() - 1;
        while (i >= 0 && j >= 0) {
            if (g[i] <= s[j]) {
                ++content_children;
                --i;
                --j;
            } else {
                --i;
            }
        }
        return content_children;
    }
};

class Solution2 {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int curr_child = 0;
        for (int curr_cookie : s) {
            if (curr_child == g.size()) break;
            if (curr_cookie >= g[curr_child]) {
                ++curr_child;
            }
        }
        return curr_child;
    }
};