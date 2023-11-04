class Task_7:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    import heapq

    min_heap = []
    for l in lists:
        if l:
            heapq.heappush(min_heap, (l.val, l))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, node.next))

    return dummy.next

list1 = Task_7(1, Task_7(4, Task_7(5)))
list2 = Task_7(1, Task_7(3, Task_7(4)))
list3 = Task_7(2, Task_7(6))

result = merge_k_sorted_lists([list1, list2, list3])
while result:
    print(result.val, end=" ")
    result = result.next
print()
