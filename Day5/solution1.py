import math
def solution(file):
	def findDestination(curr_map, source):
		for des, src, increment in curr_map:
			if src <= source < src + increment:
				return des + (source - src)
		return source

	def findLocation(seed):
		soil = findDestination(maps["seed-to-soil"], seed)
		fertilizer = findDestination(maps["soil-to-fertilizer"], soil)
		water = findDestination(maps["fertilizer-to-water"], fertilizer)
		light = findDestination(maps["water-to-light"], water)
		temperature = findDestination(maps["light-to-temperature"], light)
		humidity = findDestination(maps["temperature-to-humidity"], temperature)
		location = findDestination(maps["humidity-to-location"], humidity)
		return location

	input = []
	with open(file) as f:
		input = f.read().split("\n\n")
	seeds = input[0].strip().split(":")[1].split()
	seeds = [int(s) for s in seeds]
	map_names = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", 
				"light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
	maps = {}
	for snippet in input[1:]:
		snippet = snippet.strip().split("\n")
		map_name = snippet[0].split()[0].strip()
		if map_name not in map_names:
			print("Unknown map")
			return
		map_sets_str = snippet[1:]
		map_sets = []
		for map_set in map_sets_str:
			s = map_set.strip().split()
			s = [int(num) for num in s]
			map_sets.append(s)
		maps[map_name] = map_sets
	answer = math.inf
	for seed in seeds:
		location = findLocation(seed)
		answer = min(answer, location)
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)