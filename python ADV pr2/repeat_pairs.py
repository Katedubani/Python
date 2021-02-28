def repeat_pairs(iterable):
	it = iter(iterable)
	a = next(it)
	try:
		for _ in iterable:
			b = next(it)
			yield a, b
			a = b
	except StopIteration:
		return


def main():
	print(*repeat_pairs('abcde'))


main()