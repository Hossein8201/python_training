def calculate_floor(string):
    floor=0
    for i in range(4):
        if(string[i]=='U'):     floor+=1       
        else:   floor-=1
    return floor