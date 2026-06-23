# Fundamental booster


print("Welcome to Interactive Personal Data Collecter program")


name=(input(" Please Enter your name:"))
age=(int(input("Please Enter your Age")))
height=(float(input("Please Enter your height in meters")))
favourite=(int(input("Please Enter your favourite number")))
    
print("\nThank you! for your information.")
print("here is your information we collect")
print("\n")
print(f"Name: {name}(Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age}(Type: {type(age)}, Memory Address: {id(age)})")    
print(f"Height: {height}(Type: {type(height)}, Memory Address: {id(height)})")    
print(f"Favourite: {favourite}(Type: {type(favourite)}, Memory Address: {id(favourite)})")

birth_year= 2026 - age

print(f"your birth year is approximately ({birth_year}(based on your age of{age}))")    
print("\n")
print ("Thank you for using the personal Data collector. Goodbye!")
