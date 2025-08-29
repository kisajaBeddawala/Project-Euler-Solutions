#Sum Square Difference

#only can use when start 1 and end in range
range = 100

sum_of_squares = range * (range + 1) * (2 * range + 1) // 6     # 1^2 + 2^2 + ... + 100^2
square_of_sum = (range * (range + 1) // 2 ) ** 2                # (1 + 2 + ... + 100)^2

print(square_of_sum - sum_of_squares)