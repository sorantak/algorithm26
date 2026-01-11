input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    turn_to_zero_count = turn_to_standard(string, '0')
    turn_to_one_count = turn_to_standard(string, '1')

    return turn_to_one_count if turn_to_zero_count > turn_to_one_count else turn_to_zero_count


def turn_to_standard(array, standard):
    count = 0
    if array[0] != standard:
        count += 1

    for i in range(1, len(array)):
        if array[i] != standard and array[i] != array[i - 1]:
            count += 1
    return count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 그리디 연산
