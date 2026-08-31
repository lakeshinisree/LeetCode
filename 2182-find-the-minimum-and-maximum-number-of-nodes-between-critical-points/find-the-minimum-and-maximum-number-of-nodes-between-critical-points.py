# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1

        last = -1

        min_distance = float("inf")

        position = 1

        prev = head

        curr = head.next

        while curr is not None and curr.next is not None:
            is_critical = (
                (curr.val > prev.val and curr.val > curr.next.val)
                or
                (curr.val < prev.val and curr.val < curr.next.val)
            )

            if is_critical:
                if first == -1:
                    first = position
                else:
                    min_distance = min(min_distance, position - last)

                last = position

            prev = curr

            curr = curr.next

            position += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_distance = last - first

        return [min_distance, max_distance]