t = int(input())
answer_list=[]
for i in range(t):
    a , b, h = map(int,input().split())
    h_ = h -a
    tt = a - b
    if(h_ % tt == 0):
        answer = h_/tt+1
    else:
        answer = int(h_/tt)+2
    answer_list += [answer]
for i in answer_list:
    print(int(i))