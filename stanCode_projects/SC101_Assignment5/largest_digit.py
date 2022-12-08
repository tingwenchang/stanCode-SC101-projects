"""
File: largest_digit.py
Name: Tingwen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	TODO: This function recursively prints the biggest digit.
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, numbers that we need to find the biggest digit
	:return: function, helper(n, biggest)
	"""
	if n < 0:
		n = -n
	biggest = 0
	return helper(n, biggest)


def helper(n, biggest):
	"""
	:param n: int, numbers that we need to find the biggest digit
	:param biggest: int, the biggest digit
	:return: int, max(n, biggest); function, helper(n//10, biggest)
	"""
	# base case
	if n//10 == 0:  # unit number
		return max(n, biggest)
	else:
		# 12345
		if n % 10 > biggest:
			biggest = n % 10
		return helper(n//10, biggest)


if __name__ == '__main__':
	main()
