#დედლაინს გადამიცდა მაგრამ იქნებ შეამოწმოთ გამოცდები დამეწყო უნივერსიტეტში და ვერმოვახერხე დროულად დაწერა😔

# 1. დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას.

from random import randint
import time

def list_generator():
    arr=[]
    for i in range(10):
        arr.append(randint(1,100))
    return arr

randoms = list_generator()
print(randoms)

# 2. დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით.

sorted_list = sorted(randoms)
print(sorted_list)

# 3. დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება.

def LinearSearch(list, element):
    for i in range (len(list)):
        if list[i] == element:
            return i
    return -1

print(LinearSearch(sorted_list, 9))

def binary_search(lst, item):
    begin_index = 0
    end_index = len(lst) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = lst[midpoint]
        
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    
    return None

myItem = 10
print(binary_search(sorted_list, myItem))


# 4. დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds")
        return result
    return wrapper

def generate_and_search(size, search_func):
    random_list = [randint(1, 100) for _ in range(size)]
    sorted_list = sorted(random_list)
    search_item = randint(1, 100)
    search_func(sorted_list, search_item)

@timing_decorator
def linear_search(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1

@timing_decorator
def binary_search(lst, item):
    begin_index = 0
    end_index = len(lst) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = lst[midpoint]
        
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    
    return None

# Test with different list sizes
list_sizes = [10, 100, 1000]

for size in list_sizes:
    print(f"\nTesting with list size {size}:")
    generate_and_search(size, linear_search)
    generate_and_search(size, binary_search)
