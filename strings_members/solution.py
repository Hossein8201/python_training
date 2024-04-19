def calculator(n, m, li):
    result=0
    answer=0
    list=[]
    for i in range(n):
        if(i%m==m-1) | (i==n-1):   
            result+=li[i]
            list+=[result]
            result=0
        else:
            result+=li[i]
    for j in range(len(list)):
        if(j%2==0):  
            answer+=list[j]   
        else:   
            answer-=list[j]

    return answer

print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
