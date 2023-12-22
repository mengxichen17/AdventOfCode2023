import collections
def solution():
	def isPartNumber(i, j):
		surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		list_of_symbols = set()
		for x, y in surrounding:
			if 0 <= x + i < rows and 0 <= y + j < cols and not input[x+i][y+j].isalnum() and input[x+i][y+j] != '.':
				list_of_symbols.add((x+i, y+j))
		return list_of_symbols

	input = []
	with open('input.txt') as f:
		input = [list(line.strip()) for line in f]
	rows, cols = len(input), len(input[0])
	gears = collections.defaultdict(list) # key - location of special symbol; value - list of numbers using this special symbol
	answer = 0
	curr_num = ''
	adj_symbols = set()
	for i in range(rows):
		for j in range(cols):
			char = input[i][j]
			if char.isdigit():
				curr_num += char
				adj_symbols.update(isPartNumber(i, j))
			if j == cols - 1 or not char.isdigit():
				if curr_num and adj_symbols:
					# print(curr_num, adj_symbols)
					for a, b in adj_symbols:
						gears[(a, b)].append(int(curr_num))
				curr_num = ''
				adj_symbols = set()
	# print(gears)
	for key, lst_num in gears.items():
		if len(lst_num) == 2:
			answer += lst_num[0] * lst_num[1]

	print(answer)

if __name__ == "__main__":
	solution()