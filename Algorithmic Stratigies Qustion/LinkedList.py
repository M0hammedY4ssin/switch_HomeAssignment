class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

def make_linkedlist(nums, head=None):
    if head is None:
        head = LinkedList()

    for num in reversed(nums):
        node = Node(num,head.head) # insert to the beginning 
        head.head=node

    return head

make_linkedlist([2,3,4,5,6]).print_list()


        

