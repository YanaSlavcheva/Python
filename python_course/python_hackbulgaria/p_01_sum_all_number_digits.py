import math


def sum_of_digits(n):
    # 102 % 10 = 2
    # 102 // 10 = 10
	n = int(math.fabs(n))
	our_sum = 0

	while n != 0:
		our_sum += n % 10
		n = n // 10
	return our_sum


