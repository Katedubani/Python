def split_by_size(iterable, size):
	it = iter(iterable)

	tmp = []
	for x in it:
		tmp.append(x)

		if len(tmp) == size:
			yield tmp
			tmp = []

	if tmp:
		yield tmp


def main():
	print(*split_by_size(range(9), size=5))


main()