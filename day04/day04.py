counter = 0 
for pw in range(172930, 683083):
    temp_pw = str(pw)
    isBigger = False
    hasNeighbour = False
    for i in range(len(temp_pw)-1):
        if(int(temp_pw[i]) > int(temp_pw[i+1])):
            isBigger = True
    if(isBigger == False):
        for i in range(len(temp_pw)-1):
            if(int(temp_pw[i]) == int(temp_pw[i+1])):
                hasNeighbour = True
                break
    if((isBigger == False) and hasNeighbour):
        print(temp_pw)
        counter += 1
print(counter)
        

