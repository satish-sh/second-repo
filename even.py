a = int(input())
list_A  = []
if 10 < a < 40:
    for i in range(a):
        if i % 2 == 0:
            list_A.append(i)

print(list_A)