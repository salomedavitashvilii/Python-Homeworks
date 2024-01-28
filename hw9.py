# 1. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
import random
list = []
for i in range (1,11):
    rand = random.randint(1,100)
    list.append(rand)
    list.sort()
print (list)

# 2. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).

import random
list = []
for i in range (1,11):
    rand = random.randint(1,100)
    list.append(rand)
    sorted_list = sorted(list, reverse=True)
print (sorted_list)

# 3. დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი), საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.

import random

my_list = []
for i in range (1,11):
    rand = random.randint(1,100)
    my_list.append(rand)

def bubble_sort(List):
    for i in range(len(List)-1):
        sortedFlag = True
        for j in range(len(List)-i-1):
            if List[j] < List[j+1]:
                changeElement = List[j]
                List[j] = List[j+1]
                List[j+1] = changeElement
                sortedFlag = False
        if sortedFlag:
            break
    return List

def selection_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

print(my_list)
print(bubble_sort(my_list.copy()))
print(selection_sort(my_list.copy()))



