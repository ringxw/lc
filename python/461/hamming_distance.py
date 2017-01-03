#!/usr/bin/env python
class Solution(object):

    def hammingDistance(self, x, y):
        """

        :type x: int

        :type y: int

        :rtype: int

        """
        # Convert the int to binary in string format, then compare them bit by bit
        binary_x = bin(x)[2:].zfill(32) 
        binary_y = bin(y)[2:].zfill(32)
        print binary_x
        print binary_y
        
        return sum( bit_in_x != bit_in_y for bit_in_x, bit_in_y in zip(binary_x, binary_y))

solution = Solution()
print solution.hammingDistance(2121212121,5)

