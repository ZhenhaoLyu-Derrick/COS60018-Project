INGREDIENT_DATABASE = {
    "flour": 120.0,
    "sugar": 200.0,
    "brown sugar": 220.0,
    "butter": 227.0,
    "water": 236.0,
    "milk": 240.0,
    "honey": 340.0,
    "cocoa powder": 100.0,
    "rolled oats": 90.0,
    "chocolate chips": 170.0
}

def show_main_menu():
    print("\n--- MAIN MENU ---")
    print("1. Convert Ingredient Volume to Weight (Cups to Grams)")
    print("2. Convert Ingredient Weight to Volume (Grams to Cups)")
    print("3. Convert Oven Temperature")
    print("4. Convert Liquid (Ounces to Milliliters or vice versa)")
    print("5. Exit Program")

def show_ingredients():
    print("\nAvailable Ingredients:")
    for item in INGREDIENT_DATABASE:
        print("- " + item)
    print("----------------------")

def fahrenheit_to_celsius(f_temp):
    celsius = (f_temp - 32) * (5 / 9)
    return celsius

def celsius_to_fahrenheit(c_temp):
    fahrenheit = (c_temp * (9 / 5)) + 32
    return fahrenheit

def start_converter():
    program_running = True
    
    while program_running:
        show_main_menu()
        user_choice = input("Please select an option (1-5): ")
        
        if user_choice == "1":
            show_ingredients()
            ingredient_choice = input("Type the name of the ingredient: ")
            
            if ingredient_choice in INGREDIENT_DATABASE:
                cups_input = input("How many cups? (e.g. 1.5): ")
                
                check_number = cups_input.replace(".", "")
                
                if check_number.isdigit():
                    cups = float(cups_input)
                    grams_per_cup = INGREDIENT_DATABASE[ingredient_choice]
                    total_grams = cups * grams_per_cup
                    print("\nRESULT: " + str(cups) + " cups of " + ingredient_choice + " is " + str(total_grams) + " grams.")
                else:
                    print("\nERROR: Please enter a valid number for cups.")
            else:
                print("\nERROR: Ingredient not found in the database.")
        elif user_choice == "2":
            show_ingredients()
            ingredient_choice = input("Type the name of the ingredient: ")
            
            if ingredient_choice in INGREDIENT_DATABASE:
                grams_input = input("How many grams? (e.g. 250): ")
                check_number = grams_input.replace(".", "")
                
                if check_number.isdigit():
                    grams = float(grams_input)
                    grams_per_cup = INGREDIENT_DATABASE[ingredient_choice]
                    total_cups = grams / grams_per_cup
                    total_cups = round(total_cups, 2)
                    print("\nRESULT: " + str(grams) + " grams of " + ingredient_choice + " is about " + str(total_cups) + " cups.")
                else:
                    print("\nERROR: Please enter a valid number for grams.")
            else:
                print("\nERROR: Ingredient not found in the database.")
        elif user_choice == "3":
            print("\nTemperature Options:")
            print("A. Fahrenheit to Celsius")
            print("B. Celsius to Fahrenheit")
            temp_choice = input("Choose A or B: ")
            
            if temp_choice == "A" or temp_choice == "a":
                temp_input = input("Enter temperature in Fahrenheit: ")
                check_number = temp_input.replace(".", "").replace("-", "")
                
                if check_number.isdigit():
                    f_temp = float(temp_input)
                    c_temp = round(fahrenheit_to_celsius(f_temp), 1)
                    print("\nRESULT: " + str(f_temp) + " F is " + str(c_temp) + " C.")
                else:
                    print("\nERROR: Please enter a valid number.")
            elif temp_choice == "B" or temp_choice == "b":
                temp_input = input("Enter temperature in Celsius: ")
                check_number = temp_input.replace(".", "").replace("-", "")
                
                if check_number.isdigit():
                    c_temp = float(temp_input)
                    f_temp = round(celsius_to_fahrenheit(c_temp), 1)
                    print("\nRESULT: " + str(c_temp) + " C is " + str(f_temp) + " F.")
                else:
                    print("\nERROR: Please enter a valid number.")
            else:
                print("\nERROR: Invalid selection.")
        elif user_choice == "4":
            print("\nLiquid Conversion Options: ")
            print("A. Fluid Ounces to Milliliters")
            print("B. Milliliters to Fluid Ounces")
            liquid_choice = input("Choose A or B: ")

            if liquid_choice == "A" or liquid_choice == "a":
                oz_input = input("\nEnter fluid ounces: ")
                check_oz_number = oz_input.replace(".", "").replace("-", "")

                if check_oz_number.isdigit():
                    oz = float(oz_input)
                    milliliters = oz * 29.5735
                    print("\nRESULT: " + str(oz) + " fluid ounces is approximately " + str(milliliters) + " milliliters.")
                else:
                    print("\nERROR: Please enter a valid number.")
            elif liquid_choice == "B" or liquid_choice == "b":
                ml_input = input("\nEnter milliliters: ")
                check_ml_number = ml_input.replace(".", "").replace("-", "")

                if check_ml_number.isdigit():
                    ml = float(ml_input)
                    fluid_ounces = ml / 29.5735
                    print("\nRESULT: " + str(ml) + " milliliters is approximately " + str(fluid_ounces) + " fluid ounces.")
                else:
                    print("\nERROR: Please enter a valid number.")
        elif user_choice == "5":
            print("\nThank you for using the Baking Converter. Goodbye!")
            program_running = False 
        else:
            print("\nERROR: Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    start_converter()