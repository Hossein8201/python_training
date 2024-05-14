# https://quera.org/problemset/157645?tab=description
f_r , l_r = map(int,input().split())
year = int(input())
for i in range(year):
    f_r = f_r*2 - l_r
print(f_r)