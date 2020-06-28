import time
from os import system, name

def clear(): 
  
    # Windows Process 
    if name == 'nt': 
        _ = system('cls') 
  
    # Mac, Linux Process
    else: 
        _ = system('clear') 

def makeUsers():
    """
    Constructs each user-initial pair into a referenced dictionary.
    """
    
    numberUsers = input("How many people are in the video? (Max: 10)");
    validNums = str([i for i in range(1,11)])
    
    while numberUsers not in validNums:
        numberUsers = input("How many people are in the video? (Max: 10)");
    
    users = {};
    inv = 2
    
    for i in range(int(numberUsers)):
        name = input("What is your name?");
        while len(name) == 0:
            name = input("What is your name?");
        
        if name[0] in users.keys():
            users[name[0] + str(inv)] = name
            
        else:
            users[name[0]] = name;
            
        clear()
        
        print("Users thus far: ")
        for key in users.keys():
            print(users[key] + ", referenced by " + key)
    
    return users, users.keys;

def EpisodeInfo():
    """
    Returns user input about what project for which the program is used.
    """
    
    name = input("What's the series name (Abbreviate it!)?")
    num = input("What's the EP number?")
    clear()
    
    return name, num

def Timestamp(users, symbols, name, num):
    """
    Asks for input in a given format (told to the user), then writes it to a file.
    """
  
    isEPDone = False
    hasEPBegun = False
    curseOrEdit = ['c','e']
    curseOrEditDict = {curseOrEdit[0]: ' cursed at ',
                       curseOrEdit[1]: ' needs an edit at '}
    
    filename = 'editsfor' + name + 'EPNo' + num + '.txt'
    file = open(filename, "a+")
    
    while not hasEPBegun:
        start = input("When you are ready, type 'begin' and hit Enter to begin the EP!")
        if start == 'begin':
            start = time.time()
            clear()
            hasEPBegun = True
            
    while not isEPDone:
        
        
        print("Type the timestamp with the first letter of the person's name, then a COMMA, 'c' for Curse and 'e' for Edit (no spaces).")
        print("Example: User 'Test': to edit = 'T,e'; to note a curse = 'T,c'.")
        print("If done, type 'done' to close the program.")
        
        edit = input("BWAP! (type the timestamp here): ")
        if edit.lower() == 'done':
            clear()
            file.close()
            break
        
        while "," not in edit:
            edit = input("BWAP! (type the timestamp here): ")
        
        edit = edit.split(",")
        
        currTime = time.time()
        
        
        hours, rem = divmod(currTime - start, 3600)
        minutes, seconds = divmod(rem, 60)
        minSec = ("{:0>2}:{:0>2}".format(int(hours),int(minutes),seconds))
        
        
        secPerMin  = 60
        secPerHour    = 3600
        

        
        seconds = currTime - start

        #Calculate the days, hours, minutes and seconds

        hours = seconds / secPerMin
        seconds = seconds % secPerHour

        minutes = seconds / secPerMin
        seconds = seconds % secPerHour

        minSec = str("%02d:%02d:%02d"%(hours,minutes,seconds))
        
        
        symbol = edit[0].upper()
        whatToDo = edit[1].lower()
        
        if whatToDo not in curseOrEdit:
            whatToDo = input("Type 'c' for Curse for 'e' for Edit.")
        
        file.write(users[symbol] + curseOrEditDict[whatToDo] + minSec + '\n')
        
        
        
def main():
    users, symbols = makeUsers()
    name, num = EpisodeInfo()
    
    Timestamp(users, symbols, name, num)

main()
