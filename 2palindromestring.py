class Solution:
    def isPalindrome(self, x: str) -> bool:

        left = 0
        right = len(x) - 1

        while left < right:

            if x[left].lower() != x[right].lower():
                return False

            left += 1
            right -= 1

        return True