#!/usr/bin/env python
class Solution(object):

    def hammingDistance(self, x, y):

        """

        :type x: int

        :type y: int

        :rtype: int

        """
        # {0} is the standard format method format, things after : is the formatting
        # 032 means zero-padd up to 32 digits to the left, b means convert to binary
        binary_x = '{0:032b}'.format(x)
        binary_y = '{0:032b}'.format(y)
        print binary_x
        print binary_y
        
        return sum(bit_in_x != bit_in_y for bit_in_x, bit_in_y in zip(binary_x, binary_y))

solution = Solution()
print solution.hammingDistance(2121212121,5)

