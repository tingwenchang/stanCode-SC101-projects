"""
File: boggle.py
Name: Tingwen
----------------------------------------
TODO: This file is going to find the words in dictionary.txt file by using given four rows and only relevant neighbors
	can be included.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: This function is to find the words by using given four rows and only relevant neighbors can be included.
	"""
	List = []  # dealing with case insensitive for every row
	# List = [['f','y','c','l'],['i','o','m','g'],['o','r','i','l'],['h','j','h','u']]
	for i in range(4):
		letters = input(str(i + 1) + " row of letters: ")
		list = []
		for ch in letters:
			if ch.isalpha():
				list += ch.lower()
		List.append(list)
		if len(letters) != 7:
			print("Illegal input")
			break
	start = time.time()   # 輸入完才開始計時，並整理字典
	dictionary = read_dictionary()
	current_s = []
	for i in range(4):
		for j in range(4):
			row = i
			col = j
			used_coordinate = [(i, j)]
			find_word(List, row, col, List[i][j], current_s, dictionary, used_coordinate)
			# used_coordinate.clear()  每次for loop皆重新定義 就不用clear
	print("There are", len(current_s), "word(s) in total.")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(List, r, c, word, current_s, dictionary, used_coordinate):
	"""
	:param List: (list) A list including the alphabets in four given rows
	:param r: (int) The index of rows
	:param c: (int) The index of columns
	:param word: (str) the alphabets in each row and column
	:param current_s: (list) A list including the final words we found
	:param dictionary: (list) A list including words in the dictionary.txt file
	:param used_coordinate: (list) A list including tuples showing each alphabet's coordinator
	"""
	if len(word) >= 4:
		if word in dictionary and word not in current_s:
			print('Found: ', word)
			current_s.append(word)
	for i in range(-1, 2):
		for j in range(-1, 2):
			new_r = r+i
			new_c = c+j
			if (new_r, new_c) not in used_coordinate and 0 <= new_r <= 3 and 0 <= new_c <= 3:
				word += List[new_r][new_c]
				used_coordinate.append((new_r, new_c))
				if has_prefix(word, dictionary):
					find_word(List, new_r, new_c, word, current_s, dictionary, used_coordinate)  # r跟c要更新
				# un-choose需與choose對稱
				used_coordinate.pop()
				word = word[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, "r") as f:
		for words in f:
			words = words.strip()
			if 4 <= len(words) <= 16:   # 設一些條件，減少字典的量以加速搜尋速度
				dictionary.append(words)  # 用+=字典會一個一個字加 ex d+='apple' ->d=['a','p','p','l','e']
	return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (list) A list including words in the dictionary.txt file
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
