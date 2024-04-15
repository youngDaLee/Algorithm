n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    count = 0
    while n % 5 != 0:
        n -= 3
        count += 1
        if n < 0:
            print(-1)
            break
    if n >= 0:
        print(count + n // 5)