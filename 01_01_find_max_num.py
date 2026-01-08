def find_max_num(array):
    # max_num을 0으로 설정하면 모든 요소가 음수일때 문제가 됨
    max_num = array[0]
    for el in array:
        if el > max_num:
            max_num = el
    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# 풀이방식: 선형탐색 (Linear Search)
# 시간복잡도: O(n)
