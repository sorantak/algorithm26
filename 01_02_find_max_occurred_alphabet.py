def find_max_occurred_alphabet(string):
    # str.isalpha(): 문자열인지 확인
    # ord(): 문자열을 ASCII 코드로 변환
    # chr(): ASCII 코드를 문자열로 변환
    # 알파벳 배열을 미리만든다..
    # 배열의 시작점은 'a'
    alphabet_array = [0] * 26
    for i in string:
        if str.isalpha(i):
            index = ord(i) - ord('a')
            alphabet_array[index] += 1
    print(alphabet_array)

    max_occurred_index = 0
    for i in range(len(alphabet_array)):
        if alphabet_array[i] > alphabet_array[max_occurred_index]:
            max_occurred_index = i
    print(max_occurred_index)

    return chr(max_occurred_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# 풀이방식: 해시테이블 (인덱스 지정 0은 a, 1은 b ...)
# 공간복잡도: O(1)
