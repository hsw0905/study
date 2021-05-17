def solution(s: str) -> int:
    length = len(s)
    if length < 2:
        return length
    hash_map = {}

    left = -1
    longest = 1

    for right in range(length):
        if s[right] in hash_map:
            left = max(hash_map[s[right]], left)
        hash_map[s[right]] = right
        longest = max(right-left, longest)
    return longest


def test_solution():
    assert solution(s='abcabcbb') == 3
    assert solution(s='bbbbb') == 1
    assert solution(s='') == 0
    assert solution(s='pwwkew') == 3
