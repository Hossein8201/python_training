day_begin = input()
list_crimes = [[0,0]]
list_days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
for i in range(30):
    crime = int(input())
    if i < 6:
        list_crimes += [[0,0]]
    list_crimes[i%7][0] += crime
    list_crimes[i%7][1] +=1
index = list_days.index(day_begin)
min_crime = list_crimes[0][0]/list_crimes[0][1]
for i in range(1,7):
    if min_crime > list_crimes[i][0]/list_crimes[i][1]:
        min_crime = list_crimes[i][0]/list_crimes[i][1]
        index = (index+i)%7
answer = list_days[index] + ' ' + str(int(min_crime))
print(answer)


