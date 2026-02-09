from __future__ import annotations


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return (seen[needed], i)
        seen[num] = i
    raise ValueError("No solution")
