'''
Name: Jesse Pelletier
Description: This program builds a decoding tree and decodes a line of binary code.
FileName: huffman.py
'''
import sys
'''This class represents a tree that is used for decoding and it is called the decoding tree'''
class DecodingTree:  #adapted from practice problem
    def __init__(self): 
        self._value = None #a value
        self._left = None #a reference to another BinarySearchTree
        self._right = None #a reference to another BinarySearchTree
    #This method populates the tree that needs to be populated. 
    def populate(self, preO, inO):
        self._value = preO[0]

        if len(preO) <= 1:
            return
        try:
            rootIndex = inO.index(preO[0]) #split to left and right
            left = inO[0:rootIndex]
            right = inO[rootIndex+1:]
        except:
            return

        if left != []:
            self._left = DecodingTree()
            self._left.populate(preO[1:], left) #construct left
        if right!=[]:
            self._right = DecodingTree()
            self._right.populate(preO[len(left)+1:], right) #construct right
    #This method returns a string of the tree traversed post-order.  It's done so recursively because it is required.
    def getPostOrder(self):
        #LRN

        string = ''

        if self._right == None and self._left == None:
            return self._value
        if self._right == None and self._left != None:
            return self._left.getPostOrder() + ' ' + self._value
        if self._left == None and self._right != None:
            return self._right.getPostOrder() + ' '+ self._value
        else:
            return str(self._left.getPostOrder()) + ' ' + str(self._right.getPostOrder())+ ' ' + self._value
    #This method decodes a binary line where the binary codes indicate whether we traverse left or right starting from the root node. 
    def decode(self, line): #no recursion required
        currNode = self
        for c in line:
            if c == '0':
                currNode = currNode._left
            if c== '1' :
                currNode = currNode._right
            if currNode == None:
                currNode = self
            if currNode._left == None and currNode._right == None:
                print(currNode._value, end = '')
                currNode = self

        print()
                
                



        
    def __str__(self):
        if self._value == None: 
            return '' #empty string if no value at root
        else:
            return "({} {} {})".format(self._value, str(self._left), str(self._right)) 


'''This function reads a file by taking in a file name and reading it, using the function read().'''
def read(fileName):
    try:
        inFile = open(fileName)

        inFile = inFile.readlines()
    except:
        print("ERROR: Could not open file " + fileName)
        sys.exit(0)
        

    preOrder = inFile[0].strip().split()
    inOrder = inFile[1].strip().split()
    lineToDecode = inFile[2].strip()

    tree = DecodingTree() #This is the tree

    #FIXME - Add These methods to Decoding Tree class
    

    #PROCESSING THE INFORMATION
    tree.populate(preOrder, inOrder)
    postString = tree.getPostOrder()
    print(postString)
    tree.decode(lineToDecode)

    return
'''The main function is the main function and it does the main things that a main function must do, mainly'''
def main():
    filename = input("Input file: ")
    read(filename)

main()
    
