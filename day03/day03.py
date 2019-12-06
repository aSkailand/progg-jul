fp = open('./puzzleinput.txt', 'r')
wireMap = []
for line in fp:
    wireMap += [line.replace('\n', '').split(',')]

def createMap(wireMap):
    wireMapRoad = []
    positionX = 0
    positionY = 0
    for i in range(len(wireMap)):

        if(wireMap[i][0] == 'U'):
            for j in range(int(wireMap[i][1:])):
                wireMapRoad.append([positionX, positionY + j])
            positionY += int(wireMap[i][1:])

        if(wireMap[i][0] == 'R'):
            for j in range(int(wireMap[i][1:])):
                wireMapRoad.append([positionX + j, positionY])
            positionX += int(wireMap[i][1:])
            
        if(wireMap[i][0] == 'D'):
            for j in range(int(wireMap[i][1:])):
                wireMapRoad.append([positionX, positionY - j])
            positionY -= int(wireMap[i][1:])

        if(wireMap[i][0] == 'L'):
            for j in range(int(wireMap[i][1:])):
                wireMapRoad.append([positionX -j, positionY])
            positionX -= int(wireMap[i][1:])
        


    return wireMapRoad
    

wireMap1 = createMap(wireMap[0])
wireMap2 = createMap(wireMap[1])



for i in range(len(wireMap2)):
    if(wireMap2[i] in wireMap1):
        print(abs(wireMap2[i][0]) + abs(wireMap2[i][1]))
            
