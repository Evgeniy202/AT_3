class Task_4:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head:
        return

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second_half = prev

    current = head
    while second_half:
        next_node = current.next
        current.next = second_half
        second_half = second_half.next
        current.next.next = next_node
        current = next_node

list1 = Task_4(1, Task_4(2, Task_4(3, Task_4(4))))
reorder_list(list1)
result1 = list1
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()

list2 = Task_4(1, Task_4(2, Task_4(3, Task_4(4, Task_4(5))))
reorder_list(list2)
result2 = list2
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()
