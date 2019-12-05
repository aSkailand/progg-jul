import math
    
def readFile():
    puzzleinput = []
    fp = open('puzzleinput.txt', 'r')
    for line in fp:
        puzzleinput.append(int(line.replace('\n', '')))
    return puzzleinput

def getModuleFuel(modules):
    moduleMasses = 0
    fuelFuelMass = 0
    for mass in modules:
        tempModuleMass = int(round(mass / 3,0)) - 2
        moduleMasses += tempModuleMass 
        fuelFuelMass += getFuelFuel(tempModuleMass)
    return moduleMasses, fuelFuelMass

def getFuelFuel(fuelMass):
    tempFuel = fuelMass
    cummulativeFuel = 0
    while(tempFuel != 0): 
        print(tempFuel)
        tempFuel = int(round(tempFuel/3))-2
        if(tempFuel < 0):
            break
        else:
            cummulativeFuel += tempFuel
       
    return cummulativeFuel



if __name__ == '__main__':
    print('Hohoho! Day 1!')
    modules = readFile()
    fuelNeeded = getModuleFuel(modules)
    print(fuelNeeded[0] + fuelNeeded[1])
    print('Total amount of fuel needed: ' + str(fuelNeeded))
        
        


    


