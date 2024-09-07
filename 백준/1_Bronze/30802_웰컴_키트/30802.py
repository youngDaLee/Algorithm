n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

t_res = 0
for s in size:
    num = s//t
    if s%t!=0: num += 1
    t_res += num

print(t_res)
print(n//p,n%p)
