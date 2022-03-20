def MoonDistance(age):
     '''
        This function is computed by considering
        that an average person would have walked 
        120700 kms by the age of 80
        age : int
        sex : str
     '''
     distanceToTheMoon = 382500
     yourDistanceToMoon = round(age*80/120700,2)
     
     return print("You have walked so far", yourDistanceToMoon, " times the distance from the earth to the moon" )
      
def strandsofrhairlost(age, sex ):
    '''
    According to the American Academy of Dermatologists. It is normal
    to lose anywhere from 50 to 100 strands of hair per day.
    age : int
    sex : str
    '''
    if sex == "F":
        constantSex = 2
    else :
        constantSex = 1
    hairlost = 50*360*age*constantSex 
    return print("Up to day, you have lost", hairlost, " strands of hair in your life" )
    
    
class HumanBeing:
    '''
    Age and height need to be an integer 
    Sex needs to be either M for (Male)
    
    '''
    def __init__(self, age, height, sex , name,weight):
         self.age = age
         self.height = height
         self.sex = sex
         self.name = name
         self.weight=weight
      