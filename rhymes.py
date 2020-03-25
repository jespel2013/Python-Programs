# Jesse Pelletier
# Purpose: This program takes in a user input and finds words that rhyme with that input.
# File Name: rhymes.py




#This function prints the words that rhyme with the user's input.
def printWords(wordsList):

    for word in wordsList:
        print(word)

    return 0

#This function converts the file into a dictionary.  The keys are the words, and the value is a list of pronunciations, which
# is itself, a list of phenomes.
def convertFile(fileName):

    inFile = open(fileName)
    wordsDict = {}

    for line in inFile:
        line = line.strip()
        line = line.split()
        if line[0] in wordsDict.keys(): #line[0] is the word, the rest of the line is the phenomes
            wordsDict[line[0].upper()].append(line[1:])
        else:
            
            wordsDict[line[0].upper()]= [] #empty list
            wordsDict[line[0].upper()].append(line[1:]) # append to that list
            

    

    return wordsDict

#This function finds words that rhyme with the user input and stores them in a list.  
def findWords(specialWord, allWords):

    rhymingWords = []
    stressedV = []
    lastSound = ''
    
    pronunciations = allWords[specialWord] # a list of different pronunciations of the user input

    for p in pronunciations: # for each pronunciation in pronunciations
        for index, sound in enumerate(p):
            if '1' in sound: #finds the primary stress and copies the phenomes from that point onward
                if index == 0:
                    lastSound = p[index]
                else:
                    lastSound = p[index-1] #used to compare the sound before the primary stress
                stressedV = p[index:]
        for word in allWords: 
            for pro in allWords[word]:
                for j in range(len(pro)):
                    if pro[j:] == stressedV and word != specialWord and pro[j - 1] != lastSound:
                        #if the pronunciation is the same after the primary stress, the
                        #sound before that stress is different, and the words aren't the same
                        #we add to the list of rhyming words
                        
                        rhymingWords.append(word)

    return rhymingWords
        

    

    
    
#This is the main function that calls the other functions, as well as takes the user input.
def main():

    allWords = convertFile(input())

    rhymingWords = findWords(input().upper(),allWords)

    printWords(rhymingWords)

    return 0

#Runs program
main()
