class Task_8:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_list(head, k):
        prev = None
        current = head
        while k > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            k -= 1
        return prev

    def count_nodes(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    total_nodes = count_nodes(head)
    dummy = Task_8(0)
    dummy.next = head
    prev_group_end = dummy

    while total_nodes >= k:
        group_start = prev_group_end.next
        group_end = group_start
        for _ in range(k - 1):
            group_end = group_end.next

        next_group_start = group_end.next
        group_end.next = None
        prev_group_end.next = reverse_list(group_start, k)
        group_start.next = next_group_start
        prev_group_end = group_start
        total_nodes -= k

    return dummy.next

head = Task_8(1, Task_8(2, Task_8(3, Task_8(4, Task_8(5))))
k = 2
result = reverse_k_group(head, k)
while result:
    print(result.val, end=" ")
    result = result.next
print()
