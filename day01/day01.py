import math
    
def readFile():
    puzzleinput = []
    fp = open('puzzleinput.txt', 'r')
    for line in fp:
        puzzleinput.append(int(line.replace('\n', '')))
    return puzzleinput

def getModuleFuel(modules):
    moduleMasses = 0
    for mass in modules:
        tempModuleMass = int(round(mass / 3,0)) - 2
        moduleMasses += tempModuleMass 
    return moduleMasses

if __name__ == '__main__':
    print('Hohoho! Day 1!')
    modules = readFile()
    fuelNeeded = getModuleFuel(modules)
    print('Total amout of fuel needed: ' + str(fuelNeeded))
        
        


    


