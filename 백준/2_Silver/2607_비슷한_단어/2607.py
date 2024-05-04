def main():
    n = int(input())
    result = 0

    first_word_set = {}
    first_word_len = 0

    for i in range(n):
        word = input()
        if i == 0:
            first_word_set = set(list(word))
            first_word_len = len(word)
        else:
            if abs(first_word_len - len(word)) > 1 or len((first_word_set - set(list(word)))|(set(list(word))-first_word_set)) > 1:
                # 다른 문자 2개 이상이면 continue
                continue
            if abs(first_word_len - len(word)) == 1 and len((first_word_set - set(list(word)))|(set(list(word))-first_word_set)) == 1:
                # 다른 문자가 1개 추가되었으면 continue
                continue

            result += 1

    print(result)

main()