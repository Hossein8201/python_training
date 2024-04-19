def check_registration_rules(**kwargs):
    answer=[]
    c=0
    for i in kwargs.keys():
        if((i!='quera') & (i!='codecup') & (len(i)>=4)):
            b=len(kwargs[i])
            if(b>=6):
                for j in range(b):
                    if(kwargs[i][j] not in '0123456789'):
                        c=1
                        break
                if(c):  answer.append(i)
    return answer