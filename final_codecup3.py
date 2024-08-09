t = int(input())
answer = [0]*t
for i in range(t):
    n, m, p = map(int,input().split())
    if(p >= n+m):
        answer[i] = n+m+p
    else:
        if(n == m):
            answer[i] = n+m+p
        elif(n > m):
            if(n-m <= p):
                answer[i] = n+m+p
            else:
                answer[i] = p*2 + m*2
        elif(m > n):
            if(m-n <= p):
                answer[i] = n+m+p
            else:
                answer[i] = p*2 + n*2
for i in answer:
    print(i)