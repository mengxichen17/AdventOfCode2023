import functools
def solution(file):
	def compare(hand1, hand2):
		if hand1 == hand2: return 0
		type1, type2 = getType(hand1), getType(hand2)
		if type1 > type2:
			return 1
		elif type1 < type2:
			return -1
		else:
			for i in range(len(hand1)):
				card1, card2 = hand1[i], hand2[i]
				if card_order[card1] > card_order[card2]:
					return 1
				elif card_order[card1] < card_order[card2]:
					return -1
			return 0

	def getType(hand):
		count = {}
		count_j = 0
		for card in hand:
			if card == 'J':
				count_j += 1
			else:
				count[card] = count.get(card, 0) + 1
		values = list(count.values())
		values.sort()
		if count_j > 0:
			if values:
				values[-1] += count_j
			else:
				values = [5]
		types = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
		rank = types.index(values)
		if rank == -1: print("Unknown counter of cards")
		return rank

	input = []
	with open(file) as f:
		input = [line.strip().split() for line in f]
	card_order = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
	hand_to_bit_map = {}
	for hand, bit in input:
		hand_to_bit_map[hand] = int(bit)
	hands = list(hand_to_bit_map.keys())
	hands.sort(key=functools.cmp_to_key(compare))
	answer = 0
	for i, hand in enumerate(hands):
		rank = i + 1
		bit = hand_to_bit_map[hand]
		answer += rank * bit
	print(answer)

if __name__ == "__main__":
	prompt = input("Which file to test? Press s for the sample file. ")
	file = "input.txt"
	if prompt == 's' or prompt == 'S':
		file = "sample.txt"
	solution(file)