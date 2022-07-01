import random


class ChooseMeal: ## Select a random meal 
    '''
    Choose random meal of the list of meals and serve one.
    '''
    def __init__(self,meal):
         self.meals = meal #takes in a list or dict of meals

    def shuffle(self):
        random.shuffle(self.meals)

    def serveMeal(self):
        return self.meals.pop()

