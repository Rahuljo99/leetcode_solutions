#49 | Group Anagrams --- Dec 18th 2025 ---
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        result = {}
        #strs
        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord("a")] += 1
            count = tuple(count)
            if count in result:
                result[count].append(i)
            else:
                result[count] = [i]
        return list(result.values())

test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    [""],
    ["a"],
    ["ab", "ba", "abc", "cab", "bca"],
    ["listen", "silent", "enlist", "google", "gooegl"],
    ["rat", "tar", "art", "car"],
    ["aaa", "aaa", "aa"],
    ["dog", "cat", "god", "tac"],
    ["abc", "def", "ghi"],
    ["aabb", "bbaa", "abab", "baba"]
]

for strs in test_cases:
    print(strs, "→", groupAnagrams(strs))