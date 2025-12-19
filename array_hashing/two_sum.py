#1 | Two Sum --- Dec 18th 2025 ---

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        inv = {}
        
        for i in range(len(nums)):
            if target - nums[i] in inv:
                return [i,inv[target-nums[i]]]
            else:
                inv[nums[i]] = i
        return []

test_cases = [
    ([2, 7, 11, 15], 9),        # [0, 1]
    ([3, 2, 4], 6),             # [1, 2]
    ([3, 3], 6),                # [0, 1]
    ([1, 5, 3, 7], 8),           # [0, 3]
    ([0, 4, 3, 0], 0),           # [0, 3]
    ([-1, -2, -3, -4, -5], -8),  # [2, 4]
    ([10, 20, 30, 40], 50),      # [0, 3]
    ([5, 75, 25], 100),          # [1, 2]
    ([1, 2], 4),                 # [] (no solution)
    ([1000000, 500000, 500000], 1500000)  # [1, 2]
]

for nums, target in test_cases:
    print(nums, target, "→", twoSum(nums, target))