import csv
import pandas as pd

def open_db_meals(): ## Open database and return content

    col_list=["Category","Meal Name"]
    df=pd.read_csv("allMealsData.csv",usecols=col_list)
    return df


def add_db_meals(new_meal_cat,new_meal_name):
    with open("allMealsData.csv", "a", encoding="UTF8") as f: #write user input to csv file without header
        myFile = csv.writer(f)
        myFile.writerow([new_meal_cat,new_meal_name])

