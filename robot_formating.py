# https://quera.org/problemset/235087?tab=description
length = int(input())
list_orders = list(input())
robot_direction = 'R'
list_rotate = 'RULDRULD'
robot_format = ''
for i in list_orders:
    if (i == robot_direction):
        robot_format += 'F'
    else:
        j = list_rotate.index(robot_direction)
        while(list_rotate[j] != i):
            j += 1
            robot_format += 'R'
        robot_format += 'F'
        robot_direction = i
print(robot_format)