# https://quera.org/problemset/190993?tab=description
number , question , length = map(int,input().split())
list_answer = []
list_code = {}
for i in range(number):
    key , value = input().split()
    list_code.update({key : value})
for i in range(question):
    key = input()
    if(key in list_code.keys()):
        list_answer += [list_code[key]]
    else:
        list_answer += ['Unknown']
for i in list_answer:
    print(i)
