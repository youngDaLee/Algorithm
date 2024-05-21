## 시간초과
def addA(s):
    return s+'A'


def addB(s):
    s = s+'B'
    s = list(s)
    s.reverse()
    return ''.join(s)


def main():
    s = input()
    t = input()
    if (s == t):
        return 1

    str_list = [s]
    while True:
        if (len(str_list[0]) == len(t)):
            for st in str_list:
                if st == t:
                    return 1
            return 0

        new_set = set()
        for st in str_list:
            new_set.add(addA(st))
            new_set.add(addB(st))

        str_list = list(new_set)

print(main())