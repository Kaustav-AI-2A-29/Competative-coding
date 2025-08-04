class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    ob = Solution()
    answer = ob.isPalindrome(s)
    print("Is Palindrome?", answer)
