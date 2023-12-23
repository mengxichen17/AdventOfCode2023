import math
def solution(file):
	def numberOfWays(time, distance):
		'''
			suppose x=pressing time, y=moving time, then we have
			x + y = time
			xy > distance
			x(time - x) > distance
			-x^2 + time*x - distance > 0
			solve the minimum x and get corresponding y
		'''
		a, b, c = -1, time, -distance
		x1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
		x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
		x1, x2 = min(x1, x2), max(x1, x2)
		x1 = math.ceil(x1)
		x2 = math.floor(x2)
		return x2 - x1 + 1

	input = []
	with open(file) as f:
		input = [line.split(":")[1] for line in f]
	time = int("".join(input[0].split()))
	distance = int("".join(input[1].split()))
	print(time, distance)
	answer = numberOfWays(time, distance)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)