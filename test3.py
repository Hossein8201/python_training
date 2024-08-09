# 
question = int(input())
answer = []
for i in range(question):
    length = int(input())
    answer_string = ['YES',0]
    string = input()
    number = 0
    index = 0
    flag = 1
    while(length-1 >= index):
        if (index +3 <= length):
            if (string[index] != 0) & (string[index+2] != 0):
                answer_string += [string[index:index+3]]
                index +=3
                number += 1
        elif (index +2 <= length):
            if (string[index] != 0) & (string[index+1] != 0):
                answer_string += [string[length:length+2]]
                index += 2
                number += 1
        else:
            flag = 0
            answer[i] = ['NO']
            break
    if(flag):
        answer_string[1] = number
        answer += [answer_string]
        print(answer)

print()
for i in range(question):
    for j in range(len(answer[i])):
        print(answer[i][j])
