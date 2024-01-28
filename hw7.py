# რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)

def greet(n):
    word = "Hello"
    print(n*word)


greet(3)

# 2. შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.


def order(dish, num=1):
    print(dish, num)


order("meat")

# 3. შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს, და დააბრუნებს და დაბეჭდავს ნარმავლს.


def multiply(*args):
    if len(args) >= 3:
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "you should input at least 3 numbers"


print(multiply(2, 2, 3))
