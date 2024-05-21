result = 0

def dfs(st, s):
    global result

    if st == s:
        result = 1
        return
    if len(st) == len(s):
        return

    if st[-1] == 'A':
        dfs(st[:-1], s)

    if st[0] == 'B':
        dfs(st[1:][::-1], s)



def main():
    s = input()
    t = input()
    if (s == t):
        return 1

    dfs(t, s)
    return result


print(main())