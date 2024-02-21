import product
from juice import juice_choice


active = True
user_order = []

while active:
    print("Welcome to Python Kebab!\n", "`"*80)
    print("What you desire:\n1 - Kebab, \n2 - Juice, \n3 - French fries, \n4 - Menu, \n5 - Show cart, \n6 - Total price")
    user_option = input("Enter your order option: ")

    if user_option.lower() == "q" or user_option == "":
        print("Goodbye!")
        active = False
    elif user_option == "1":
        print(f"The selected option is {user_option}")
    elif user_option == "2":  # Juice selection
        user_order.append(juice_choice())
    elif user_option == "3":
        pass
    elif user_option == "4":
        pass
    elif user_option == "5":  # Show cart
        for product in user_order:
            product.presentation()
    elif user_option == "6":  # Total price
        summ = 0
        for product in user_order:
            summ += product.price
        print(f"Total price: {summ}")
    else:
        print(f"The chosen option is: {user_option}")


