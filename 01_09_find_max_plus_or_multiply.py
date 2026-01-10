def find_max_plus_or_multiply(array):
    total = array[0]
    for el in array[1:]:
        plus = total + el
        multiply = total * el
        total = plus if plus > multiply else multiply
    return total


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", result([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", result([1, 1, 1, 3, 3, 2, 5]))

# 시간복잡도: O(N)
# 공간복잡도: O(1)
# 이것도 그리디연산법
