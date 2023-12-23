def Solution(file):
	def powerOfCubes(result):
		grabs = result.strip().split(";")
		bag = {"red": 0, "green": 0, "blue": 0}
		for grab in grabs:
			items = grab.strip().split(",")
			for item in items:
				number, color = item.strip().split(" ")
				number = int(number.strip())
				color = color.strip()
				if bag[color] < number:
					bag[color] = number
		power = 1
		for value in bag.values():
			power *= value
		return power

	input = []
	with open(file) as f:
		input = [line.strip() for line in f]

	# bag = {"red": 12, "green": 13, "blue": 14}
	answer = 0
	for line in input:
		game, result = line.split(":")
		# game_id = int(game.strip().split(" ")[1])
		answer += powerOfCubes(result)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	Solution(file)