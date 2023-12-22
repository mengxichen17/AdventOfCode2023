# from string import punctuation
def solution():
	def isPartNumber(i, j):
		surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for x, y in surrounding:
			if 0 <= x + i < rows and 0 <= y + j < cols and not input[x+i][y+j].isalnum() and input[x+i][y+j] != '.':
				return True
		return False

	input = []
	with open('input1.txt') as f:
		input = [list(line.strip()) for line in f]
	rows, cols = len(input), len(input[0])
	answer = 0
	curr_num = ''
	part_num = False 
	for i in range(rows):
		for j in range(cols):
			char = input[i][j]
			if char.isdigit():
				curr_num += char
				if not part_num:
					part_num = isPartNumber(i, j)
			if j == cols - 1 or not char.isdigit():
				if curr_num and part_num:
					# print(curr_num)
					answer += int(curr_num)
				curr_num = ''
				part_num = False

	print(answer)

if __name__ == "__main__":
	solution()