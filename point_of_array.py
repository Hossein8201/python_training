n, m, q = map(int,input().split())
list_answer_q = []
list_number = input().split()
list_point = [[]]
for i in range(m):
    list_point.append(input().split())
for j in range(q):
    index_in, index_out = map(int,input().split())
    dicti_count = {}
    for i in range(index_in-1, index_out):
        if(int(list_number[i]) in dicti_count):
            dicti_count[int(list_number[i])] += 1
        else:
            dicti_count.update({int(list_number[i]) : 1})
    list_answer_q += [0]
    for i in dicti_count:
        if((dicti_count[i] >= int(list_point[i][0])) & (dicti_count[i] <= int(list_point[i][1]))):
            list_answer_q[j] += 1

for i in list_answer_q:
    print(i,end=" ")
