# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად: input: “ablabdabdab” Output: „Tripled: ablabdabdabablabdabdabablabdabdab“
def tripling(word):
    return word*3


print(tripling(input("enter something... ")))

# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6-ჯერ ნაკლებია დედამიწისაზე)


def weight_on_mars(weight):
    return float(weight)/6


print(weight_on_mars(input("enter your weight: ")))

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input() ფუნქციის დახმარებით(სამ მონაცემს - პირველ რიცხვს, მოქმედებას(+ -* / ^), მეორე რიცხვს) მაგ. „2 * 6“.  ფუნქცია დაშლის სტრიქონს split()ფუნქციის გამოყენებით. დათვლის და დააბრუნებს შედეგს. გაითვალისწინე, რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი. ასევე, ნულზე გაყოფა არ შეიძლება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)
# def calculator(num1, operation, num2):


def calculator():
    nums = input("enter what you want to calculate: ")
    data = nums.split()
    if (len(data) != 3):
        return "invalid input... try again."
    num1 = float(data[0])
    operator = data[1]
    num2 = float(data[2])
    if (data[1] == "+"):
        return num1 + num2
    elif (data[1] == "-"):
        return num1 - num2
    elif (data[1] == "*"):
        return num1 * num2
    elif (data[1] == "/"):
        if (num2 == 0):
            return "invalid input, you cannot devide a number into 0"
        else:
            return num1 / num2
    elif (data[1] == "^"):
        return num1 ** num2
    else:
        return "invalid input. please enter an expression for example 2 * 6 "


print(calculator())


# არასავალდებულო: გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური სიმბოლოებით დაწერილ სიტყვას, დაშიფრავს მორწეს ანბანით და დააბრუნებს შედეგს.
