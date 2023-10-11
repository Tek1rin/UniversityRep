word = input("Введіть слово: ")

sum = 0

for char in word:
    sum += ord(char)

print("Сума ASCII-кодів символів у слові '{}': {}".format(word, sum))