def main():
    n = int(input())
    result = 0

    first_word = ''

    for i in range(n):
        word = input()
        if i == 0:
            first_word = word
        else:
            first_word_list = list(first_word)
            word_list = list(word)

            w_set = []
            for i in range(len(word)):
                if word[i] not in word_list:
                    w_set.append(word[i])
                else:
                    word_list.pop(i)

            for i in ra
            

            f_set = [x for x in first_word if x not in list(word)]
            print(w_set, f_set)
            if ((len(w_set) + len(f_set)) > 1):
                # 다른 문자 2개 이상이면 continue
                continue

            result += 1


    print(result)

main()