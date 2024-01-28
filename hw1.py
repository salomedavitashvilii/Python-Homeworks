# 1. დაწერეპროგრამარომელიცგეკითხებაჯერსახელს, შემდეგგვარსდაინფორმაციისმიღებისშემდეგტერმინალშიბეჭდავსერთმანეთისგვერდით. George Abramia

name = input("what is your name? ")
surname = input("what is your surname? ")
print(name, surname)

# 2. დაწერეპროგრამარომელიცითხოვსორრიცხვს, პირველირიცხვიაჰყავსმეორისხარისხშიდაშედეგიიბეჭდებატერმინალში.
x = input("enter number: ")
y = input("enter another number: ")
print(int(x)**int(y))

# 3. დაწერეპროგრამარომელიცგეკითხება სახელს, გვარს, ასაკს და ქალაქს დაბეჭდავსინფორმაციასშემდეგისახით:
# Name: LiaSurname: KebadzeAge: 20City: Tbilisi
name = input("Enter your name: ")
surname = input("now your last name: ")
age = input("what is your age? ")
city = input ("enter city name: ")
print(f"Name: {name}\nSurname: {surname}\nAge: {age}\nCity: {city}")
# 4. დაწერეპროგრამა, რომელიცგთხოვსშეიყვანონებისმიერისამისხვადასხვახილისდასახელებაცალცალკე. რეზულტატიკიიბეჭდებაშემდეგისახით:Apple//Peach%%Orange
fruit1 = input("enter the first fruit: ")
fruit2 = input("enter the second fruit: ")
fruit3 = input("enter the third fruit: ")
print(f"{fruit1}//{fruit2}%%{fruit3}")
# 5. დაწერეპროგრამა, რომელიცგთხოვსშეიყვანოტექსტი, დათვლისმასშიარსებულისიმბოლოებისრაოდენობასდაგამოიტანსშედეგსშემდეგნაირად:Number of symbols: 50
str = input("Please enter some text: ")
print(f"Number of symbols: {len(str)}")