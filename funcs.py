from classes import ChooseMeal
from database import open_db_meals
from database import add_db_meals

def print_db_meals(): ## Print entire meal database - Main func
    print("\n")
    print(open_db_meals())
    print("\n")


def add_new_meal(): ## User input to fill the database of different meals - Main func
    print("Let´s fill your Library with delicious food ideas.")
    while True:
        new_meal_cat = input("\nType 'done' when finished.\n\nEnter a Category? Pasta, Rice, Fast Food, etc...: ")
        if new_meal_cat == "done":
            print("All set! The meals have been added to your list.")
            break
        else:
            new_meal_name = input("Please type a new meal you would like to add: ")
            add_db_meals(new_meal_cat,new_meal_name)
            print("Your meal was added. Keep going :-)")
            
            continue

def suggest_meal(db_meals): ## Select a random meal from database and print it - Main func

    while True:
        db_meals = db_meals["Meal Name"].tolist() #get all meals and return it as a list
        new_meal = ChooseMeal(db_meals)
        new_meal.shuffle()
        print("\n" + new_meal.serveMeal() + "\n")

        while True:
            try:
                happy = input("Are you happy or do you want to choose again? Type 'happy' or 'again': ")
            except:
                print("Please type happy or again. Please try again.")
            else:
                if happy.lower() == "happy":
                    break
                elif happy.lower() == "again":
                    new_meal = ChooseMeal(db_meals)
                    new_meal.shuffle()
                    print("\n")
                    print(new_meal.serveMeal())
                    print("\n")
                    continue
        break


def select_category(): ## User selects a category from db

    #print categories
    db_meals = open_db_meals()
    cat = db_meals["Category"].drop_duplicates() #only get unique categories
    print("\n")
    print(cat)
    #take user input
    while True:
        choose_cat = str(input("\nPlease select a category. Type Category name: "))
        if choose_cat.title() in cat.tolist():
            break
        else:
            print("Please type the category name! Try again.")
            continue
    return choose_cat.title()

## Take the selected category and print a random meal from it - Main func
def suggest_meal_from_cat(Category):

    #get all meals from the chosen category
    db_meals = open_db_meals()
    db_meals = db_meals[db_meals["Category" ] == Category ]
    db_meals = db_meals["Meal Name"].tolist()
    # append meals as list to class C
    new_meal = ChooseMeal(db_meals)
    new_meal.shuffle()
    print("\n" + new_meal.serveMeal() + "\n")
    # ask if happy or shuffle again
    while True:
            happy = input("Are you happy or do you want to choose again? Type 'happy' or 'again': ")
            print("Please type happy or again. Please try again.")
            if happy.lower() == "happy":
                break
            elif happy.lower() == "again":
                new_meal = ChooseMeal(db_meals)
                new_meal.shuffle()
                print("\n")
                print(new_meal.serveMeal())
                print("\n")
                continue
            else:
                print("Please type 'happy' or 'again'")