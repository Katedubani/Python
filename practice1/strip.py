user_string = input()
not_required_text = input()

a = int(user_string[:len(not_required_text) + 1] != not_required_text)
user_string = not_required_text * a + user_string[len(not_required_text) + 1:]

print(user_string)
