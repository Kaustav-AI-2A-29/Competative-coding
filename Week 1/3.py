class Solution:
    def getSecondLargest(self, arr):
        largest = max(arr)
        second_largest = -1  # Start with -1, as required

        for a in arr:
            if a != largest:
                if second_largest == -1 or a > second_largest:
                    second_largest = a

        return second_largest

if __name__ == "__main__":
    # Taking array input from user
    arr_input = input("Enter the array elements separated by spaces: ")
    arr = list(map(int, arr_input.strip().split()))

    # Creating object and calling the function
    solution = Solution()
    result = solution.getSecondLargest(arr)

    # Printing result
    print("Second largest element:", result)
