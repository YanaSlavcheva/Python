from math import sqrt


def check_prime(n):
	is_prime = True
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			is_prime = False

	return is_prime
