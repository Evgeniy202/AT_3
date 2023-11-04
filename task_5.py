class Task_5:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next

list1 = Task_5(4, Task_5(5, Task_5(1, Task_5(9))))
node_to_delete1 = list1.next 
delete_node(node_to_delete1)
result1 = list1
while result1:
    print(result1.val, end=" ")
    result1 = result1.next
print()

list2 = Task_5(4, Task_5(5, Task_5(1, Task_5(9))))
node_to_delete2 = list2.next.next  
delete_node(node_to_delete2)
result2 = list2
while result2:
    print(result2.val, end=" ")
    result2 = result2.next
print()
