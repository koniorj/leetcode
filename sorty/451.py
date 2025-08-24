# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

def frequencySort(s):
    from collections import defaultdict
    n = len(s)

    cnt_char = {}
    for char in s:
        cnt_char[char] = cnt_char.get(char, 0) + 1

    # idx to frequency, value to lista znakow
    buckets = defaultdict(list)
    for freq, char in cnt_char.items():
        buckets[char].append(freq)

    result = []
    for freq in range(n, 0, -1): 
        for char in buckets[freq]:
            result.append(char * freq)
    
    return ''.join(result)

s = "ccccaaa"
# print(frequencySort(s))

def topKFrequent(words, k):
    cnt_words = {}
    for word in words:
        cnt_words[word] = cnt_words.get(word, 0) + 1

    sorted_words = sorted(cnt_words.items(), key=lambda x: (-x[1], x[0]))

    res = []
    for i in range(k):
        res.append(sorted_words[i][0])

    return res

words = ["i","love","leetcode","i","love","coding"]
k = 2
print(topKFrequent(words,k))