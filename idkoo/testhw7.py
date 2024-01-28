# # Function packing and unpacking arguments
# def display_info(*args):
#  for arg in args:
#     print(arg)
# # Packing and unpacking in function call
# info = ("Alice", 25, "New York") 
# display_info(*info)

# . რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)

# 2. შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.

# 3. შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს, და დააბრუნებს და დაბეჭდავს ნარმავლს.

# Global variable
y = 20
# Function accessing global variable
def my_function():
 print("Inside the function:", y)
my_function()
print("Outside the function:", y)

def details(name, age, country):
 print(f"Name: {name}, Age: {age}, Country: {country}") 
user_info = {"name": "Alice", "age": 25, "country": "USA"} 
# Unpacking dictionary into keyword arguments
details(**user_info) # Output: Name: Alice, Age: 25, Country: US


# fruits = ['apple', 'banana', 'Orange', 'Grape']
# new_fruits = [fruit for fruit in fruits if not fruit[0].isupper()]
# length = lambda new_fruits: len(new_fruits)
# result = length(new_fruits)
# print(result)