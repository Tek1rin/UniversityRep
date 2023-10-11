import math

def expression(a, b):
    z = math.sin(a + b) * math.sin(a - b)
    return z

def distance(m, f, count):
    initial_m = m  # Store the initial distance
    while m < initial_m + 50:
        f = m / 100 * f
        m = m + f
        count += 1
    return count


a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

print("Значення виразу z =", expression(a, b))

m = float(input("Введіть початкову дистанцію m: "))
f = int(input("Введіть фроцент збільшення дистанції: "))
count = 1


result = distance(m, f, count)
print("Значення виразу count =", result)