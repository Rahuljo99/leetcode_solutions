#217 | Contains Duplicate --- Dec 18th 2025 --- 

from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False

test_cases = [
    [1, 2, 3, 4, 5],            # No duplicates
    [1, 2, 3, 1],               # Duplicate at start/end
    [5, 5, 5, 5],               # All duplicates
    [],                         # Empty list
    [10],                       # Single element
    [-1, -2, -3, -1],           # Negative numbers duplicate
    [100, 200, 300, 400],       # Large numbers, no duplicates
    [0, 1, 2, 3, 0],             # Zero duplicate
    [1, 2, 3, 4, 3],             # Duplicate in middle
    [999999, 1, 2, 3, 999999]   # Large value duplicate
]

for nums in test_cases:
    print(nums, "→", containsDuplicate(nums))