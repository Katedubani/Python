def compose_map(func_collection, iterable):
	it = iter(iterable)
	func = [*iter(func_collection)][::-1]

	for i in it:
		res = i
		for f in func:
			res = f(res)
		yield res


def main():
	print(*compose_map([lambda x: x ** 2, lambda x: 2 ** x], [0, 2, 5]))


main()
