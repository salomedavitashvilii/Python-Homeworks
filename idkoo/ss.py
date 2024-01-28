def get_unique_numbers():
    numbers = []
    
    while True:
        user_input = input("Enter a number (type 'exit' to finish): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to finish.")
    
    unique_numbers = list(set(numbers))
    return unique_numbers

# Example usage:
unique_numbers_list = get_unique_numbers()
print("Unique numbers entered:", unique_numbers_list)
