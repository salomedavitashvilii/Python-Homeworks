# 1. დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.

numbers = [1, 2, 9]
def multiply(x, y): return x * y
result = [multiply(num, 3) for num in numbers]
print(result)

# 2. დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს, მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება. (გამოიყენე .isupper() მეთოდი)

# fruits = ['apple', 'banana', 'berry', 'berry', 'Orange', 'grape']
# for fruit in fruits:
#     if fruit[0].isupper():
#             fruits.remove(fruit)
# length = lambda x: len(x)
# result = length(fruits)
# print(result)   #ასე არ გამოდიოდა და რატომ წესით ხომ სწორია?

fruits = ['apple', 'banana', 'Berry', 'Orange', 'grape']
new_fruits = list(filter(lambda x: x[0].islower(), fruits))
length = lambda x: len(x)
result = length(new_fruits)
print(result)



# 3. დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.


def sum(x):
    positive_sum = 0
    negative_sum = 0
    positive_nums = list(filter(lambda i: i > 0, x))
    negative_nums = list(filter(lambda i: i <= 0, x))
    
    for num in positive_nums:
        positive_sum += num
    for num in negative_nums:
        negative_sum += num
    return positive_sum, negative_sum

numbers = [1, 7, -2, 8, -5]
result = sum(numbers)
print(result)


# 4. დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.

user_name = input("what username do you want to be? ")
password = input("now choose a password: ")
money = float(input("how much do you want to transfer into your acc? "))
try:
    auth_username = input("enter your username here... ")
    auth_pass = input("enter your account password... ")
    if (user_name == auth_pass and password == auth_pass):
        print(f"{user_name}, you have successfully logged in to your account, and your balance is {money} GEL")
    else:
        raise ValueError
except ValueError:
    print("your username or password is inccorect, please try again...")
