def solution(file):
	def checkPoints(winning, have):
		winning = set(winning)
		point = 0
		for num in have:
			if num in winning:
				if point == 0:
					point = 1
				else:
					point *= 2
		return point

	input = []
	with open(file) as f:
		input = [line.strip().split(":")[1].strip() for line in f]
	answer = 0
	for card in input:
		winning, have = card.split("|")
		winning = winning.strip().split()
		have = have.strip().split()
		answer += checkPoints(winning, have)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)