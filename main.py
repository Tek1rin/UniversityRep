a = int(input ("Введіть а: "))

while (a < 0):

    a = int(input ("Введіть а: "))

b = int(input ("Введіть b: "))

while (b < 0):

    b = int(input ("Введіть ще раз b: "))

if a < b:

    r = 3 * a / b + 1

elif a == b:

    r = -5

else:

    r = a * b + 21

print("Результат обчислення виразу: " , r)