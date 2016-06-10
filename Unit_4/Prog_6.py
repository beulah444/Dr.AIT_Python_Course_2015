__author__ = 'Dr.S.Gowrishankar'

#Construct a Linked list with 3 nodes.
#Write Pythonic code to remove the second node.
#Return the reference to the removed node and print the value.

class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def print_list(node):
    while node:
        print node,
        node = node.next
    print

def link_nodes(node1):
    node1.next = node2
    node2.next = node3

def removeSecond(list):
    if list == None:
        return
    first = list
    second = list.next
    #make the first node refer to the third node
    first.next = second.next
    second.next = None
    return second


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

link_nodes(node1)

print_list(node1)

removed = removeSecond(node1)

print_list(removed)

print_list(node1)

