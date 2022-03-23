def print_dataset(number):
    if(number == 3 or number == 4 or number == 6):
        f = open(f'prog{number}_dataset.csv','r')
        count =1
        for line in f.readlines():
            print(f'{line}', end='')
            count+=1
    else:
        print(f'No dataset available for {number}')

