from database import open_db_meals
from funcs import suggest_meal
from funcs import suggest_meal_from_cat
from funcs import add_new_meal
from funcs import print_db_meals
from funcs import select_category


def main():
    print("\nWelcome to your Breakfast, Lunch & Dinner automation! \
        \nSafe your energy about what to choose to eat today.\
        \nThis is your automation tool that helps you focus on the desicions that matter!\
        \n\n Let's go!\n")
    while True:
        print("\n\tWhat do you want to do?\n")
        try:
            menu_sel = int(input("\
                 1. Get a random meal from your Food Library.\n \
                2. Get a random meal from a category you choose.\n \
                3. Add new meals to your Library.\n \
                4. Show me my Library.\n\n \
                Please type 1,2,3 or 4: "))
        except:
            print("\nPlease type a number from 1 - 4. Try again.")
            
        else:
            if menu_sel == 1:
                suggest_meal(open_db_meals())
                main_menu = input("Return to menu? Type 'y' or 'n':  ")
                if main_menu == "y":
                    continue
                elif main_menu == "n":
                    print("Enjoy your meal!")
                    break
            elif menu_sel == 2:
                suggest_meal_from_cat(select_category())
                main_menu = input("Return to menu? Type 'y' or 'n':  ")
                if main_menu == "y":
                    continue
                elif main_menu == "n":
                    print("Enjoy your meal!")
                    break
            elif menu_sel == 3:
                add_new_meal()
                main_menu = input("Return to menu? Type 'y' or 'n':  ")
                if main_menu == "y":
                    continue
                elif main_menu == "n":
                    print("Have nice day!")
                    break
            elif menu_sel == 4:
                print_db_meals()
                main_menu = input("Return to menu? Type 'y' or 'n':  ")
                if main_menu == "y":
                    continue
                elif main_menu == "n":
                    print("Have nice day!")
                    break
           
if __name__ == "__main__":
    main()
