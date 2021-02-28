def fill_pairs(iterable, fill_element):
	is_odd = False
	if len(iterable) % 2 == 0:
		is_odd = True

	it = iter(iterable)	
	try:
		for _ in iterable:
			a = next(it)
			b = next(it)
			yield a, b
	except StopIteration:
		if is_odd:
			return
		else:
			b = fill_element
			yield a, b


def main():
	print(*fill_pairs('abcd', fill_element=None))


main()