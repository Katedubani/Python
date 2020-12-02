x, y = input().split()
x, y = float(x), float(y)

first_line = (x * (y**(1/2))) / (((x**2) + 0.8 * x * y)**(1/2))
second_line = (((x**2) - 0.8 * x * y)**(1/2))

print(first_line / second_line)