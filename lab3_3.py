sentence = input("Введіть речення: ")

words = sentence.split()

words_with_three_e = []

for word in words:
    count_e = word.count("е") 
    if count_e == 3:
        words_with_three_e.append(word)

if len(words_with_three_e) > 0:
    print("Слова із трьома 'е':")
    for word in words_with_three_e:
        print(word)
else:
    print("У введеному реченні немає слів із трьома 'е'.")