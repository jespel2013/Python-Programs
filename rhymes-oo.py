#Name: Jesse Pelletier
#Purpose: This program finds words that rhyme with a given word.
#FileName: rhymes-oo.py

'''An instance of this class represents a word'''
class Word:
    def __init__(self, word, pronunciation):
        self._word = word
        self._pronunciations = [pronunciation]
    def getWord(self):
        return self._word
    def getPronunciations(self):
        return self._pronunciations
    def addPronunciation(self, newPro): #adds a different pronunciation of a word
        self._pronunciations.append(newPro)
    def __eq__(self, other):#FIXME: not sure how this special method will be used
        stressedV = []
        lastSound = ''
        for p in self._pronunciations: # for each pronunciation in pronunciations
            for index, sound in enumerate(p):
                if '1' in sound: #finds the primary stress and copies the phenomes from that point onward
                    if index == 0:
                        lastSound = p[index]
                    else:
                        lastSound = p[index-1] #used to compare the sound before the primary stress
                    stressedV = p[index:]
            for p2 in other._pronunciations: #iterate through other words pronunciations
                for j in range(len(p2)):
                    if p2[j:] == stressedV and p2[j - 1] != lastSound and p2 != p: #last statement is making sure the pronunciations aren't the same (not only the words)
                        return True
        return False
                    
    def __str__(self):
        return self._word + str(self._pronunciations)

'''An instance of this class represents data structures and methods to associate words with the corresponding word objects'''
class WordMap:
    def __init__(self):
        self._map = {}
    def getMap(self):
        return self._map
    def readDictionary(self, file): #This method reads in a pronunciation dictionary and maps words to objects
        try:
            inFile = open(file)
        except:
            print("ERROR: Could not open file " + file)
            return

        for line in inFile:
            line = line.strip()
            line = line.split()
            if line[0].lower() in self._map.keys(): #line[0] is the word, the rest of the line is the phenomes
                self._map[line[0].lower()].addPronunciation(line[1:])
            else:
                self._map[line[0].lower()] = Word(line[0].lower(), line[1:])

         
    def printRhymes(self, wordIn): #This method reads in a word and prints out the words that rhyme with it
        rhymingWords = []
        try:
            specialWord = self._map[wordIn.lower()] # a list of different pronunciations of the user input
        except:
            print("ERROR: the word input by the user is not in the pronunciation dictionary " + wordIn.lower())
            return
        for word in self._map.keys(): #Iterating through the words
            if word.lower() != wordIn.lower() and specialWord == self._map[word]:
                rhymingWords.append(word)
        
        for rhymingWord in sorted(rhymingWords):
            print(rhymingWord.lower())
    def __str__(self): 
        return str(self._map)

    
'''This function takes in user input and creates an instance of the WordMap.
The methods of the WordMap do most of the processing and computation'''
def main():
    wordDict = WordMap()
    
    wordDict.readDictionary(input())

    if wordDict.getMap() != {}: #empty dictionary means no file was read
        wordDict.printRhymes(input())

main()
    
