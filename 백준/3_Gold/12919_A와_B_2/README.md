# [12919. A와 B 2](https://www.acmicpc.net/problem/12919)
## 문제
* 문자열 S를 문자열 T로 바꿈
  * 문자열 뒤에 A 추가
  * 문자열 뒤에 B 추가하고 문자열 뒤집음
* 위 조건으로 S -> T 되는지 확인

## 풀이
* T 문자열 길이만큼 문자열을 만든다 -> 있으면 1, 전체 탐색했는데 없으면 0 => 시간초과
* 탐색 시간을 줄이자 -> s를 t로 만들기
  * 문자열 뒤에 A가 있으면 제거
  * 문자열 앞에 B가 있으면 뒤집고 B 제거
