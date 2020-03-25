'''
Name: Jesse Pelletier
Description: This program reads in data about basketball teams (team name, conference, wins, losses)
from a file, then calculates and prints out the conference(s) with the highest win ratio.  
FileName: bball.py
'''
class Team: 
    def __init__ (self, line):
        assert len(line) == 2, "Line Parsed Incorrectly"
        self._name = line[0]
        self._conference = line[1][0]
        self._wins = int(line[1][1][0])
        self._losses = int(line[1][1][1])
    def getName(self): #getter for name
        return self._name
    def getConf(self): #getter for conference name
        return self._conference
    def winRatio(self): #computes win ratio
        assert (self._wins + self._losses) != 0, "Cannot Divide By Zero"
        return self._wins/(self._wins + self._losses)
    def __str__(self): #string representation of Team object
        return "{} : {}".format(self._name, str(self.winRatio()))

class Conference:
    def __init__(self, conf): #Creates instance of Conference object
        assert type(conf) == str, "Conference attribute is not the correct type"
        self._name = conf
        self._teams = [] #initializes list of teams in the conference
    def __contains__(self, team): #special method find if team is in the conference
        assert type(team) == Team, "team variable is incorrect type" #asserts that team is a team object
        if team in self._teams:
            return True
        else:
            return False
    def getName(self): #getter for conference name
        return self._name
    def addTeam(self, team):
        assert type(team) == Team, 'team variable is incorrect type'
        self._teams.append(team)
    def avgWinRatio(self): #computes average win ratio for the teams in division
        totalPerc = 0
        totalTeams = len(self._teams)
        assert totalTeams > 0, "No teams in division"
        for team in self._teams:
            #INVARIANT -- Total percentage is greater than or equal to any individual team win percentage
            totalPerc += team.winRatio()
        
        return totalPerc/totalTeams
    def __str__(self):  #string representation of Conference object
        return "{} : {}".format(self._name, str(self.avgWinRatio()))

class ConferenceSet:
    def __init__(self): #creates instance of a conference set
        self._conferences = []
        self._confStrings = []
    def addTeam(self, team): #adds a team to the correct conference
        assert type(team) == Team
        if team.getConf() in self._confStrings:
            for conf in self._conferences: #finds correct conference
                if conf.getName() == team.getConf():
                    conf.addTeam(team)
                    #INVARIANT -- The amount of teams in the conference object must be at least 2
        else: #creating new conference in set
            newConf = Conference(team.getConf())
            newConf.addTeam(team)
            self._conferences.append(newConf)
            self._confStrings.append(newConf.getName())
            assert len(self._conferences) == len(self._confStrings) #the _confstrings attribute is a list of the names of the conferences
    def best(self): #creates a list of the conference(s) with the highest win percentage
        assert len(self._conferences) > 0, "No Conferences in Set"
        currAvg = 0
        bestList = []
        bestAvg = 0
        for conf in self._conferences:
            #INVARIANT -- the currAvg is the average of the last conference
            currAvg = conf.avgWinRatio()
            if currAvg > bestAvg:
                bestAvg = currAvg
                bestList = [conf]
            elif currAvg == bestAvg:
                bestList.append(conf)
        return bestList

'''This function initializes a conference set and process the information that was read from the file'''
def processLines(lines):
    assert len(lines) > 0, "No lines to process"
    confSet = ConferenceSet()
    for line in lines:
        newTeam = Team(line)
        confSet.addTeam(newTeam)

    for conf in confSet.best():  #output
        print(conf)
    return
        
'''This function reads a user specified fileName and organizes the information in the file into a list of lists that can be used to create a team object'''
def readFile(fileName):
    try:
        inFile = open(fileName)
    except:
        print("ERROR: Could not open file " + str(fileName))
        return 
    listOfLines = []
    for line in inFile:
        line = line.replace("\t", " ") #replaces tabs
        line = line.strip()
        if line[0] != '#': #lines with a hashtag are comments
            assert len(line) > 0, "Line contains no information"
            for i in range(len(line)-1, 0, -1):
                if line[i] == '(': #splits after the perentheses that indicates the conference
                    line = [line[0:i], line[i+1:]]
                    line[1] = line[1].split(')')
                    line[1][1] = line[1][1].split()
                    break
            listOfLines.append(line) #appends single team info to list

    processLines(listOfLines)
    return

'''This function calls all necessary functions and takes input for the file name'''
def main():
    readFile(input())
    return

main()
