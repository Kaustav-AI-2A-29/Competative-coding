class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        result = [0] * n  # Initialize result array with zeros

        # Count frequency of each number from 1 to n
        for num in arr:
            if 1 <= num <= n:
                result[num - 1] += 1

        return result
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
    solution = Solution()
    freq = solution.frequencyCount(arr)
    print("Frequency of numbers from 1 to n:", freq)
