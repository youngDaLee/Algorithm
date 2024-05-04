def win_ttt(ttt, ox):
    # 가로
    for t in ttt:
        if (ox == t[0] == t[1] == t[2]): return True

    # 세로
    for i in range(3):
        if (ox == ttt[0][i] == ttt[1][i] == ttt[2][i]): return True

    # 대각선
    if (ox == ttt[0][0] == ttt[1][1] == ttt[2][2] or
        ox == ttt[0][2] == ttt[1][1] == ttt[2][0]):
        return True
    return False


def tictackto(ttt):
    x_len = 0
    o_len = 0
    for tt in ttt:
        for t in tt:
            if t == 'X' : x_len += 1
            elif t=='O': o_len += 1

    # X, O가 한개보다 더 차이나는 경우 없음
    if abs(x_len - o_len) > 1 or x_len < o_len:
        return False

    win_x = win_ttt(ttt, 'X')
    win_o = win_ttt(ttt, 'O')

    # 둘 다 이기는 경우 없음
    if win_x and win_o: return False

    # X가 이겼으면서 한개 차이나면 True
    if win_x and x_len - o_len == 1 : return True
    elif win_x: return False

    # O가 이겼으면서 개수같으면 True
    if win_o and x_len == o_len: return True
    elif win_o: return False

    # 그 외에 X가 5개, O가 4개면 True(비긴경우)
    if o_len==4 and x_len==5: return True

    # 그 외에는 false
    return False


def main():
    while True:
        line = input()
        if (line == 'end'):
            break

        ttt = []
        for i in range(3):
            ttt.append(line[i*3:(i+1)*3])

        if tictackto(ttt):
            print('valid')
        else:
            print('invalid')


main()