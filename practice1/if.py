num = int(input())

result_no = int(bool(1000 // num))
result_yes = int(not bool(result_no))


print('No' * result_no + 'Yes' * result_yes)