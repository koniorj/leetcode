// Given two strings needle and haystack, return the index of the first
// occurrence of needle in haystack, or -1 if needle is not part of haystack.

#include <string>
#include <string_view>
using namespace std;

int strStr(const string& haystack, const string& needle) {
    const size_t needle_length = needle.size();
    const size_t haystack_length = haystack.size();

    if (haystack_length < needle_length)
    {
        return -1;
    }

    for (int i=0; i <= haystack_length - needle_length; ++i)
    {
        // using if (haystack.substr(i, needle_length) == needle) is less
        // efficient due to need of allocating new memory on heap,
        // string_view enables us to simply view the string. We don't
        // allocate any new memory, we don't copy anything.
        if (string_view(haystack).substr(i, needle_length) == needle)
        {
            return i;
        }
    }

    return -1;
}
