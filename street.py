'''Name: Jesse Pelletier
Description: This program takes a user input for a street and produces a rendering according to the user's
specification.
FileName: street.py'''

'''An instance of this class would be a representation of a building'''
class Building:
    def __init__(self, width, height, brick):
        self._width = int(width)
        self._height = int(height)
        self._char = brick
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    '''This method returns a string representation of the structure at height num'''
    def atHeight(self, num):
        if num < self._height:
            return self._char * self._width
        else:
            return ' ' * self._width
        
    

'''An instance of this class would represent an empty parking lot'''
class EmptyLot:
    def __init__(self, width, string):
        self._string = string.replace('_', ' ')
        self._width = int(width)
        self._height = 1
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    '''This method returns a string representation of the structure at height num'''
    def atHeight(self, num):
        if num == 0:
            return (self._string * (int(self._width/len(self._string))+1))[:self._width]
        else:
            return ' ' * self._width
        

'''An instance of this class represents a park'''
class Park:
    def __init__(self, width, leaves):
        self._width = int(width)
        self._leaves = leaves
        self._height = 5
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    '''This method returns a string representation of the structure at height num'''
    def atHeight(self, num):
        if num == 4: #top of tree
            return ' ' * (self._width//2) + self._leaves + ' ' * (self._width//2)
        elif num ==3:
            return ' ' * ((self._width-3)//2) + (self._leaves*3) + ' ' * ((self._width-3)//2)
        elif num == 2:
            return ' ' * ((self._width-5)//2) + (self._leaves*5) + ' ' * ((self._width-5)//2)
        elif num > 4:
            return ' ' * self._width
        else:
            return ' ' * (self._width//2) + '|' + ' ' * (self._width//2)

'''This function recursively converts the user input to a list of structures'''
def convertToStructures(userInput):
    if userInput == []: #base case
        return []
    else:
        if userInput[0][0] == 'p': #park
            item = userInput[0][2:].split(',')
            item = Park(item[0], item[1])

        elif userInput[0][0] == 'b':#building
            item = userInput[0][2:].split(',')
            item = Building(item[0], item[1], item[2])

        elif userInput[0][0] == 'e': #emptylot
            item = userInput[0][2:].split(',')
            item = EmptyLot(item[0], item[1])

        return [item] + convertToStructures(userInput[1:])

'''This function recursively finds the highest structure on the street'''
def findHighestStructure(L, highest):
    if L == []: #base
        return highest
    else:
        if L[0].getHeight() > highest:
            highest = L[0].getHeight()
        return findHighestStructure(L[1:], highest)
'''This function recursively finds the total width of the rendering'''
def findTotalWidth(L):
    if L == []: #base
        return 0
    else:
        return L[0].getWidth() + findTotalWidth(L[1:])
'''This function prints at a certain height'''
def printAtHeight(structures, height):
    if structures == []: #base
        return
    else:
        print(structures[0].atHeight(height), end = '')
        printAtHeight(structures[1:], height)
    return
'''This function recursively prints the street'''
def printRendering(structures, height):
    if height == -1:
        return
    else:
        print('|', end = '')
        printAtHeight(structures, height)
        print('|')
        printRendering(structures, height-1)

    return
    
def main():

    userInput = input("Street: ")

    #organize into list
    userInput = userInput.strip()
    userInput = userInput.split()

    listOfStructures = convertToStructures(userInput)

    height = findHighestStructure(listOfStructures, 0)
    width = findTotalWidth(listOfStructures)

    print('+' + '-'*width + '+')
    
    printRendering(listOfStructures, height)

    print('+' + '-'*width + '+')

    
main()
