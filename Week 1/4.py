class Solution:
    def pushZerosToEnd(self, arr):
        count = 0  # Position for the next non-zero element

        # Move all non-zero elements to the front
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1

        # Fill remaining positions with 0
        while count < len(arr):
            arr[count] = 0
            count += 1
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
    
    solution = Solution()
    solution.pushZerosToEnd(arr)
    
    print("Array after pushing zeros to end:", arr)
