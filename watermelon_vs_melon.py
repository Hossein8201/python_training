# https://quera.org/problemset/235095?tab=description
watermelon_number = int(input())
melon_number = int(input())
if(melon_number % 2 == 0):
    if((melon_number >= 2) or (watermelon_number % 2 == 0)):
        print("YES")
    elif((melon_number == 0) & (watermelon_number % 2 == 1)):
        print("NO") 
elif(melon_number % 2 == 1):
    print("NO")