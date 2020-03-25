'''
Name: Jesse Pelletier
Purpose: This program analyzes some recent data to identify what they mainly focus on.  This is done by taking the words in the titles of recent news articles and organizing them in a linked list in descending order by the amount
of times the word occurs in the titles
FileName: fake-news.py
'''
import string
import csv

'''An object of this class represents information about a word'''
class Word:
    '''This method initializes an instance of an object'''
    def __init__(self, word):
        self._word = word
        self._count = 1
    def getWord(self):
        return self._word
    def getCount(self):
        return self._count
    '''Increments count by 1'''
    def increment(self):
        self._count += 1
    '''Special method to help sort.  Defines which of two words is greater than the other'''
    def __gt__(self, other):
        if self.getCount() < other.getCount():
            return True
        elif self.getCount() == other.getCount():
            return not self.getWord() < other.getWord()
        else:
            return False
    '''A string representation of the word object'''
    def __str__(self):
        return self._word + ' : ' + str(self._count)


'''This function processes the file and organizes relevant information into objects'''
def processInput(file):
    listOfWords = []
    p = string.punctuation
    
    inFile = open(file) #try - except
    csvReader = csv.reader(inFile)

    
    for lineList in csvReader:
        if lineList[0][0] != '#': #ignore lines that begin with a hashtag
            title = lineList[4] #title's index is 4
            for pMark in p: #replacing all punctuation with spaces
                title = title.replace(pMark, ' ')
            title = title.strip()
            title = title.split() #creates a list of words in title

            for word in title: #iterating through the words 
                if len(word) > 2:
                    word = word.lower()
                    found = 0
                    for w in listOfWords:
                        if word == w.getWord():
                            w.increment()
                            found = 1
                    if found == 0:
                        wordObj = Word(word)
                        listOfWords.append(wordObj)
                     #adds word to linked list if not there, increments count by one if it is

    
    return listOfWords

'''This recursive function merges two lists -- taken from recursion slides'''
def merge(L1, L2, merged):
    if L1 == [] or L2 == []:
        return merged + L1 + L2
    else:
        if L1[0] < L2[0]:
            new_merged = merged + [L1[0]]
            new_L1 = L1[1:]
            new_L2 = L2
        else:
            new_merged = merged + [L2[0]]
            new_L1 = L1
            new_L2 = L2[1:]
        return merge(new_L1, new_L2, new_merged)


'''This functions splits the unsorted list and calls merge  -- Taken from recursion slides'''
def mSort(L):
    if len(L) <= 1:
        return L
    else:
        splitIndex = len(L)//2
        L1 = L[:splitIndex]
        L2 = L[splitIndex:]
        sortedL1 = mSort(L1)
        sortedL2 = mSort(L2)
        return merge(sortedL1, sortedL2, [])

def printUpTo(num, L):
    threshold = L[num].getCount()

    i = 0
    while L[i].getCount() >= threshold:
        print(L[i])
        i+=1

    return
    

'''This function takes in the file input and does the high-level processes.'''
def main():
    fileName = input("File: ")
    
    try:  #error case where the file could not be opened
        wordList = processInput(fileName)
    except:
        print("ERROR: Could not open file " + fileName)
        return
    
    try: #error case where N can't be read or converted into an integer
        integer = int(input("N: "))
    except:
        print("ERROR: Could not read N")
        return

    assert integer >= 0 #assert N is a non-negative number

    sortedList = mSort(wordList)

    printUpTo(integer, sortedList)
    

main()
