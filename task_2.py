class Task_2:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Приклади використання:
list1 = Task_2(1, Task_2(1, Task_2(2)))
result1 = delete_duplicates(list1)
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()

list2 = Task_2(1, Task_2(1, Task_2(2, Task_2(3, Task_2(3)))))
result2 = delete_duplicates(list2)
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()
