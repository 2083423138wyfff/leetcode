class Solution:
    def isPalindrome(self,s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
if __name__ == "__main__":
    import sys
    solution=Solution()
    input = sys.stdin.readline
    # 读一整行（保留空格，因为空格属于要跳过的符号）
    s = input().strip() 
    print(solution.isPalindrome(s))