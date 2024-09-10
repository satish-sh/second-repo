user_input = int(input())

for i in range(user_input):
    if i % 2 == 0:
        list_A.append(i)

print(list_A)

list_B = []
for i in range(user_input):
    if i%2 != 0:
        list_B.append(i)
print(list_B)

