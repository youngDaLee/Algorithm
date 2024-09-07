def fizzbuzz(fiznum):
    if (fiznum%3==0 and fiznum%5==0):
        return "FizzBuzz"
    elif (fiznum%3==0):
        return "Fizz"
    elif (fiznum%5==0):
        return "Buzz"
    else:
        return fiznum

li = []
for _ in range(3):
    li.append(input())

fiznum = 0
for i in range(3):
    try:
        num = int(li[i])
        fiznum = (3-i)+num
        break
    except:
        continue

print(fizzbuzz(fiznum))