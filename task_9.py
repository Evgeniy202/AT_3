class Task_10:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    less_head = Task_10(0)
    less_tail = less_head
    greater_head = Task_10(0)
    greater_tail = greater_head

    current = head

    while current:
        if current.val < x:
            less_tail.next = current
            less_tail = less_tail.next
        else:
            greater_tail.next = current
            greater_tail = greater_tail.next
        current = current.next

    less_tail.next = greater_head.next
    greater_tail.next = None

    return less_head.next

head = Task_10(1, Task_10(4, Task_10(3, Task_10(2, Task_10(5, Task_10(2))))))
x = 3
result = partition(head, x)
while result:
    print(result.val, end=" ")
    result = result.next
print()
