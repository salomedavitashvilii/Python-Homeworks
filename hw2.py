# 1. ვიქტორინა 
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?” სავარაუდოპასუხები: 
# 1.შუმერთა
# 2.სელჩუკთა
# 3.რომის
# 4.მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი. შეცდომის შემთხვევაში იბეჭდება: „არა! სწორი პასუხია რომის!“ სწორი პასუხის შემთხვევაში იბეჭდება: „სწორია!“

# quest = input("რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებ სდღესაც?")
# print("სავარაუდო პასუხები:\n 1.შუმერთა\n 2.სელჩუკთა\n 3.რომის\n 4.მონღოლთა")
# ans = input("აირჩიეთ ერთ-ერთი: ")
# if (ans == "4" or ans == "რომის"):
#     print("სწორია!")
# else:
#     print("არა! სწორი პასუხია - რომის!")

# 2. ონლაინ მაღაზია 
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას. 
# მაგ. 1.ლეპტოპები
#     2.პერსონალური კომპიუტერები
#     3.მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში. (თითო კატეგორიაში მინიმუმ 
# 3 პროდუქტი მაინც უნდა იყოს) თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში 
# არ გააჩნია შემოთავაზება.

# print("პროდუქტების ჩამონათვალი (აირჩიეთ ერთ-ერთი):\n1.ლეპტოპები\n2.პერსონალური კომპიუტერები\n3.მობილურები")
# chosen = input("")
# budget = int(input("შეიყვანეთ მაქსიმალური ბიუჯეტი: "))
# if (800<budget<1500):
#     if (chosen == "1"):
#         print("lenovo thinkbook")
#     elif (chosen == "2"):
#         print("Lenovo F0G500ALRK")
#     elif (chosen == "3"):
#         print("iPhone 11")
# elif (1500<budget<2500):
#     if (chosen == "1"):
#         print("acer swift i5")
#     elif (chosen == "2"):
#         print("HP 22-c0031ur")
#     elif (chosen == "3"):
#         print("iPhone 13 pro max")
# elif (2500<budget):
#     if (chosen =="1"):
#         print("hp")
#     elif (chosen == "2"):
#         print("HP 24 23.8")
#     elif (chosen == "3"):
#         print("iPhone 15 Pro")
# else:
#     print("ამ თანხაში არ გვაქვს შემოთავაზება ამ ეტაპზე🥹")

# 3. ქუესთის შედგენა (Text Based Adventure Game) 
# დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების გამოყენებით მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
# მაგ თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს მქომედების რამდენიმე ვარიანტს. სხვადასხვა არჩევანის შემთხვევაში თამაშს ხვადასხვანაირად ვითარდება. 

# print("welcome to the treasure island. your mission is to find the treasure.")
# firstq = input("left or right? ")
# # if (firstq == "right"):
# #     print("Game over!")
# if (firstq == "left"):
#     secondq = input("swim or wait?")
# elif (firstq == "right"):
#     print("game over, try again later 🤷‍♀️")
# if (secondq == "wait"):
#     thirdq = input("which door? blue, yellow or red?")
# elif (secondq == "swim"):
#     print("game over, try again later 🤷‍♀️")
# if (thirdq == "yellow"):
#     print("congratulations! you win!🏆")
# else:
#     print("game over, try again later 🤷‍♀️")

# 4. მომხმარებლისთვის კარიერის შერჩევა (არასავალდებულო)
# პროგრამა უსვამს მომხმარებელს რამდენიმე კითხვას (თქვენი იმპროვიზაციით) და ურჩევს მისთვის შესაფერის პროფესიას.

first = input("do you prefer technical or historical subjects? ")
if (first == "technical"):
    second = input("do you prefer business ideas or programming tasks? ")
    if (second == "business"):
        print("you'd better continue your studies for business administration")
    elif (second == "programming tasks"):
        print("i thiknk you should go for a programming field")
elif (first == "historical"):
    third = input("do you prefer law proccesses or psycology? ")
    if (third == "law processes"):
        print("i guess legal field is right for you")
    elif (third == "psycology"):
        print("helping other people mentally is good option for you")
