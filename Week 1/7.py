class Solution:
    def reverseString(self, s: str) -> str:
        return s[::-1]  # Pythonic way using slicing

if __name__ == "__main__":
    s = input("Enter a string: ")
    solution = Solution()
    print("Reversed string:", solution.reverseString(s))
