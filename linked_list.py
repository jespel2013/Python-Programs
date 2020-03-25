'''
Name: Jesse Pelletier
Description: This file contains the class LinkedList that represents the data structure of the same name.  It
was taken from the practice problems for CSC 120.
FileName: linked_list.py
'''
class LinkedList:
    def __init__(self):
        self._head = None

    def getHead(self):
        return self._head
    
    # search the list for item and return True if found and False otherwise
    def find(self, item):
        currNode = self._head #make current node the first node in list
        while (currNode != None):
            if item == currNode.getName(): #if the nodes value is equal to the item True is returned
                return True
            currNode = currNode.getNext() #to avoid an infinite loop, iterate to the next node in linked list
        return False #returns false otherwise
    
    # add a node to the head of the list
    def add(self, node):
        if self._head == None:
            self._head = node
        else:
            node.setNext(self._head)
            self._head = node
    
    
    def __str__(self):
        string = 'List['
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node) + ' '
            curr_node = curr_node.getNext()
        string += ']'
        return string
