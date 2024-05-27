# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:

    def is_palindrome(x) -> bool:

        #O(n) complexity - runtime 64ms, memory 16.46 mb
        # y = str(x)

        # reversed = []
        
        # for i, index in enumerate(y):
        #     reversed.append(y[len(y) -1 -i])

        # rev_y = "".join(reversed)   

        # return y == rev_y

        # O(n) complexity improved - runtime 56ms, memory 16.46 mb
        # y = str(x) 

        # return y == y[::-1]

        # O(n) complexity even more runtime improved - runtime 46ms, memory 16.46 mb
        return str(x) == str(x)[::-1]
    


sol = Solution

print(sol.is_palindrome(10))