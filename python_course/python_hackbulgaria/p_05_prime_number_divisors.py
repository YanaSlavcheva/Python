from p_04_check_prime import check_prime


def prime_number_of_divisors(n):
	# find number of divisors
	number_of_divisors = 0

	for i in range(1, n + 1):
		if n % i == 0:
			number_of_divisors += 1

	# check if the number of divisors is prime
	return check_prime(number_of_divisors)
