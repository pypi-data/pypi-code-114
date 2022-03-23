def print_program(number):
    if(number<1 or number >9):
        print(f'Program number {number} not available')
        return
    f = open('Prog'+str(number)+'.py','r')
    count =1
    for line in f.readlines():
        print(f'{line}', end='')
        count+=1
