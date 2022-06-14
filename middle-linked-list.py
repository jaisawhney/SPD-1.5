# https://leetcode.com/problems/middle-of-the-linked-list/

class Solution(object):
    def middleNode(self, head):
        linked_list = []
        while head:
            linked_list.append(head)
            head = head.next

        return linked_list[len(linked_list) // 2]
