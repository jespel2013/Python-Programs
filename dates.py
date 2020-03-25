# Jesse Pelletier
# Purpose: This program converts a text file of dates, events and inquiries.  It processes the inquiries by printing the events on the inquired date in alphabetical order.
# Filename: dates.py
'''This class creates an object that contains a list of events associated with a date'''
class Date:
    def __init__(self, date, event):  #creates an instance of the object with a date and a list with a single event associated with that date
        self._date = date
        self._events = [event]
    def get_date(self):
        return self._date
    def get_events(self):
        return self._event
    def add_event(self, event):  #adds an event to the events list
        self._events.append(event)
    def __str__(self): #simplifies printing by returning a string (with the form specified on the spec) that contains all the events associated with the date
        tempString = ''
        for event in sorted(self._events):
            tempString += self._date + ': ' + event + '\n'
        return tempString

'''This class creates an object that contains all the date objects in a dictionary with the date as a key'''
class DateSet:
    def __init__(self): #creates an instance of the DateSet with a single dictionary mapping dates to date objects
        self._set = {}
    def get_set(self):
        return self._set
    def add_date(self, date, event): # adds a date object as a value and the date as the key
        if date not in self._set.keys(): #creates new key if date is not in the DateSet's keys
            self._set[date] = [event]
        else:
            self._set[date].append(event)
    def get_keys(self):
        return self._set.keys()
    def get_date(self, date): # returns the value of a key
        if date in self._set.keys():
            return self._set[date]
    def add_event(self, key, event): # adds an event to the date object (the value)
        self._set[key][0].add_event(event)
    def __str__(self): #simple string representation of a Dateset object
        return str(self._set())
'''This funtion converts any form of date encountered into canonical form'''
def convertDate(date_str):
    month = ''
    day = ''
    year = ''
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] # list of months to make month conversion easier
  
    if '-' in date_str: #1st possible format
        date_str = date_str.split('-')
        month = date_str[1]
        
        if month[0] == '0': #the month shouldn't start with a 0
            month = month.strip('0')
        day = date_str[2]
        if day[0] == '0': #the day shouldn't start with a zero
            day = day.strip('0')
        year = date_str[0]
        assert int(month) < 13 and int(day) < 32, "Error: Illegal date."  #assertion specified in the assignment spec.  It's contained in each if statement
        return year + '-' + month + '-' + day
    elif '/' in date_str: #2nd possible format
        date_str = date_str.split('/')
        month = date_str[0]
        day = date_str[1]
        if month[0] == '0': 
            month = month.strip('0')
        day = date_str[1]
        if day[0] == '0':
            day = day.strip('0')
        year = date_str[2]
        assert int(month) < 13 and int(day) < 32, "Error: Illegal date."
        return year + '-' + month + '-' + day
    else: # last possible format
        date_str = date_str.split()
        year = date_str[2]
        day = date_str[1]
        if day[0] == '0':
            day = day.strip('0')
        for i in range(len(months)): #convert name of month to number that represents that month
            if months[i] == date_str[0]:
                month = i+1
        assert int(month) < 13 and int(day) < 32, "Error: Illegal date."
        return year + '-' + str(month) + '-' + day

    
'''This function processes all input from the input file'''
def processInput(file): #FIXME
    inFile = open(file)

    dates = DateSet() #creates a dateSet object
    

    for line in inFile:
        line = line.strip()
        assert line[0] == 'I' or line[0] == 'R', "Error: Illegal Operation." #specified in assignment spec
        if line[0] == "I":
            line = line[2:] #removes operation from line String
            line = line.split(':') #splits along the colons
            line[0] = line[0].rstrip().lstrip()  #deleting extra whitespace

            
            
            line[0] = convertDate(line[0]) #coverts date to canonical representation
            tempString = ''
            
            i=0
            for item in line[1:]: #if any event strings have a colon in them, we replace that colon
                if i > 0:
                    tempString += ': '
                item = item.rstrip().lstrip()
                tempString+= item
                i+=1
            
            if line[0] not in dates.get_keys(): # if the date isn't in the dateSet, we must add a key:value pair to it
                newDate = Date(line[0], tempString)
                dates.add_date(line[0], newDate)
            else: #otherwise we add an event to the date object
                dates.add_event(line[0], tempString)
  
        else:
            line = line[2:] # removes operation portion of line
            line = line.rstrip().lstrip()
            line = convertDate(line)
            listOfDates = dates.get_date(line) # a list of just the date objects associated with the date (should be one date object)
            if len(listOfDates) >0: # if there are events associated with the key
                for date in listOfDates:
                    print(date, end = '')     
    
    return 0
'''The main function simply calls the process input function'''          
def main():
    processInput(input())
    
    return 0
main()
