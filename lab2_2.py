from mod import distance

print("Завдання 2")

m = float(input("Введіть початкову дистанцію m: "))
f = int(input("Введіть фроцент збільшення дистанції: "))
count = 1


result = distance(m, f, count)
print("Значення виразу count =", result)