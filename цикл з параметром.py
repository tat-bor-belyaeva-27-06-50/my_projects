sum = 0
addition = 1

for i in range(1, 65):
    sum = sum + addition
    addition = addition * 2

print("Кількість зерна =", sum)