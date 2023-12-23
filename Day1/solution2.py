import re
def Solution(file):
	def extractWordNumber(substring):
		# return the list of spelled number (in string) in a string, if any; if none, return empty list
		if not substring: return []
		words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
		numbers = [None] * len(substring)
		number_in_word = ''
		for word in words:
			found_index = [m.start() for m in re.finditer(word, substring)]
			for i in found_index:
				numbers[i] = words[word]
		found = [number for number in numbers if number]
		return found

	def extractNumber(string):
		numbers = []
		substring = ''
		for s in string:
			if s.isdigit():
				numbers += extractWordNumber(substring)
				numbers.append(s)
				substring = ''
			else:
				substring += s
		numbers += extractWordNumber(substring)
		return int(numbers[0] + numbers[-1])

	input = []
	with open(file) as f:
		input = [line.strip() for line in f]
	answer = 0
	for string in input:
		answer += extractNumber(string)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample2.txt"
	Solution(file)