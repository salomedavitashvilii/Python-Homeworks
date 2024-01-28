# 1. დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.

def myfunc(file_path):
    with open(file_path, 'a') as user_file:
        user_input = input("enter some information (type 'enough' to stop): ")
        while user_input.lower() != "enough":
            user_file.write(user_input + '\n')
            user_input = input("enter some information (type 'enough' to stop): ")

with open('countries.txt', 'r') as my_file:
    line = my_file.readline() 
    while line:  
        print(line.strip()) 
        line = my_file.readline()  

myfunc('countries.txt')

# 2. დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.

import os
def create_file(folder_location, file_name):
    if not os.path.exists(folder_location):
        os.makedirs(folder_location)

    with open(os.path.join(folder_location, file_name), 'w') as f:
        f.write('new file ')

def get_files_in_folder(folder_location):
    files = os.listdir(folder_location)

    for file in files:
        print(file)


folder_location = input('enter the folder location: ')
file_name = input('enter the file name: ')

create_file(folder_location, file_name)

get_files_in_folder(folder_location)

