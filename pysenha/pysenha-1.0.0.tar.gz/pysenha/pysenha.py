
#############################################################################################################################
#   filename:pysenha.py                                                       
#   created: 2022-03-23                                                              
#   import your librarys below                                                    
#############################################################################################################################


def pysenha(old_password):
  
    old_password = old_password.replace("", "-")
    old_password = old_password.split('-')[1:17]
    new = []
    for i in range(len(old_password)):
        a = random.choice(old_password)
        new.append(a)
    
    return print(''.join(new))
    