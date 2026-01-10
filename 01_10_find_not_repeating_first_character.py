def find_not_repeating_first_character(string):
    # 지난번처럼 아스키 배열을 쓰려다가 정렬이 되면 안되기 때문에 딕셔너리 사용함
    string_dict = {}
    result_character = "_"

    # 값이 없으면 0으로 초기화한 후 1을 더함
    for el in string:
        string_dict[el] = string_dict.get(el, 0) + 1

    for key, value in string_dict.items():
        if value == 1:
            return key
    return result_character


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

# 시간복잡도: O(N)
