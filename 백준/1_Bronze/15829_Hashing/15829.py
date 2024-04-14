l = int(input())
s = input()

r = 31

res = 0
for (i, c) in enumerate(s):
    res += (ord(c) - ord('a') + 1) * (r ** i)

print(res % 1234567891)