class Task_6:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list(head):
    carry = 0
    current = head

    while current:
        current.val = current.val * 2 + carry
        carry = current.val // 10
        current.val = current.val % 10

        if not current.next and carry > 0:
            current.next = ListNode(carry)
            break

        current = current.next

    return head

list1 = Task_6(1, Task_6(8, Task_6(9)))
result1 = double_linked_list(list1)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()

list2 = Task_6(9, Task_6(9, Task_6(9)))
result2 = double_linked_list(list2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()
