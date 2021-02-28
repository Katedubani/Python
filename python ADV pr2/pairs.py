def pairs(iterable):
	it = iter(iterable)
	try:
		for _ in iterable:
			yield (next(it), next(it))
	except StopIteration:
		return


def main():
	print(*pairs(['a', 'b', 'c', 'd']))


main()
		