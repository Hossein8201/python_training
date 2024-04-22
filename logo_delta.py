# https://quera.org/problemset/220669?tab=description  
list=''
n=int(input())
list=(n-1)*'.'+'D'+(n-1)*'.'
print(list)
for i in range(1,n-1):
    list=(n-i-1)*'.'+'D'+(2*i-1)*'.'+'D'+(n-i-1)*'.'
    print(list)
list=''
for i in range(n):
    list+='D.'
print(list[0:2*n-1])
