print("PROGRAMMING BASICS")

user_name = input("Enter your name: ")

print(f"\n{user_name}, do you know what variables are? Yes/No")

while True:
    variables = input("Answer: ").lower()

    if variables in ["yes", "y"]:
        print("\nGreat!")
        print("A variable is a named box where you store a piece of information so you can use or change it later in your program.")
        break
    elif variables in ["no", "n"]:
        print("\nNo problem! Let me explain.")
        print("A variable is like a labeled box that stores information.")
        break
    else:
        print("Please answer with yes or no.")

print("\nExample:")
print("age = 15")
print("Here, 'age' is the variable and 15 is the value stored inside it.")

print("\nDo you want to learn about data types? Yes/No")

while True:
    data_types = input("Answer: ").lower()

    if data_types in ["yes", "y"]:
        print("\nData Types:")
        print("1. int  → Whole numbers (e.g., 5, 10)")
        print("2. float → Decimal numbers (e.g., 3.14)")
        print("3. str  → Text (e.g., 'hello')")
        print("4. bool → True or False")
        break
    elif data_types in ["no", "n"]:
        print("\nAlright! We'll stop here.")
        break
    else:
        print("Please answer with yes or no.")

print("QUIZ TIME!")
print("first question")
answer = input("Is 3.14 an int or a float? ").lower()

if answer == "float":
    print("Correct!")
else:
    print("Not quite. 3.14 is a float because it has decimals.")

print("second question")
answer = input("What data type is 25? ").lower()

if answer == "int":
    print("Correct!")
else:
    print("Not quite. 25 is a int.")