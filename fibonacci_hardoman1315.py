def check_prime(num: int) -> bool:
    if num == 2:
        is_prime = True
    elif num <= 1 or num % 2 == 0:
        is_prime = False
    else:
        is_prime = True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
            is_prime = True
    return is_prime


def fibonacci(num: int) -> int:
    is_prime = check_prime(num)
    if is_prime:
        last_digit = num % 10
        previous, current = 0, 1
        for _ in range(last_digit):
            previous, current = current, previous + current
        return previous


nums = []

with open('in_nums.txt', 'r') as input_file:
    for line in input_file:
        nums.append(int(line.strip()))

with open('out_nums.txt', 'w') as output_file:
    for number in nums:
        fib_num = fibonacci(number)
        if fib_num is not None:
            output_file.write(str(fib_num) + '\n')
