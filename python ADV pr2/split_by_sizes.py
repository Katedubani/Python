def split_by_sizes(iterable, split_sizes):
	it = iter(iterable)
	sizes = iter(split_sizes)
	tmp = []
	current_size = next(sizes)
	for x in it:
		tmp.append(x)

		if len(tmp) == current_size:
			yield tmp
			tmp = []

			try:
				current_size = next(sizes)
			except StopIteration:
				return

	if tmp:
		yield tmp


def main():
	print(*split_by_sizes(range(9), split_sizes=[3, 4, 3]))


main()