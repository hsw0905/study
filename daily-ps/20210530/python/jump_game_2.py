from typing import List


def solution(nums: List[int]) -> int:
    count_list = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(1, nums[i] + 1):
            if i + j >= len(nums):
                continue
            if count_list[i + j] == 0:
                count_list[i + j] = count_list[i] + 1
    return count_list[len(nums) - 1]


def test_jump_game_2_solution():
    assert solution([2, 3, 1, 1, 4]) == 2
    assert solution([2, 3, 0, 1, 4]) == 2
