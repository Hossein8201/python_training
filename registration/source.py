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

print(check_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$'))
print(check_registration_rules(saeed='1234567', ab='afj$L12'))