# Jesse Pelletier
# Purpose: This program takes input from two files: one with a list of words and one with a grid full of letters.
# The program reads these files and searches to see if any of the words can be found in the grid, reminiscent of a crossword puzzle.
# If there are any matches, the program prints out those matches.  
# File name: word-search.py


def read_file(file):  # reads the file and turns the file into a list of lists.
    words = []
    inFile = open(file)

    for line in inFile:
        line = line.strip()
        line = line.lower()
        line = line.split()
        words.append(line)


    

    return words
def occurs_in(string, letters):  # This function searches the grid for any matches by creating a
                                 # temp word with the characters in the grid and seeing if the string
                                 # provided is in that new temporary word.
    
    tempWord = ''


    for i in range(len(letters)): #horizontal forward
        for j in range(len(letters)):
            tempWord += letters[i][j]
            
        if(string in tempWord):
            return True
        tempWord = ''

    for i in range(len(letters)): #horizontal backward
        for j in range(len(letters) -1, -1,-1):
            tempWord += letters[i][j]
        if(string in tempWord):
            return True
        tempWord = ''

    for i in range(len(letters)): #vertical top first
        for j in range(len(letters)):
            tempWord += letters[j][i]
        if(string in tempWord):
            return True
        tempWord = ''

    for i in range(len(letters)): #vertical bottom first
        for j in range(len(letters)-1, -1, -1):
            tempWord += letters[j][i]
        if(string in tempWord):
            return True
        tempWord = ''

    #diagonal from top

    for i in range(len(letters)):
        for j in range(len(letters)-i):
            tempWord += letters[j][j+i]
        if(string in tempWord):
            return True
        tempWord = ''

    #diagonal from sid

    for i in range(len(letters)):
        for j in range(len(letters)-i):
            tempWord += letters[j+i][j]
        if(string in tempWord):
            return True
        tempWord = ''

    return False
    


    
def search(words, letters): # This function adds the word to a list if there are matches in the grid.
    matches = []
   
    for i in range(len(words)):
        if(occurs_in(words[i][0], letters)):
            matches.append(words[i])

    return matches

def print_matches(matches):  #Takes a list of matches, sorts them, and prints them out.  
    matches.sort()

    for i in range(len(matches)):
        print(matches[i][0])
    

def main():  # This function takes the input for file names, then uses those
            #files to call the other functions that do the heavy lifting. 
    wordFile = input()
    letterFile = input()

    wordList = read_file(wordFile)
    letterGrid = read_file(letterFile)

    matches = search(wordList, letterGrid)

    print_matches(matches)

    return 0

main()

    

    
