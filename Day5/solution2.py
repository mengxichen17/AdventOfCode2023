import math, bisect
def solution(file):
	def findSource(curr_map, dest):
		ind = bisect.bisect(curr_map, [dest, math.inf, math.inf])
		ind -= 1
		des, src, increment = curr_map[ind]
		if des <= dest < des + increment:
			return src + (dest - des)
		return dest

	def findSeed(location):
		humidity = findSource(maps["humidity-to-location"], location)
		temperature = findSource(maps["temperature-to-humidity"], humidity)
		light = findSource(maps["light-to-temperature"], temperature)
		water = findSource(maps["water-to-light"], light)
		fertilizer = findSource(maps["fertilizer-to-water"], water)
		soil = findSource(maps["soil-to-fertilizer"], fertilizer)
		seed = findSource(maps["seed-to-soil"], soil)
		return seed

	input = []
	with open(file) as f:
		input = f.read().split("\n\n")
	seeds = input[0].strip().split(":")[1].split()
	seeds = [int(s) for s in seeds]
	new_seeds = []
	for i in range(0, len(seeds), 2):
		new_seeds.append(seeds[i:i+2])
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
			bisect.insort(map_sets, s)
		maps[map_name] = map_sets
	new_seeds.sort()
	print(new_seeds)
	location = 0
	while True:
		seed = findSeed(location)
		ind = bisect.bisect(new_seeds, [seed, math.inf]) - 1
		print(f"location: {location}, seed: {seed}, ind: {ind}")
		if ind >=0 and new_seeds[ind][0] <= seed < new_seeds[ind][0] + new_seeds[ind][1]:
			print(location)
			break
		location += 1

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)