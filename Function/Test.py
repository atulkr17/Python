from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert each number to a string
        numbers = list(map(str, nums))
        
        # Sort the strings based on the custom comparator
        numbers.sort(key=cmp_to_key(lambda a, b: (1 if a + b < b + a else -1)))

        # If the largest number is "0", return "0"
        if numbers[0] == "0":
            return "0"
        
        # Build the result from the sorted array
        return ''.join(numbers)

# Example Usage
solution = Solution()

# Test case 1
nums1 = [10, 2]
print(solution.largestNumber(nums1))  # Output: "210"

# Test case 2
nums2 = [3, 30, 34, 5, 9]
print(solution.largestNumber(nums2))  # Output: "9534330"
