def addTwoStrings(num1: str, num2: str):
    if '.' in num1:
        int_part1, dec_part1 = num1.split('.')
    else:
        int_part1, dec_part1 = num1, ''
    if '.' in num2:
        int_part2, dec_part2 = num2.split('.')
    else:
        int_part2, dec_part2 = num2, ''

    max_len_dec = max(len(dec_part1), len(dec_part2))
    dec_part1 = dec_part1.ljust(max_len_dec, '0')
    dec_part2 = dec_part2.ljust(max_len_dec, '0')

    dec_sum, carry = addTwoIntegerStrings(dec_part1, dec_part2, True)
    int_sum, _ = addTwoIntegerStrings(int_part1, int_part2, False, carry)

    dec_sum = dec_sum.rstrip('0')

    if not dec_sum:
        return int_sum
    else:
        return f"{int_sum}.{dec_sum}"
def addTwoIntegerStrings(num1: str, num2: str, isDecimal: bool, carry: int = 0) -> tuple[str, int]:
    i, j = len(num1) - 1, len(num2) - 1
    result = []
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            digit1 = int(num1[i])
        else:
            digit1 = 0
        if j >= 0:
            digit2 = int(num2[j])
        else:
            digit2 = 0
        currSum = digit1 + digit2 + carry
        carry = currSum // 10
        result.append(str(currSum % 10))
        i -= 1
        j -= 1
    total_sum = ''.join(result[::-1])
    if isDecimal:
        if len(total_sum) > len(num1):
            return total_sum[1:], int(total_sum[0])
        else:
            return total_sum, 0
    else:
        if not result:
            return '0', 0
        else:
            return total_sum, 0

print(addTwoStrings("3.14", "0.9"))
print(addTwoStrings("999.9", "0.1"))  # "1000"
print(addTwoStrings("123456789123456789.98765", "987654321987654321.01235"))  # "1111111111111111111"