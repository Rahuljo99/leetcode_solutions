#242 | Valid Anagram --- Dec 18th 2025 ---

from collections import Counter
def isAnagram(s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False 
test_cases = [
    ("anagram", "nagaram"),     # True – classic anagram
    ("rat", "car"),             # False – different letters
    ("listen", "silent"),       # True
    ("aacc", "ccac"),           # False – frequency mismatch
    ("", ""),                   # True – both empty
    ("a", "a"),                 # True – single character
    ("a", "b"),                 # False
    ("Dormitory", "Dirtyroom"), # False – case-sensitive
    ("abc", "abcc"),            # False – different lengths
    ("123", "321")              # True – numbers as characters
]
for s, t in test_cases:
    print(f"{s}, {t} → {isAnagram(s, t)}")