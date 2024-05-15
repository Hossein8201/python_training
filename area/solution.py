def get_func(ls):
    import math
    answer = []
    for i in ls:
        if i=='square':
            def area_square(x):
                return x*x
            answer += [area_square]
        elif i=='circle':
            def area_circle(x):
                return math.pi*x*x
            answer += [area_circle]
        elif i=='rectangle':
            def area_rectangle(x,y):
                return x*y
            answer += [area_rectangle]
        elif i=='triangle':
            def area_triangle(x,h):
                return x*h*(0.5)
            answer += [area_triangle]
    return answer

'''
ls = get_func(['square', 'circle', 'rectangle', 'triangle'])
print(ls)

print(ls[0](1))      # 1
print(ls[1](2))      # 12.566370614359172
print(ls[2](2, 4))   # 8
print(ls[3](4, 5))   # 10.0  
'''
