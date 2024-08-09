# 
list_days = []
hour = int(input())
min_hour , max_hour = map(int,input().split())

def hour_in_day(remain_hour,number):
    if(remain_hour < 0):
        return -1
    elif(remain_hour == 0):
        return number
    for i in range(min_hour,max_hour+1):
        print(remain_hour-i,i)
        return hour_in_day(remain_hour-i,number+1)

list_days += [hour_in_day(hour , 0)]
sorted(list_days)
print(list_days[0])