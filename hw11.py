# 1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

def unique_list():
    nums = [1,2,3,2,6,3]
    new_nums = set(nums)

    return new_nums

print(unique_list())

# 2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).

def immutable_set():
    some_list = ["street", "book", "phone", "pack","book","street"]
    new_set = set(some_list)
    frozen_set = frozenset(new_set)
    return frozen_set
print(immutable_set())

# 3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

def set_to_tuple():
    words1 = {"davit", "roza", "guga", "tika"}
    words2 = {"beka", "lizi", "saba", "lasha"}
    united = words1.union(words2)
    untuple = tuple(united)
    return untuple
print(set_to_tuple())