def solution(file):
	def checkMatch(winning, have):
		winning = set(winning)
		point = 0
		for num in have:
			if num in winning:
				point += 1
		return point

	input = []
	with open(file) as f:
		input = [line.strip().split(":")[1].strip() for line in f]
	cards = [1] * len(input)
	for i, card in enumerate(input):
		winning, have = card.split("|")
		winning = winning.strip().split()
		have = have.strip().split()
		match = checkMatch(winning, have)
		for j in range(1, match + 1):
			cards[i+j] += cards[i]
	answer = sum(cards)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)