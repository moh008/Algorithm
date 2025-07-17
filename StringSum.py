def add_strings(num1: str, num2: str) -> str:
    # Split integer and decimal parts
    if '.' in num1: 
        int_part1, dec_part1 = num1.split('.') 
    else: 
        int_part1, dec_part1 = num1, ''
    
    if '.' in num2: 
        int_part2, dec_part2 = num2.split('.') 
    else: 
        int_part2, dec_part2 = num2, ''

    # Make decimal parts the same length by padding with zeros
    max_dec_len = max(len(dec_part1), len(dec_part2))
    dec_part1 = dec_part1.ljust(max_dec_len, '0')
    dec_part2 = dec_part2.ljust(max_dec_len, '0')

    # Add decimal parts
    dec_sum, carry = add_integer_strings(dec_part1, dec_part2, True)
    # Add integer parts (including carry from decimal addition if any)
    int_sum, _ = add_integer_strings(int_part1, int_part2, False, carry)
    #Trim trailing zeros in decimal part when there's only single '0' at the decimal part, do not right strip '0's
    dec_sum = dec_sum.rstrip('0')

    # Construct final result
    if not dec_sum: 
        return int_sum 
    else: 
        return f"{int_sum}.{dec_sum}"

def add_integer_strings(num1: str, num2: str, is_decimal:bool, carry: int = 0) -> tuple[str, int]:
    result = []
    i, j = len(num1) - 1, len(num2) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            digit1 = int(num1[i])
        else:
            digit1 = 0
        if j >= 0:
            digit2 = int(num2[j])
        else:
            digit2 = 0

        curr_sum = digit1 + digit2 + carry
        carry = curr_sum // 10
        result.append(str(curr_sum % 10))

        i -= 1
        j -= 1
    
    total_sum = ''.join(result[::-1])
    
    if is_decimal:        
        if len(total_sum) > len(num1): #자리수가 넘어가서 carry가 생겼을 경우
            return total_sum[1:], int(total_sum[0])
        else:
            return total_sum, 0 # 자리수가 안넘어가서 그냥 숫자만 더하면 될 경우
    if result: return total_sum, carry
    else:   #더한 값이 존재하지 않을때
        return '0', 0

print(add_strings("3.14", "0.9")) # 4.04
print(add_strings("999.9", "0.1"))  # "1000"
print(add_strings("123456789123456789.98765", "987654321987654321.01235"))  # "1111111111111111111"