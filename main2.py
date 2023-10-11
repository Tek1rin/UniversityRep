a = 1
b = 1
c = 0
sum = 0

for x in range(0, 25, 1):
  c = b
  b = b + a
  a = c
  if x > 0:
    sum = sum + b
    print(b)  
print(f'Сума членів ряду Фібоначчі з 5-го по 25-й:', sum) 