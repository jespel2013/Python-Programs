# Name: Jesse Pelletier
# Purpose: This program is a model of half of the board game Battleship.  It models Player 1's ship
# placements and Player 2's guesses.
# FileName: battleship.py


# This class represents an object that represents a position on the grid.  
class GridPos:
    def __init__(self, x, y):  #when a new instance is created there is no ship
        self._x = x
        self._y = y
        self._ship = None
        self._isHit = 0 #not hit yet
    def getShip(self):
        return self._ship
    def getIsHit(self):
        return self._isHit
    #This method adds part of a ship in that grid position
    def changeShip(self, ship):
        self._ship = ship
    #If this grid position has been guessed already, the attribute _isHit is changed to 1
    def gotHit(self):
        self._isHit = 1
    def __str__(self):
        return ("({}, {}) + {}".format(self._x, self._y, self._ship))

# This class represents an object that represents one of the battleships.
class Ship:
    def __init__(self, name, start, end):
        self._name = name

        
        #done this way in order to work with how I populated the grid
        if start[0] < end[0] or start[1] < end[1]:
            newStart = start
            newEnd = end
        else:
            newStart = end
            newEnd = start
        if newStart[0] == newEnd[0]: #vertical
            self._size = newEnd[1] - newStart[1] + 1 #calculating the size -- will be tested for errors later
        else: #horizontal
            self._size = newEnd[0] - newStart[0] + 1
        self._end1 = newStart
        self._end2 = newEnd
        self._lives = self._size
    def getName(self):
        return self._name
    def getSize(self):
        return self._size
    def getStart(self):
        return self._end1
    def getEnd(self):
        return self._end2
    def getLives(self):
        return self._lives
    #This method keeps track of how many times the ship has been hit in different spots
    def gotHit(self):
        self._lives -= 1
    def __str__(self):
        return self._name 
    
# This class is a representation of the playing board.
class Board:
    def __init__(self):
        self._grid = []

        #populate board with a grid object with no ships
        for row in range(10):
            rowList = []
            for col in range(10):
                currPos = GridPos(col, row)
                rowList.append(currPos)
            self._grid.append(rowList)
        self._kills = 0
        self._names = []
    def getGrid(self):
        return self._grid
    def getKills(self):
        return self._kills
    def getNames(self):
        return self._names
    #This method takes in a guess and outputs a corresponding message
    def processGuess(self, guess):

        #illegal guess
        if (guess[0] > 9 or guess[0] < 0 or guess[1] > 9 or guess[1] < 0):
            print("illegal guess")
        elif (self._grid[guess[1]][guess[0]].getShip() == None): #nothing at position
            if (self._grid[guess[1]][guess[0]].getIsHit() == 1): #has been hit before
                print("miss (again)")
            else:
                self._grid[guess[1]][guess[0]].gotHit()
                print("miss")
        elif (self._grid[guess[1]][guess[0]].getShip() != None):
            if (self._grid[guess[1]][guess[0]].getIsHit() == 1):
                print("hit (again)")
            elif (self._grid[guess[1]][guess[0]].getShip().getLives() == 1): # The ship has been hit and sunk
                self._kills +=1
                print("{} sunk".format(self._grid[guess[1]][guess[0]].getShip()))
            else: #just a normal hit
                self._grid[guess[1]][guess[0]].getShip().gotHit()
                self._grid[guess[1]][guess[0]].gotHit()
                print("hit")

        if self._kills == 5: #all ships have been sunk
            print("all ships sunk: game over")
            return "done"
        return "okay"
   #This method adds a ship to the game board
    def addShip(self, ship):
        self._names.append(ship.getName()) #adds the ship name to the list of names
        x = ship.getStart()[0] #just reassigning the points to variables
        y = ship.getStart()[1]
        if ship.getStart()[0] ==ship.getEnd()[0]: #vertical ship
            for i in range(ship.getSize()):
                if str(self._grid[y+i][x].getShip()) in ['A', 'B', 'S', 'D', 'P']:
                    return False
                self._grid[y+i][x].changeShip(ship)
        else:
            for i in range(ship.getSize()): #horizontal ship
                if str(self._grid[y][x+i].getShip()) in ['A', 'B', 'S', 'D', 'P']:
                    return False
                self._grid[y][x+i].changeShip(ship)
        return True
    def __str__(self):
        return str(self._grid)

# This function tests the validity of a line of input from the ship placement texts
def testValidity(name, x1, y1, x2, y2, line, grid):
    
    if name in grid.getNames():
        print("ERROR: fleet composition incorrect")
        return False
    elif x1 > 9 or x2 > 9 or y1 > 9 or y2 > 9 or x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0:
        print("ERROR: ship out-of-bounds: " + line)
        return False
    elif not(x1 == x2 or y1 == y2):
        print("ERROR: ship not horizontal or vertical: " + line)
        return False
    

    return True

        
    
#This function initializes a Board object and populates the board with ships.
def processBoardFile(file):
    inFile = open(file)
    grid = Board()
    length = 0

    for line in inFile:
        
        origLine = line #for ease of printing purposes
        length +=1
        line = line.strip()
        line = line.split()
        
                              
        
        result = testValidity(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]), origLine, grid)
        if result == False:
            return "STOP"  #stop is returned to indicate to stop the program
        newShip = Ship(line[0], (int(line[1]),int(line[2])), (int(line[3]), int(line[4])))

        #length test
        shipDict = {'A':5, 'B':4, 'S':3, 'D':3, 'P':2}
        if shipDict[line[0]] != newShip.getSize():
            print("ERROR: incorrect ship size: " + origLine)
            return "STOP"


        boolean = grid.addShip(newShip)

        #returned False if there was not a None object in every coordinate newShip occupies
        if boolean == False:
            print("ERROR: overlapping ship: " + origLine)
            return "STOP"

    
    if length != 5:
        print("ERROR: fleet composition incorrect")
        return "STOP"

    return grid

#This function processes the guesses. 
def processGuessFile(file, grid):
    guesses = open(file)

    for guess in guesses:
        guess = guess.strip()
        guess = guess.split()
        x = int(guess[0])
        y = int(guess[1])
        response = grid.processGuess((x, y))
        if response == "done":
            return

    return

#This is the main function.  It calls on the other two functions to process the 2 inputs.  
def main():
    
    input1= input()
    input2= input()
    
    try:
        populatedGrid = processBoardFile(input1)
        if (populatedGrid == "STOP"):
            return
    
    except:
        print("ERROR: Could not open file: " + input1)
        return

    try:
        processGuessFile(input2, populatedGrid)
    except:
        print("ERROR: Could not open file: " + input2)
        return
    
    return

    

main()
