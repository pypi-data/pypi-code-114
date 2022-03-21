def num2rank(number):    
    number = str(number)
    length = len(number) - 1
    #calculate exceptions to the rule
    if length >= 1:
        print("got here!")
        if int(number[length-1] + number[length-2]) == 11:
            return number + "th"
        if int(number[length -1] + number[length-2]) == 12:
            return number + "th"
        if int(number[length - 1] + number[length-2]) == 13:
            return number + "th"
            
    #calculate for numbers that follow the rule
    if int(number[length]) == 1:
        return number + "st"
    if int(number[length]) == 2:
        return number + "nd"
    if int(number[length]) == 3:
        return number + "rd"
    if int(number[length]) >= 4 < 9 or int(number[length]) == 0:
        return number + "th"