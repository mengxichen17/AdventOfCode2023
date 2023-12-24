from math import lcm, gcd
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
	
	curr = [node for node in network.keys() if node.endswith('A')]
	steps = []
	for node in curr:
		i = 0
		step = 0
		while not node.endswith('Z'):
			direction = instruction[i]
			if direction == 'L':
				next_node = network[node][0]
			else:
				next_node = network[node][1]
			node = next_node
			i = (i + 1) % len(instruction)
			step += 1
		steps.append(step)
	answer = 1
	for i in steps:
	    answer = answer*i // gcd(answer, i)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)