#347 | Top K Frequent Elements --- 18th Dec 2025 ---  
from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        for i,j in sorted(count.items(), key = lambda x: x[1],reverse = True)[:k]:
            result.append(i)
        return result

test_cases = [
    # nums, k
    ([1, 1, 1, 2, 2, 3], 2),          # Most common elements
    ([1], 1),                         # Single element
    ([1, 2], 2),                      # All elements
    ([4, 4, 4, 6, 6, 7], 1),           # One most frequent
    ([5, 5, 5, 5], 1),                 # All same
    ([1, 2, 3, 4], 2),                 # Same frequency
    ([-1, -1, -2, -2, -2], 2),         # Negative numbers
    ([100, 100, 100, 200, 200, 300], 2),
    ([1, 1, 2, 2, 3, 3], 3),            # k = number of uniques
    ([1, 1, 1, 2, 2, 3, 3, 3, 3], 2)     # Tie-breaking scenario
]

for nums, k in test_cases:
    print(nums, k, "→", topKFrequent(nums, k))