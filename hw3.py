# 1.დაასრულე ჯეირანის თამაშის პროგრამა ციკლის გამოყენებით. თამაშის დასასრულებლად რომელიმე მოთამაშემ უნდა დააგროვოს 3 ქულა.
# Rock 0
# Paper 1
# scissors 2
# import random
# arr = ["Rock", "Paper", "Scissors"]
# user_score = 0
# computer_score = 0
# while (user_score<3 and computer_score< 3):
#     choose = int(input("what do you want to choose? write 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
#     if choose in [0, 1, 2]:
#         num = random.randint(0, 2)
#         if (choose == num):
#             print("It's a draw")
#         elif (choose == 0 and num == 2) or (choose == 1 and num == 0) or (choose == 2 and num == 1):
#             print("you win this round!")
#             user_score += 1
#         else:
#             print("computer wins this round!")
#             computer_score += 1
#         print(f"your score: {user_score}, computer's score: {computer_score}")
# if (user_score > computer_score):
#     print("congratulations! you win the game! 🏆")
# elif (user_score < computer_score):
#     print("sorry, you lose the game. better luck next time. 🥹")
# else:
#     print("the game ends in a tie. 🤝")


# 2. გამრავლების ტაბულა ორმაგი for ციკლის დახმარებით
# დაბეჭდე გამრავლების ტაბულა 1-დან მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.
# num = int(input("enter the num "))
# for j in range(1, num+1):
#     for i in range(1, 11):
#         ans = j * i
#         print(f"{j} x {i} = {ans}")


# 3. საბანკო ანგარიში
# შეადგინე პროგრამა, რომელიც განასახიერებს საბანკო ანგარიშს. მასზე განთავსებულია თანხა 3000 ლარის ოდენობით. პროგრამა გეკითხება,გაწეულ ხარჯს და აკლებს ანგარიშს მანამ, სანამ არ შეიყვან 0-ს. შემდეგ გიბეჭდავს ანგარიშზე დარჩენილ თანხას და წყვეტს ფუნქციონირებას. თუ ანგარიშზე არსებული თანხა ნაკლებია დანახარჯის თანხაზე, პროგრამამ უნდა დაბეჭდოს, რომ ანგარიშზე არ არის საკმარისი თანხა და გააგრძელოს ფუნქციონირება

# amount = 3000
# while (True):
#     quest = int(input("how many did you spend? "))
#     amount -= quest
#     print(amount)
#     if (quest == 0):
#         break
#     if (amount < quest):
#         print("there is not enough amount of money")


# 4.თუთიყუშის პროგრამა
# დაწერე პროგრამა - თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ, სანამ არ შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat!?”თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება „User Said Whaaat!?” “User Said Hello”
while (True):
    word = input("")
    print(f"'User Said Whaaat!?' 'User Said {word}'")
    if (word == "quit"):
        break
