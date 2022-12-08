"""
File: coin_flip_runs.py
Name: Ting-Wen (Wenny)
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program is to use random number to see whether the coin is head or not and calculate how many runs to end
	the flip game. We will set a False/True to not store the repeated value.
	"""
	print('Let\'s flip a coin!')
	number = int(input('Number of runs: '))
	# print(result(number,r))
	run = 0
	record = ''
	flip1 = r.choice([1, 2])
	if flip1 == 1:
		record += 'H'
	else:
		record += 'D'
	is_in_record = False

	while True:
		flip2 = r.choice([1, 2])
		if flip2 == 1:
			record += 'H'
		else:
			record += 'D'
		if flip1 == flip2:
			if not is_in_record:
				run += 1
				is_in_record = True
		else:
			is_in_record = False
		if run == number:
			break
		flip1 = flip2
	print(record)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
