question , turn = map(int,input().split())
list = [0]
list_answer = ['o']
for i in range(1,question+1):
    list += [int(input())]
    Max = max(list[i-1],list[i])
for i in range(1,Max+1):
    if(i==1 or (i-1)%(turn+1)==0):
        list_answer += ["Peygir"]
    elif(i==2 or list_answer[i-1]=="Morshed" or (list_answer[i-1]=="Peygir" and list_answer[i-2]=="Morshed")):
        list_answer+=["Tannaz"]
    elif(i==3 or list_answer[i-1]=="Tannaz" or (list_answer[i-1]=="Peygir" and list_answer[i-2]=="Tannaz")):
        list_answer+=["Jeddy"]
    else:
        list_answer+= ["Morshed"]
for i in range(1,question+1):
    print(list_answer[list[i]])