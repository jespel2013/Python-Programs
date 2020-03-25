'''
Name: Jesse Pelletier
Description: This program uses a linked list data structure to find friends in common in a social network.
File Name: friends.py
'''
from linked_list import *
import sys 

class Name:
    def __init__(self, name):
        self._name = name
        self._next = None
        self._friends = LinkedList()
    def getName(self):
        return self._name
    def getFriends(self):
        return self._friends
    def getNext(self):
        return self._next
    def setNext(self, newName):
        self._next = newName
    #adds friend to friends list
    def addFriend(self, newFriend):
        self._friends.add(newFriend)
    #searches the list to see if the a specific name is in the list.  Returns true if it is, false otherwise.
    def searchFriends(self, name): 
        currNode = self._friends.getHead()
        while currNode != None:
            if currNode.getName() == name:
                return True
            currNode = currNode.getNext()
        return False
    def __str__(self):
        return self._name

#This function reads a file of names and organizes it in a linked list
def processFile(fileName):
    mainList = LinkedList()
    try:
        inFile = open(fileName)
    except:
        print("ERROR: Could not open file " + fileName)
        sys.exit(0)

    for line in inFile:
        line = line.strip()
        line = line.split()
        tempName1 = Name(line[0])
        tempName2 = Name(line[1])
        #add to main linked list
        if not mainList.find(tempName1.getName()):
            mainList.add(tempName1)
        if not mainList.find(tempName2.getName()):
            mainList.add(tempName2)

        #add to linked list of friends names.  Each line requires that the first name is added to the second names' friends list, and vice versa.
        currNode = mainList.getHead()
        while currNode != None:
            if currNode.getName() == tempName1.getName():
                currNode2 = currNode.getFriends()
                currNode2.add(Name(line[1]))
            if currNode.getName() == tempName2.getName():
                currNode2 = currNode.getFriends()
                currNode2.add(Name(line[0]))
            currNode = currNode.getNext()

        

        
    return mainList
#This function finds and prints any mutual friends
def findMutualFriends(mainList, name1, name2):
    
    currNode1 = mainList.getHead()
    currNode2 = mainList.getHead()

    #This section finds each name in the main list and gets the friends list for each
    while currNode1 != None:
        if currNode1.getName() == name1:
            friendsList1 = currNode1.getFriends()
            while currNode2 != None:
                if currNode2.getName() == name2:
                    friendsList2 = currNode2.getFriends()
                currNode2 = currNode2.getNext()
        currNode1 = currNode1.getNext()

    #friendsList 1 and 2 haven't been initialized if the names didn't exist, so this is where I handled the errors.  
    try:
        nodeF1 = friendsList1.getHead()
    except:
        print("ERROR: Unknown person " + name1)
        sys.exit(0)
    try:
        nodeF2 = friendsList2.getHead()
    except:
        print("ERROR: Unknown person " + name2)
        sys.exit(0)
    #to indicate if at least 1 mutual friend is found
    friendFound = 0

    #this section of code prints any friends in common
    while nodeF1 != None:
        nodeF2 = friendsList2.getHead()
        while nodeF2 != None:
            if nodeF1.getName() == nodeF2.getName():
                if friendFound == 0:
                    print("Friends in common:")
                    print(str(nodeF1))
                    friendFound+=1
                else:
                    print( str(nodeF1))
            nodeF2 = nodeF2.getNext()
        nodeF1 = nodeF1.getNext()
    return 0
    
#The main function takes all user input and calls the other functions, which do the heavy lifting.
def main():

    fileName = input("Input file: ")
    mainList = processFile(fileName)

    name1 = input("Name 1: ")
    name2 = input("Name 2: ")
    name1 = name1.strip()
    name2 = name2.strip()

    #print friends troubleshoot
    
        
        

    findMutualFriends(mainList, name1, name2)
    return 0
    
    


main()
