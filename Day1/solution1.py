def Solution():
	def extractNumber(string):
		first_char, last_char = '', ''
		for s in string:
			if s.isdigit():
				if not first_char:
					first_char = s
				last_char = s
		return int(first_char + last_char)

	input = []
	with open("input.txt") as f:
		input = [line.strip() for line in f]
	answer = 0
	for string in input:
		answer += extractNumber(string)
	print(answer)

if __name__ == "__main__":
	Solution()