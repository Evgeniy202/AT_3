class Task_3:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

list1 = Task_3(3, Task_3(2, Task_3(0, Task_3(-4))))
list1.next.next.next.next = list1.next
print(has_cycle(list1))  

list2 = Task_3(1, Task_3(2))
list2.next.next = list2 
print(has_cycle(list2)) 

list3 = Task_3(1)
print(has_cycle(list3))
