t = int(input())
answer = ["NO"]* t
for i in range(t):
    numbers = list(map(int,input().split()))
    rank =  list(map(int,input().split()))
    solved =  list(map(int,input().split()))
    level = int(input())
    for j in range(6):
        if(numbers[j] >= 7):
            if(solved[j] >= 2):
                if(rank[j] == 1):
                    answer[i] = "YES"
                    break
    if(level <= 40):
        answer[i] = "YES"
for i in range(t):
    print(answer[i])