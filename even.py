user_input = int(input())

list_A  = []
for i in range(user_input):
    if i % 2 == 0:
        list_A.append(i)

print(list_A)
