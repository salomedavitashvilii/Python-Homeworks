# 1.მომხმარებელს შემოაყვანინე ინფორმაცია და დათვალე რამდენი რიცხვი, ანბანის ასო და სხვა სიმბოლოა მოცემული წინადადებაში. შედეგი დაბეჭდე. გამოიყენე for ციკლი, is alpha და is digit ფუნქციები.

data = input("enter some data here... ")
letter = 0
num = 0
other = 0
for char in data:
    if char.isalpha() == True:
        letter += 1
    elif char.isdigit() == True:
        num += 1
    else:
        other += 1
print(f"there are {letter} letter, {num} digits and {other} other symbols in the given string")


# 2.მომხმარებელს შეაყვანინე ორი წინადადება და მათგან შეადგინე მესამე შემდეგ წესებზე დაყრდნობით. შექმნილი წინადადება უნდა იწყებოდეს პირველი წინადადების პირველი სიმბოლოთი, რომელსაც ჯერ მოჰყვება მეორე წინადადების 
# ბოლო სიმბოლო, შემდეგ კი პირველი წინადადების მეორე სიმბოლო და მეორე წინადადების ბოლოდან მეორე სიმბოლო.

first = input("enter the first sentence here: ") 
second = input("enter the second sentence here: ")   
"""
for i in first:
    for j in second:
        mesame =   ამას ციკლით ვაკეთებდი მარა ან ძალიან მარტივად კეთდება ან პირობა ვერ გავიგე 
"""
mesame = first[0] + second[-1] + first[1] + second[-2]
print(mesame)



# 3.მომხმარებელს შეაყვანინე ორი წინადადება და შეამოწმე, პირველ წინადადებაში არსებული ყველა სიმბოლო თუ შედის მეორე წინადადებაში და პირიქით, მეორე წინადადებაში შემავალი ყველა სიმბოლო თუ შედის პირველ წინადადებაში. თუ ეს ორი პირობა დაკმაყოფილდა, დაბეჭდე:
# „Strings are balanced!“ თუ რომელიმე პირობა დაირღვა, დაბეჭდე: „Strings are not balanced!“


first = input("enter the first sentence here: ") 
second = input("enter the second sentence here: ") 
balanced = True  
for i in first:
    if (i not in second):
        balanced = False
        break
for j in second:
    if (j not in first):
        balanced = False
        break
if balanced:
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")

