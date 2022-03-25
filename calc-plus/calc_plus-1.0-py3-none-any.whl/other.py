import random
def middle(min: int,max: int):
 return (min+max)/2
def chance(number: int,change: int):
    return number+random.randint(-change,change)
