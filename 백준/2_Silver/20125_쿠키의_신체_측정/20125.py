def find_heart(cookie, n):
    # 행의 번호 x
    for x in range(n):
        # 열의 번호 y
        for y in range(n):
            if (cookie[x][y] == '*'):
                # index 0부터 시작하니까 +1, 심장은 아래 행에 위치하므로 +1
                return x+2, y+1


def find_lenght(cookie,x,y,dx,dy,cnt):
    if((x+dx < 0 or x+dx == len(cookie)) or (y+dy < 0 or y+dy == len(cookie))):
        return cnt
    if(cookie[x+dx][y+dy] == '_'):
        return cnt
    cnt+=1
    return find_lenght(cookie, x+dx, y+dy, dx, dy, cnt)

def main():
    n = int(input())
    cookie = []
    for _ in range(n):
        cookie.append(input())

    x, y = find_heart(cookie, n)
    left_arm = find_lenght(cookie,x-1,y-1,0,-1,0)
    right_arm = find_lenght(cookie,x-1,y-1,0,1,0)
    waist = find_lenght(cookie,x-1,y-1,1,0,0)
    left_leg = find_lenght(cookie,x-1+waist,y-2,1,0,0)
    right_leg = find_lenght(cookie,x-1+waist,y,1,0,0)

    print(x, y)
    print(left_arm,right_arm,waist,left_leg,right_leg)


main()