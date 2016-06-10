__author__ = 'Dr.S.Gowrishankar'

#Program that takes input from user to create the nodes dynamically based on user requirement

class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

def print_list(node):
    i = 0
    while i < len(node):
        print node[i],
        node[i] = node[i].next
        i+=1
    print


def link_nodes(node):
    i = 0
    while (i < len(node)):
        #we will be connecting a node to the next node until last but one
        if i < len(node)- 1:
            node[i].next = node[i+1]
        else:
            node[i].next = None #the last node is made to point to None
        i += 1

#First Create a Dictionary
#This is used to hold all the node objects that are created dynamically
node = {}
number_Of_Nodes = int(raw_input('Enter the number of nodes to be creates'))
i=0
while (i < number_Of_Nodes):
    node_Val = int(raw_input('Enter the value for the node'))
    print
    node[i] = Node(node_Val)#here we are dynamically creating objects are using dictionary to store it
    i+=1

#Call the function to link each node to the other node
#Here we are passing the dictionary containing the entire node
link_nodes(node)
#Once the links are established between the nodes then print the node values
print 'The list of nodes created are'
print_list(node)
