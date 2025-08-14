# here we go again 
def ShowMenu():
    print("----- Unit converter -----")
    print("1. Weight")
    print("2. Heat")
    print("3. Height")
    print("4. Exit")

def ShowMenuWeight():
    print(" Weight Converter ")
    print("Choose the one you want convert: 1: Kilogram -> Pound  or  2: Pound -> Kilogram ?")
    choice = input("Enter your choice: ")
    value = float(input("Enter the value: "))
    
    if choice == "1":
        result = value * 2.20462
        print(f" {value} kg = {result} lb")
    elif choice == "2":
        result = value / 2.20462
        print(f" {value} lb = {result} kg")
    else:
        print("Invalid choice...!")   

def ShowMenuHeat():
    print(" Heat Converter")
    print("Choose the one you want convert: ")
    print("1: C -> F")
    print("2: F -> C")
    choice = input("Enter your choice: ")
    value = float(input("Enter the value: "))
    
    if choice == "1":
        result = (value * 9/5) + 32
        print(f" {value} C = {result} F")
    elif choice == "2":
        result = (value - 32) * 5/9
        print(f" {value} F = {result} C")
    else:
        print("Invalid choice...!") 

def ShowMenuHeight():
    print(" Height Converter ")
    print("Choose the one yout want convert: ")
    print("1: m to km")
    print("2: km to m")
    print("3: m to mile")
    print("4: mile to m")
    choice = input("Enter your choice: ")
    value = float(input("Enter the value: "))
    
    if choice == "1":
        result = value / 1000
        print(f" {value} m = {result} km")
    elif choice == "2":
        result = value * 1000
        print(f" {value} km = {result} m")
    elif choice == "3":
        result = value * 0.000621371
        print(f" {value} m = {result} mile")
    elif choice == "4":
        result = value * 1609.34
        print(f" {value} mile = {result} m")
    else:
        print("Invalid choice...!")  
        
while True:
    ShowMenu()
    firstChoice = input("enter your choice: ")
    
    if firstChoice == "1":
        ShowMenuWeight()
    
    elif firstChoice == "2":
        ShowMenuHeat()
        
    elif firstChoice == "3":
        ShowMenuHeight()
        
    elif firstChoice == "4":
        print("Have a Nice Day, Byeee....")
        break
