def solution(file):
	def numberOfWays(time, distance):
		count = 0
		curr = time // 2
		while curr * (time - curr) > distance:
			count += 1
			curr -= 1
		total = count * 2 if time % 2 == 1 else count * 2 - 1
		return total

	input = []
	with open(file) as f:
		input = [line.split(":")[1] for line in f]
	time = input[0].split()
	time = [int(t) for t in time]
	distance = input[1].split()
	distance = [int(d) for d in distance]
	races = list(zip(time, distance))
	answer = 0
	for t, d in races:
		count = numberOfWays(t, d)
		if count > 0 and answer == 0:
			answer = 1
		answer *= count
		print(f"time: {t}, distance: {d}, count: {count}, answer: {answer}")
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)