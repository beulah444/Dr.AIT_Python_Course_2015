#list operations are expressed using recursive methods

class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def link_nodes(node1):
    node1.next = node2
    node2.next = node3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

link_nodes(node1)

def print_backward(list):
    if list == None:
        return
    head = list
    tail = list.next
    print_backward(tail)
    print head,

print_backward(node1)
