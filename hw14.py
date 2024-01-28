# 1.დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.
from collections import Counter
import csv

with open('article.txt', 'r') as f:
    text = f.read()

words = text.lower().split()
word_counts = Counter(words)
second_frequent = word_counts.most_common(2)[1][0]

print(second_frequent)


# 2. names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('names.txt', 'w') as txt_file:
        for row in csv_reader:
            txt_file.write(','.join(row) + '\n')
