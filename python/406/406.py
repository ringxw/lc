from operator import itemgetter
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret_list = []
        # (h, k)  h is height, k is number of ppl in front of you
        # sort twice, height descending then number of ppl ascending.
        # when inserting to new queue, k would just be where the item should be standing, since everything in queue is already taller or equal to the item. 
        people = sorted(sorted(people,key=itemgetter(1)), key=itemgetter(0), reverse=True)
        for item in people:
                ret_list.insert(item[1], item)
                
        return ret_list
