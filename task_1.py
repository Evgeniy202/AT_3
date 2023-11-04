class Task_1:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(list1, list2):
    dummy = Task_1(-1)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2

    return dummy.next

list1 = Task_1(1, Task_1(2, Task_1(4)))
list2 = Task_1(1, Task_1(3, Task_1(4)))
result = merge(list1, list2)
while result:
    print(result.val, end=" ")
    result = result.next
print()

list1 = None
list2 = None
result = merge(list1, list2)
while result:
    print(result.val, end=" ")
    result = result.next
print()

list1 = None
list2 = Task_1(0)
result = merge(list1, list2)
while result:
    print(result.val, end=" ")
    result = result.next
print()
