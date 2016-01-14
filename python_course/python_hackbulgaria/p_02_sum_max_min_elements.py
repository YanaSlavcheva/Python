import sys


def sum_min_max_element(arr):
	min_element_value =	min(arr)
	max_element_value = max(arr)
	sum_value = min_element_value + max_element_value
	print(sum_value)


if __name__ == '__main__':
	sum_min_max_element(sys.argv[0])


