from typing import List


def solution(nums: List[int], target: int) -> List[int]:
    answer = {}
    for i, num in enumerate(nums):
        if target - num in answer:
            return [answer[target-num], i]
        answer[num] = i

    return answer


def test_solution():
    assert solution(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert solution(nums=[3, 2, 4], target=6) == [1, 2]
    assert solution(nums=[3, 3], target=6) == [0, 1]
