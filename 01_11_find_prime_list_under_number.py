input = 20


# 1트
def find_prime_list_under_number1(number):
    prime_list = []
    new_number = number
    while True:
        if new_number == 1:
            break

        new_divider = 2
        has_divisor = False
        while True:
            if new_divider == new_number:
                break

            if new_number % new_divider == 0:
                has_divisor = True
                break
            new_divider += 1
        if not has_divisor:
            prime_list.append(new_number)
        new_number -= 1
    return prime_list


# 2트
# for-else 구문 처음봄..
def find_prime_list_under_number2(number):
    prime_list = []
    for i in range(2, number + 1):
        # for j in range(2, i):
        # for j in range(2, int(i**0.5) + 1):   # 이렇게 제곱근을 사용하면 시간이 줄어들 것
        for j in prime_list:  # 애초에 소수들로만 나눠도 된다고 함
            # if i % j == 0:
            if j * j < i and i % j == 0:    # j * j도 제곱근의 개념임
                break
        else:
            prime_list.append(i)
    return prime_list


result = find_prime_list_under_number2(input)
print(result)
