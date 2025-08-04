# User function Template for python3

class Solution:
    def rotate(self, arr):
        if len(arr) == 0:
            return  # no need to rotate if array is empty

        last = arr[-1]  # Save last element

        # Shift all elements one step to the right
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = last  # Place last element at the beginning
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

    solution = Solution()
    solution.rotate(arr)

    print("Array after rotating by one position:", arr)
