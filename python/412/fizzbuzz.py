#!/usr/bin/env python

class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret_list = []
        for i in xrange(1,n+1):
            val = ''
            if not i%3:
                val += 'Fizz'
            if not i%5:
                val += 'Buzz'
            if not val:
                val = str(i)
            ret_list.append(val)

	    return ret_list
