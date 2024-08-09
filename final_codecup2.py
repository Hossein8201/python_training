t = int(input())
answer = [-1]*t
for i in range(t):
    x , y = map(int,input().split())
    answer[i] = max(x,y)
    if(x == y):
        answer[i] += 1
for i in answer:
    print(i)