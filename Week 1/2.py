# Find largest element in array 
class Solution:
    def largest(self, arr):
        return max(arr)

if __name__ == "__main__":
    # Taking array input from user
    arr_input = input("Enter the array elements separated by spaces: ")
    arr = list(map(int, arr_input.strip().split()))

    # Creating object and calling function
    solution = Solution()
    largest_element = solution.largest(arr)

    # Printing the result
    print("Largest element:", largest_element)
