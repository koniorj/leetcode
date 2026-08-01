// Write a function that reverses a string. The input string is given as an
// array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory.

#include <vector>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        size_t length = s.size();
        char* l = &s[0];
        char* r = &s[length-1];

        while (l < r) {
            char temp = *l;
            *l = *r;
            *r = temp;
            ++l;
            --r;
        }
    }
};