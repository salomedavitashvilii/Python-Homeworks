# 1.ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივესი ადაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input-ის მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად: Name: Elene Lastname: Khardava Age: 21
# companies = ["Microsoft", "Google", "Oracle", "Apple"]
# for item in companies:
#  print(item)
import copy
data = []
data1 = []
data2 = []
data3 = []
costumer_info = []
for i in range (3):
    users = input("please enter you name, surname and age: ")
    users = users.split()
    # data.append(users)
    costumer_info.append(users)
# data1.append(costumer_info[0])
# data2.append(costumer_info[1])
# data3.append(costumer_info[2])
data1 = copy.deepcopy(costumer_info[0])
data2 = copy.deepcopy(costumer_info[1])
data3 = copy.deepcopy(costumer_info[2])

# costumer_info.append(data1)
# costumer_info.append(data2)
# costumer_info.append(data3)
print(data3[0])
indx = int(input("please enter the index of user: "))
if (indx==0):
    print(f"Name: {data1[0][0]}; Lastname: {data1[0][1]}; Age: {data1[2]}")
elif (indx==1):
    print(f"Name: {data2[0]}; Lastname: {data2[1]}; Age: {data2[2]}")
elif (indx==2):
    print(f"Name: {data3[0]}; Lastname: {data3[1]}; Age: {data3[2]}")
else:
    print("please enter the valid index (from 0 to 2)")
# print(costumer_info)


# print(data[0][0])



# 2.მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე თუ სახელის ველი არ იქნება ცარიელი, ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია. მისი მონაცემები შეინახე ლისთში. შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ შემოყვანილი ინფორმაცია სიაში შენახულ ინფორმაციას. დაბეჭდე შესაბამისი მესიჯი.
# 3.შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია. მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდა მის შესახებ არსებული ინფორმაცია რეზუმის სახით.
    

    
# def histogram(lst):
#     for num in lst:
#         print('*' * num)

# nums = input("enter the nums: ")

# numbers = [int(x) for x in nums.split()]

# histogram(numbers)


# def histogram(*args):
#     for i in args
#     prin

# def find_longest_word(words):
#     # words = input("please enter you name, surname and age: ")
#     words = words.split()
#     for i in range(len(words)):
#         best = len(words[0])
#         if (len(words[i] > best)):
#             best = words[i]
#             return best


# find_longest_word("salome, eka, maka")


# def find_longest_word(words):
#     words = words.split()
#     best = len(words[0])
#     for i in range(1, len(words)):
#         if len(words[i]) > best:
#             best = len(words[i])
#             longest_word = words[i]
#     return longest_word

# result = find_longest_word("salome, eka, maka")
# print(result)
