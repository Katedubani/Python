word, count = input().split()
count = int(count)


mid_of_the_word = len(word) // 2
left_part = (count - 1) // 2
count -= left_part

part_before_changes = word[(mid_of_the_word - left_part) : (mid_of_the_word + count)]

print(word[:mid_of_the_word - left_part] + part_before_changes[::-1] + word[mid_of_the_word + count:])