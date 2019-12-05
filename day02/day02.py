fp = open('./puzzleinput.txt', 'r')
puzzleString = ''
for line in fp:
    puzzleString += line
puzzleListCopy = [int(i) for i in puzzleString.split(',')]

def gravityCalc(puzzleList, noun, verb):
    puzzleList[1] = noun
    puzzleList[2] = verb
    for i in range(0, len(puzzleList), 4):
        if(puzzleList[i] == 1):           
            puzzleList[puzzleList[i+3]] = puzzleList[puzzleList[i+1]] + puzzleList[puzzleList[i+2]]
        elif(puzzleList[i] == 2):
            puzzleList[puzzleList[i+3]] = puzzleList[puzzleList[i+1]] * puzzleList[puzzleList[i+2]]
        elif(puzzleList[i] == 99):
            return puzzleList[0]

# part one        
print(gravityCalc(puzzleListCopy.copy(), 12, 2))

# part two
for noun in range(0,100):
    for verb in range(0,100):
        if(gravityCalc(puzzleListCopy.copy(), noun, verb) == 19690720):
            print(100 * noun + verb)
            