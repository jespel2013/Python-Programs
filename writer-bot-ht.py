"""
Jesse Pelletier
Purpose: This program acts as a writer bot and generates a pseudo-randomized text using the Markov Chain algorithm
File Name: writer-bot.py
"""
import sys
import random
NONWORD = "@"
SEED = 8




'''This class is an implementation of a hash table'''
class HashTable:
    def __init__(self, size):
        self._size = size
        self._pairs = [None] * size
    '''This is the hash function.  It computes a polynomial and returns a hash value as an integer'''
    def hash(self, key):
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size
    '''Hashes key and inserts key-value pair in the hash table'''
    def put(self, key, value):  #value must be passed in as list
        hashValue = self.hash(key)
        if self._pairs[hashValue] == None:
            self._pairs[hashValue] = [key, [value]]
        else:
            while self._pairs[hashValue] != None: #decrement until spot on table is free
                if self._pairs[hashValue][0] == key:
                    self._pairs[hashValue][1].append(value)
                    return
                hashValue -= 1
            self._pairs[hashValue] = [key,[value]]
    '''Looks up a key in the hash table and if found, returns the value.  returns None otherwise'''
    def get(self, key):
        hashValue = self.hash(key)
        if self._pairs[hashValue][0] == key:
            return self._pairs[hashValue][1]
        else: #linear probing
            while self._pairs[hashValue][0] != key:
                
                hashValue -= 1
                if self._pairs[hashValue] == None:
                    return None
            return self._pairs[hashValue][1]
    '''Special method to see if a key is already in a hashtable'''
    def __contains__(self, key):
        hashValue = self.hash(key)
        if self._pairs[hashValue][0] == key:
            return True
        else: #linear probing
            while self._pairs[hashValue][0] != key:
                if self._pairs[hashvalue] == None:
                    return False
                hashValue -= 1
            return True
    def __str__(self):
        string = ''
        for i in range(len(self._pairs)):
            if self._pairs[i] != None:
                string += (self._pairs[i][0] + '\t' + str(self._pairs[i][1]) + '\n')
            else:
                string += '\n'
        return string


def produceChain(words, preSize, hashSize):
    """Produces the Markov Chain used to generate a new text"""

    markovChain = HashTable(hashSize)
    prefix = ''

    for i in range(preSize):  #This loop generates the key value pairs that include NONWORDS
        if i == 0:
            key = (NONWORD+' ')*preSize
            key = key.strip()
            markovChain.put(key, words[0])
        else:
            key = (NONWORD+' ')*(preSize-i)
            for j in range(i):
                key += words[j] + ' '

            key = key.strip()
            markovChain.put(key, words[j])
    
    for i in range(len(words)-preSize+1):  #Loops through the list of words in the file, generates keys, and assigns them with a suffix, which is appended to a list of suffixes 
        prefix = ''
        for j in range(preSize):
            prefix += words[i+j] + ' '
        prefix = prefix.strip()
                
        if i != len(words)-preSize:
            markovChain.put(prefix, words[i+preSize])
        else: #if we are at the last possible prefix pair
            markovChain.put(prefix, NONWORD)
    
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
    key = ''


    for index in range(size):  #appends the only N words that could start the text
        textList.append(words[index])


    for i in range(num - size):
        for j in range(0, size):  #Generates a key that is N words long
            key += textList[i+j] + ' '
        key = key.strip()
            
        currSuffix = chain.get(key)
        key = ''  #resets key
            
            
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
"""The main function.  It takes in user inputs and calls other functions"""
def main():
    

    listWords = readFile(input())
    tableSize = int(input())
    prefixSize =  int(input())
    numWords =  int(input())
    #asserts
    if prefixSize < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
        
    if numWords < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)
        
    chain = produceChain(listWords, prefixSize, tableSize)

    text = generateText(chain, numWords, prefixSize,listWords)
    printText(text)
    

    return

main()
