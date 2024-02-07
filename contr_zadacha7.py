def count_sum_digits(num_str):
    res = 0
    for dig in num_str:
        res += int(dig)
    return res


numbers = input().split()

max_nums = []
max_sum = -1

for num in numbers:
    sum_dig = count_sum_digits(num)
    if sum_dig > max_sum:
        max_sum = sum_dig
        max_nums = [num]
    elif sum_dig == max_sum:
        max_nums.append(num)

print(*max_nums)
