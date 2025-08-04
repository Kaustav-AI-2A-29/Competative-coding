#Insert an element at end of array
class Solution:
    def insertAtEnd(self, arr, val):
        arr.append(val)
        return arr

if __name__ == "__main__":
    # Taking array input from user
    arr_input = input("Enter the array elements separated by spaces: ")
    arr = list(map(int, arr_input.strip().split()))

    # Taking value to insert
    val = int(input("Enter the value to insert at the end: "))

    # Creating object and calling function
    solution = Solution()
    updated_arr = solution.insertAtEnd(arr, val)

    # Printing the result
    print("Updated array:", updated_arr)

