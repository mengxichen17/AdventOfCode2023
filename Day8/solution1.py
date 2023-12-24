def solution(file):
	input = []
	with open(file) as f:
		input = f.read().split("\n\n")
	instruction = input[0]
	node_map = input[1].strip().split('\n')
	network = {}
	for line in node_map:
		start, parethesis = line.split('=')[0].strip(), line.split('=')[1].strip()
		dest = parethesis.strip('(').strip(')').split(", ")
		dest = [d.strip() for d in dest]
		network[start] = dest
	answer = 0
	i = 0
	curr = 'AAA'
	while curr != 'ZZZ':
		direction = instruction[i]
		if direction == 'L':
			next_node = network[curr][0]
		else:
			next_node = network[curr][1]
		curr = next_node
		i = (i + 1) % len(instruction)
		answer += 1
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)