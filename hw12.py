# 1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.
def remove_duplicates(dictionary):
  unique_values = {}

  for key, value in dictionary.items():
    if value not in unique_values:
      unique_values[key] = value

  return unique_values

my_dict = user_profile = {
"First Name": "John", 
"Last Name": "Doe", 
"Gender": "male",
"Last Name": "Doe"
}
print(remove_duplicates(my_dict))

# 2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.
def is_empty(dictionary):
  if not dictionary:
    return True
  else:
    return False

my_dict = user_profile = {}

print(is_empty(my_dict))

# 3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს. ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას. მაგალითად გადავეცით სტრიქონი : 'racoon' უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}

def string_dict(string):
  dictionary = {}

  for char in string:
    if char not in dictionary:
      dictionary[char] = 1
    else:
      dictionary[char] += 1

  return dictionary

print(string_dict("racoon"))