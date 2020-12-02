user_string = input()
mid_of_the_str = len(user_string) // 2 

user_string = user_string[mid_of_the_str:] + user_string[:mid_of_the_str]

print(user_string)