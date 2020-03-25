"""
Jesse Pelletier
Purpose: This program acts as a writer bot and generates a pseudo-randomized text using the Markov Chain algorithm
File Name: writer-bot.py
"""

import random
NONWORD = " "
SEED = 8


def produceChain(words, size):
    """Produces the Markov Chain used to generate a new text"""

    markovChain = {}
    prefix = ()

    for i in range(size):  #This loop generates the key value pairs that include NONWORDS
        if i == 0:
            markovChain[(NONWORD,)*size] = [words[0]]
        else:
            key = [NONWORD]*(size-i)
            for j in range(size - len(key)):
                key.append(words[j])
            key = tuple(key)
            markovChain[key] = [words[j]]
    
    for i in range(len(words)-size+1):  #Loops through the list of words in the file, generates keys, and assigns them with a suffix, which is appended to a list of suffixes 
        prefix = tuple(words[i:i+size])
        if prefix in markovChain.keys(): 
                
                if i != len(words)-size:
                    markovChain[prefix].append(words[i+size])
                else: #if we are at the last possible prefix pair
                    markovChain[prefix].append(NONWORD) 
        else:
            if i != len(words)-size:
                markovChain[prefix] = [words[i+size]]
            else: #If the loop is at the last possible prefix pair
                markovChain[prefix] = [NONWORD]
    
    return markovChain

def readFile(sFile):
    """Reads the user-specified file and converts the entire file into a single string, and that string to a list"""
    inFile = open(sFile)
    fileString = ''
    for line in inFile:
        fileString += line
    fileString = fileString.strip()
    fileString = fileString.split() #converts to list

    assert (len(fileString) > 0)
    
    return fileString

def generateText(chain, num, size, words):
    """Generates the final randomized text in the form of a text list"""
    random.seed(SEED)
    textList = []
    randomNum = 0
    key = []


    for index in range(size):  #appends the only N words that could start the text
        textList.append(words[index])


    for i in range(num - size):
        for j in range(0, size):  #Generates a key that is N words long
            key.append(textList[i+j])
            
        currSuffix = chain[tuple(key)]
        key = []  #resets key
            
            
        if len(currSuffix) > 1: #if the suffix list has a length greater than 1, the program select a random word within the list
            randomNum = random.randint(0, len(currSuffix)-1)  
            textList.append(currSuffix[randomNum])
        else:
            textList.append(currSuffix[0]) #first (only) word in the suffix list
        
    
    return textList

def printText(text):
    """Prints the generated Text"""
    for i in range(len(text)):
        if i%10 == 0 and i != 0: #new line after ten words
            print()
        print(text[i], end = '')

        if i % 10 != 9 and i != len(text) - 1: #space after every word not at the end of the line
            print(' ', end = '')
        if i == len(text) -1: #new line at the end of the file 
            print()

    
            
    return
def main():
    """The main function.  It takes in user inputs and calls other functions"""

    listWords = readFile(input())
    prefixSize =  int(input())
    
    numWords =  int(input())

    #asserts
    assert prefixSize > 0
    assert numWords > 0
    chain = produceChain(listWords, prefixSize)
    
    text = generateText(chain, numWords, prefixSize,listWords)
    printText(text)
    

    return

main()
