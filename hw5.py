# 1.ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე ინფორმაცია საკუთარი სახელის, გვარის და ასაკის შესახებ. თითოეული მომხმარებლის ინფორმაცია შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივესი ადაამატე საერთო ცალრიელ სიას სახელად consumer_info. Input-ის მეშვეობით მომხმარებლის ინდექსის შეყვანის შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ მომხმარებელზე ინფორმაცია შემდეგნაირად: Name: Elene Lastname: Khardava Age: 21

# import copy
# data = []
# data1 = []
# data2 = []
# data3 = []
# costumer_info = []
# for i in range (3):
#     users = input("please enter you name, surname and age: ")
#     users = users.split()
#     costumer_info.append(users)
# data1 = copy.deepcopy(costumer_info[0])
# data2 = copy.deepcopy(costumer_info[1])
# data3 = copy.deepcopy(costumer_info[2])
# # costumer_info = data1 + data2 + data3 #ასეც შეგვეძლო ეს
# indx = int(input("please enter the index of user: "))
# if (indx==0):
#     print(f"Name: {data1[0][0]}; Lastname: {data1[0][1]}; Age: {data1[2]}")
# elif (indx==1):
#     print(f"Name: {data2[0]}; Lastname: {data2[1]}; Age: {data2[2]}")
# elif (indx==2):
#     print(f"Name: {data3[0]}; Lastname: {data3[1]}; Age: {data3[2]}")
# else:
#     print("please enter the valid index (from 0 to 2)")


# 2.მომხმარებელი დაარეგისტრირე ონლაინ პლატფორმაზე თუ სახელის ველი არ იქნება ცარიელი,
# ხოლო პაროლი 8 სიმბოლოზე მეტი ან ტოლია. მისი მონაცემები შეინახე ლისთში. შემდეგ მიეცი საშუალება სცადოს პლატფორმაზე შესვლა და შეადარე მის მიერ შემოყვანილი ინფორმაცია სიაში შენახულ ინფორმაციას. დაბეჭდე შესაბამისი მესიჯი.
# user_name = input("for registration please enter your name: ")
# user_pass = input("now enter your password: ")
# data = []
# data2 = []
# if (len(user_name)>0 and len(user_pass)>=8):
#     data.append(user_name)
#     data.append(user_pass)
# else:
#     print("please input the valid data")

# login_name = input("for authorisation enter your name: ")
# login_pass = input("now enter your password: ")
# data2.append(login_name)
# data2.append(login_pass)

# if (data == data2):
#     print("your name and password is right, you can log in to you acc")
# else:
#     print("your name or password is incorrect, please try again")


# 3.შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული ცნობილი მსახიობების შესახებ ინფორმაცია. მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი. თუ სიაში მოიძებნა მსახიობი, დაბეჭდა მის შესახებ არსებული ინფორმაცია რეზუმის სახით.


data = [["Name: Leonardo DiCaprio", "Born: 1974", "Age: 49", "Country: Los Angeles"],
        ["Name: Audrey Hepburn", "Born: 1929",
            "Age: 64(died)", "Country: Belgium"],
        ["Name: Kate Winslet", "Born: 1975", "Age: 48", "Country: United Kingdom"],
        ["Name: Marilyn Monroe", "Born: 1926",
            "Age: 36(died)", "Country: California, US"],
        ["Name: Julia Roberts", "Born: 1967", "Age: 56", "Country: Georgia, US"],
        ["Name: Johnny Depp", "Born: 1963", "Age: 60", "Country: Kentucky, US"],
        ["Name: Charles Chaplin", "Born: 1889",
            "Age: 88(died)", "Country: London, UK"],
        ["Name: Al Pacino", "Born: 1940", "Age: 83", "Country: New York, US"]]

data_to_check = input("enter the name or surname to check in the list: ")

found = False
for person_data in data:
    if data_to_check in person_data[0]:
        found = True
        indx = data.index(person_data)
        break

if found:
    print("\n".join(data[indx]))
else:
    print(f"{data_to_check} is not in the list.")
