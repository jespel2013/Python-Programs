'''
Name: Jesse Pelletier
Description: This program uses classes to read a user-specified file and organizes all the user specified
    sized ngrams.  It then prints out all the ngrams with the most appearances in the file.  
FileName: ngrams.py
'''

'''This class holds an open file and has methods to process the information'''
class Input:
    def __init__(self): 
        fileName = input()
        try:
            self._file = open(fileName)
        except:
            print("ERROR: Could not open file " + fileName)
            quit
        
    def getFileName(self):
        return self._fileName
    def wordlist(self): #creates a list of all the words in the file that are valid for computing ngrams
        #INVARIANT -- the file is not blank.  That has already been asserted in the initialization of the instance. 
        listOfWords = []
        numBlanks = 0
        for line in self._file:
            line = line.split()
            for word in line:
                word = word.strip()
                word = word.strip("?!.',:\"_&$%@") #removes extra punctuation
                if len(word) != 0:
                    #INVARIANT -- word is not a blank space
                    listOfWords.append(word.lower())
        return listOfWords
    
'''This class holds a dictionary with ngrams of self._num length and their occurences'''
class Ngrams:
    def __init__(self):
        self._num = int(input())
        assert self._num > 0 #ngrams cannot have a negative or zero length
        self._nDict = {}

    def update(self, ngram):#updates the dictionary for a specific ngram
        assert type(ngram) == tuple
        if ngram in self._nDict.keys(): #adds an occurence of the engram
            self._nDict[ngram] += 1
        else:
            self._nDict[ngram] = 1 #appends to the ngram dictionary

    def processWordList(self, wordList): #creates ngrams of self._num length
        assert len(wordList) >= self._num #assert that there's enough words to create at least 1 ngram
        
        for i in range(len(wordList) - self._num+1): #iterate through wordlist
            currGram = () #initialize tuple
            for j in range(self._num):
                currGram += (wordList[i+j],) #adds self._num words to currGram
            assert len(currGram) == self._num #correct ngram length
            self.update(currGram)
            
    def printMaxNgrams(self): #finds the ngram with the max occurences and prints all ngrams with that many occurences
        maxNum = 0
        maxKeys = []

        for key in self._nDict.keys():
            #INVARIANT -- The maxNum is larger than the occurences of all the ngrams before it
            if self._nDict[key] > maxNum:
                maxKeys = [key] #refresh maxKeys list
                maxNum = self._nDict[key]
            elif self._nDict[key] == maxNum: #another ngram with the same amount of occurences
                maxKeys.append(key)

        for ngram in maxKeys:
            #INVARIENT -- nString is the previous nGram with the highest amount of occurences
            nString = ''
            for word in ngram: #creates string from ngram tuple
                nString += word + " "

            print("{} -- {}".format(str(maxNum), nString.strip()))

'''This is the main function.  It shows the basic flow of the program.  It creates an input and ngram object, and calls the necessary functions and methods to meet the program requirements'''
def main():
    
    inp = Input()
    
    grams = Ngrams()
    wordList = inp.wordlist()
    assert len(wordList)>0, "Empty wordlist"
    grams.processWordList(wordList)
    grams.printMaxNgrams()
    return
    

main()
