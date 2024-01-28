# print("hello world")
# 4. ააწყვე იქსიკის და ნულიკის თამაში ჩაშენებული სიების მეშვეობით.

# · შექმენი მატრიცა კვადრატების ნომრებით.

# · შექმენი მთავარი ციკლი.

# · შემოაყვანინე პირველ მომხმარებელს იქსიკის ჩასმის ლოკაცია (კვადრატის ნოომერი)

# · შემოაყვანინე მეორე მომხმარებელს ნულიკის ჩასმის ლოკაცია. (კვადრატის ნოომერი)

# · დაბეჭდე არსებული მდგომარეობა.

# · გაამეორე ციკლი მანამ, სანამ ლოგიკური გამონათქვამის მეშვეობით არ დადგინდება რომ რომელიმე მოთამაშემ მოიგო.

table = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
while True:
    v = int(input("enter the vertical location number from 0 to 2 "))
    h = int(input("enter the horizontal location number from 0 to 2 "))
    sym = input("enter the symbol 0 or X ")
# for i in table:
    table[v][h] = sym
    print(f"{table}\n")
for i in range(2):
    for j in range(2):
        if (table[0][0] == table[1][1] == table[2][2] or
                table[0][0] == table[0][1] == table[0][2] or
                table[0][0] == table[1][0] == table[2][0] or
                table[1][0] == table[1][1] == table[1][2] or
                table[2][0] == table[2][1] == table[2][2]):
            # მგონი არასწორად მივდივარ მარა ნახეთ აბა მაინც~
            
            print("You win")
