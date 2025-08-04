class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
    
    solution = Solution()
    result = solution.isSorted(arr)
    
    print("Is the array sorted in non-decreasing order?", result)
