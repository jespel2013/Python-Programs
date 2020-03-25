#Jesse Pelletier
#Purpose: This program takes a .csv file of different types of pokemon and their stats, organizes them,
        # and prints out the Pokemon type with highest average statistic requested by the user.
#File Name: pokemon.py


def handleQuery(query, d): #This function prints out the type(s) with the highest average stat
    highestAvg = 0
    highestKey = [] #will be the list of Pokemon types that have the same highest average stat
    num = 99 #the number stays at 99 if the query is invalid
    
    
    query = query.lower()
    
    #these if/elif statements convert the query to an index that corresponds to the statistic the user wants
    if query == 'total':
        num = 0

    elif query == 'hp':
        num = 1

    elif query == 'attack':
        num = 2

    elif query == 'defense':
        num = 3

    elif query == 'specialattack':
        num = 4

    elif query == 'specialdefense':
        num = 5

    elif query == 'speed':
        num = 6

    

    if num!= 99: #if query is not invalid
        for key in d:
            if highestAvg < d[key][num]: #if there isnt two types with the same average, the list with the types starts over with a single type
                highestAvg = d[key][num]
                highestKey = [key]
            elif highestAvg == d[key][num]: #if there is a tie, we just add to the list of types
                highestKey.append(key)

    for i in range(len(highestKey)): #print out all types that have the same average
        print("{}: {}".format(highestKey[i], highestAvg))
            
    


    

    
    

    return 0
    

def computeAvgs(oldD): # This function computes the averages, puts them in a list for each type,
    #and uses a dictionary to map the type to the corresponding averages
    newD = {} #average dictionary
    avgList = []
    numChars = 0  
    summation = 0
    avg = 0
    
        
    for T in oldD:  # T = type -- for each key, we need 7 averages, so we loop through 
        for i in range(7): # i is the index of the stat we want to compute the average to
            for chars in oldD[T]: #chars = characters, for each character of Type T we increase numChars, and add the stat value of that character to sum
                numChars+=1
                summation += int(oldD[T][chars][i])
            avg = summation/numChars #compute the average for each stat
            avgList.append(avg)# add to the list of averages for each type
            summation = 0
            numChars = 0
        newD[T] = avgList #map type to list of averages
        avgList = []

    return newD
                
                
            
        

def convertToDict(LOL): #This function converts the lines in the .csv file to a two level dictionary of form {Type: {Character: Stats}}

    tempDict = {}

    for l in LOL:  #for line in list of lines
        if l[2] not in tempDict.keys(): #if the type isn't in the dictionary yet
            tempDict[l[2]] = {l[1]:l[4:11]} #l[4:11] are the only statistics that are relevent
        else:
            tempDict[l[2]][l[1]] = l[4:11]
    
    return tempDict

def readFile(): #This function takes in a file input and converts it to a list of lines.  Each line in the list is also a list.  
    inFile = open(input())
    listOfLines = []

    for line in inFile:
        if line[0] != '#':
            line = line.strip()
            line = line.split(',')
            listOfLines.append(line)
        
    return listOfLines
            
            

def main(): #The main function calls the different functions and takes user queries.

    LOL = readFile() #returns a list of lines of the file

    mainD = convertToDict(LOL) #converts the lines to a dictionary
    
    avgD = computeAvgs(mainD) #a new dictionary that contains the Pokemon types and their average stats
    

    userIn = 'default' # default user input to get into while loop
    while(len(userIn) != 0):
        userIn = input()
        handleQuery(userIn, avgD) #prints output according to user query
        
    
        
    

    return 0

main()

