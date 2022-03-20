# logic_puzzles.py

from logic_puzzle_tools import *
        
'''
    A general puzzle solver with a permutation generator
    and associations and relationships.
'''

def einstein ():
    '''
    Einstein puzzle

    There are five houses in a row in different colors.
    In each house lives a person with a different nationality.
    The five owners drink a different drink,
    smoke a different brand of cigar
    and keep a different pet, one of which is a Walleye Pike.
    
     1. The Brit lives in the red house.
     2. The Swede keeps dogs as pets.
     3. The Dane drinks tea.
     4. The green house is on the left of the white house.
              4. has to be interpreted as immediatly to the left of
              or there is more than one solution
     5. The green house owner drinks coffee.
     6. The person who smokes Pall Malls keeps birds.
     7. The owner of the yellow house smokes Dunhills.
     8. The man living in the house right in the center drinks milk.
     9. The man who smokes Blends lives next to the one who keeps cats.
    10. The Norwegian lives in the first house.
    11. The man who keeps horses lives next to the one who smokes Dunhills.
    12. The owner who smokes Bluemasters drinks beer.
    13. The German smokes Princes.
    14. The Norwegian lives next to the blue house.
    15. The man who smokes Blends has a neighbor who drinks water.
              15. has to be interpreted as lives adjacent to.  or there
              is more than one solution.
    The question is-- who owns the fish?
    '''
    logic_puzzle_setup()
    houseposition = [1, 2, 3, 4, 5] # This is fixed Left:1 2 3 4 5:Right
    # these belong to scope of einstein
    nationalities = [None] * 5
    drinks        = [None] * 5
    housecolor    = [None] * 5
    pets          = [None] * 5
    smokes        = [None] * 5

    def choose_nationalities():
        nonlocal nationalities
        permute_nationalities = permute('norwegian, brit, swede, dane, german', nationalities)
        for p in permute_nationalities:
            category(nationalities, p)
            if fails(is_associated('norwegian', 1)):                    #R10
                continue
            choose_drinks()

    def choose_drinks ():
        nonlocal drinks
        permute_drinks = permute('coffee, milk, beer, tea, water', drinks)
        for p in permute_drinks:
            category(drinks, p)
            if fails(is_associated('dane', 'tea')):                     # R3
                continue
            if fails(is_associated('milk', 3)):                         # R8
                continue
            choose_housecolor()

    def choose_housecolor ():
        nonlocal housecolor
        permute_housecolor = permute('blue, green, white, red, yellow', housecolor)
        for p in permute_housecolor:
            category(housecolor, p)
            if fails(is_associated('brit', 'red')):                     # R1
                continue
            if fails(is_just_left_of('green', 'white')):                # R4
                continue
            if fails(is_associated('green', 'coffee')):                 # R5
                continue
            if fails(is_adjacent_to('norwegian', 'blue')):              # R14
                continue
            choose_pets()
            
    def choose_pets ():
        nonlocal pets
        permute_pets = permute('fish, birds, dogs, horses, cats', pets)
        for p in permute_pets:
            category(pets, p)
            if fails(is_associated('swede', 'dogs')):                   # R2
                continue
            choose_smokes()

    def choose_smokes ():
        nonlocal smokes
        permute_smokes = permute('blends, pallmalls, bluemasters, dunhills, princes', smokes)
        for p in permute_smokes:
            category(smokes, p)
            if fails(is_associated('pallmalls', 'birds')):              # R6
                continue
            if fails(is_associated('yellow', 'dunhills')):              # R7
                continue
            if fails(is_adjacent_to('blends', 'cats')):                 # R9
                continue
            if fails(is_adjacent_to('horses', 'dunhills')):             # R11
                continue
            if fails(is_associated('bluemasters', 'beer')):             # R12
                continue
            if fails(is_associated('german', 'princes')):               # R13
                continue
            if fails(is_adjacent_to('blends', 'water')):                # R15
                continue
            a_solution()

    def a_solution ():
        # a_solution. If not enough constraints, there will be more
        # than one. If too many constraint, there will be none.
        fmt1 = '%7s %11s %8s %11s %8s %12s'
        fmt2 = '%7d %11s %8s %11s %8s %12s'
        print(fmt1%('house #','nationality','drinks','housecolor','pet','smokes'))
        print('=' * 70)
        PrintSolution(fmt2, houseposition, nationalities, drinks, housecolor, pets, smokes)
        # who owns the fish
        print('the', nationalities[idx('fish')],'owns the fish, (the Walleye Pike)')

    fixed_cat(houseposition)
    choose_nationalities()  # einstein() back to the first function at the top

def floors ():
    '''
    Baker, Cooper, Fletcher, Miller and Smith all live on different floors of an apartment house
    that contains five floors.
    
    R1 Baker does not live on the top floor.
    R2 Cooper does not live on the Bottom floor.
    R3 Fletcher does not live on the top
    R4      or the bottom floor.
    R5 Miller lives on a higher floor than does Cooper.
    R6 Smith does not live on a floor adjacent to Fletcher
    R7 Fletcher does not live on a floor adjacent to Cooper.

    Where does every one live?
    '''

    logic_puzzle_setup()
    floors = [x for x in range(1,6)]
    fixed_cat(floors)
    people = [0] * 5

    permute_people = permute('baker,cooper,fletcher,miller,smith', people)
    for p in permute_people:
        category(people, p)
        if is_associated('baker', 5):               # R1
            continue
        if is_associated('cooper', 1):              # R2
            continue
        if is_associated('fletcher', 5):            # R3
            continue
        if is_associated('fletcher', 1):            # R4
            continue
        if is_below('miller', 'cooper'):            # R5
            continue
        if is_adjacent_to('smith', 'fletcher'):     # R6
            continue
        if is_adjacent_to('fletcher', 'cooper'):    # R7
            continue
        fmt1 = '%5s %10s'
        fmt2 = '%5d %10s'
        print(fmt1 % ('floor', 'person'))
        print('=' * 30)
        PrintSolution(fmt2, floors, people)


def lolla ():   #the lollapoloosa marriages problem
    '''
    ;;;;;        The Lollapalooza marriage

    ;;;;;R1      Dolly is married to Fred
    ;;;;;R2      Polly is not married to Mick
    ;;;;;R3      Holly is not married to Mick.
    ;;;;;R4      Mick is Gerard
    ;;;;;R5      George is not surnamed Grant
    ;;;;;R6      Black is not Bill
    ;;;;;R7      Fred is not Atkinson
    ;;;;;R8      George is not surnamed Atkinson
    ;;;;;R9      George drives 1937 Jaguar SS100 Roadster
    ;;;;;R10     Blacks drive a 1935 Mecedes-Benz 500K
    ;;;;;R11     lolly was in mercedes-benz
    ;;;;;R12     The Grants drive a silver arrow
    ;;;;;R13     Polly does not drive a Cord
    ;;;;;R14     Bill does not drive a 1938 Cadillac V-16 Coupe
    ;;;;;R15     Bill does not drive a 1933 Pierce Silver arrow
    '''
    logic_puzzle_setup()
    brides   = 'dolly,holly,lolly,molly,polly'.split(sep=',')
    grooms   = [0] * 5
    surnames = [0] * 5
    cars     = [0] * 5
    
    fixed_cat(brides)

    def a_solution ():
        fmt = '%11s %11s %11s %11s'
        print(fmt % ('brides', 'grooms', 'surnames', 'cars'))
        print('=' * 48)
        PrintSolution(fmt, brides, grooms, surnames, cars)

    def choose_cars ():
        nonlocal cars
        permute_cars = permute('silverarrow,mercedes,cord,jaguar,cadillac', cars)
        for p in permute_cars:
            category(cars, p)
            if is_not_associated('george', 'jaguar'):       # R9
                continue
            if is_not_associated('black', 'mercedes'):      # R10
                continue    
            if is_not_associated('lolly', 'mercedes'):      # R11
                continue
            if is_not_associated('grant', 'silverarrow'):   # R12
                continue
            if is_associated('polly', 'cord'):              # R13
                continue
            if is_associated('bill', 'cadillac'):           # R14
                continue
            if is_associated('bill', 'silverarrow'):        # R15
                continue
            a_solution()

    def choose_surnames():
        nonlocal surnames
        permute_surnames = permute('atkinson,black,bower,gerard,grant', surnames)
        for p in permute_surnames:
            category(surnames, p)
            if is_not_associated('mick', 'gerard'):   # R4
                continue
            if is_associated('george', 'grant'):      # R5
                continue
            if is_associated('bill', 'black'):        # R6
                continue
            if is_associated('fred', 'atkinson'):     # R7
                continue
            if is_associated('george', 'atkinson'):   # R8
                continue
            choose_cars ()

    permute_grooms = permute('fred,bill,boris,george,mick', grooms)
    for p in permute_grooms:
        category(grooms, p)
        if is_not_associated('dolly', 'fred'):  # R1
            continue
        if is_associated('polly', 'mick'):      # R2
            continue
        if is_associated('holly', 'mick'):      # R3
            continue
        choose_surnames()
            
def marriage ():
    '''
    marriage

            a marriage problem
            5 men:                          [paul, rob,   stan, vern, wally]
            married 1 on 1 5 women:         [anne, cathy, eve,  fran, ida]
            each on a different weekday:    [mon,  tue,   wed,  thu,  fri]
                    such that:
    R1      anne married on mon
    R2      anne not married to wally
    R3      stan married on wed
    R4      rob married on fri
    R5      rob not married to ida
    R6      vern married to fran
    R7      vern married day after eve
    '''
    logic_puzzle_setup()
    
    week = 'mon,tue,wed,thu,fri'.split(sep=',')
    grooms = week[:]
    brides = week[:]
    fixed_cat(week)
    permute_grooms = permute('paul,rob,stan,vern,wally', grooms)
    for p1 in permute_grooms:
        category(grooms, p1)
        permute_brides = permute('anne,cathy,eve,fran,ida', brides)
        for p2 in permute_brides:
            category(brides, p2)
            if is_not_associated('anne', 'mon'):    # R1
                continue
            if is_associated('anne', 'wally'):      # R2
                continue
            if is_not_associated('stan', 'wed'):    # R3
                continue
            if is_not_associated('rob', 'fri'):     # R4
                continue
            if is_associated('rob', 'ida'):         # R5
                continue
            if is_not_associated('vern', 'fran'):   # R6
                continue
            if not just_after('vern', 'eve'):       # R7
                continue
            fmt = '%6s %6s %6s'
            print(fmt % ('day', 'groom', 'bride'))
            print('=' * 20)
            PrintSolution(fmt, week, grooms, brides)
            
def sorority():
    '''
    ; Five school girls sat for an examination.
    ; Their parents -- so they thought --
    ; showed an undue degree of interest in the result.
    ; They therefore agreed that in
    ; writing home about the examination,
     ;each girl should make one true statement and
    ; one untrue statement.
    ; The relevant passages from there letters.

    ; R1 Betty: "Kitty was second in the examination. I was only third."
    ; R2 Ethel: "You'll be glad to hear that I was on top. Joan was second."
    ; R3 Joan:  "I was third, and poor old Ethel was bottom."
    ; R4 Kitty: "I came out second. Mary was only fourth."
    ; R5 Mary:  "I was fourth. Top place was taken by Betty"

    ; What in fact was the order in which the girls were placed?
    '''
    logic_puzzle_setup()
    scores = 'first,second,third,fourth,fifth'.split(sep=',')
    fixed_cat(scores)

    girls = scores[:]
    
    permute_girls = permute('betty,ethel,joan,kitty,mary', girls)
    for p in permute_girls:
        category(girls, p)
        if  is_associated('kitty', 'second') == \
            is_associated('betty', 'third'):    # R1
            continue
        if  is_associated('ethel', 'first') == \
            is_associated('joan', 'second'):    # R2
            continue
        if  is_associated('joan', 'third') == \
            is_associated('ethel', 'fifth'):    # R3
            continue
        if  is_associated('kitty', 'second') == \
            is_associated('mary', 'fourth'):    # R4
            continue
        if  is_associated('mary', 'fourth') == \
            is_associated('betty', 'first'):    # R5
            continue
        fmt = '%7s %7s'
        print(fmt % ('girl','score'))
        print('=' * 15)
        PrintSolution(fmt, girls, scores)

def yachts ():
    '''
    ; Mary Ann Moore's father has a yacht and so has each of his four friends:
    ; Colonel Downing, Mr. Hall, Sir Barnacle Hood, and Dr. Parker. Each of
    ; the five also has one daughter and each has named his yacht
    ; after the daughter
    ; of one of the others. Sir Barnacle's yacht is the Gabrielle, Mr. Moore
    ; owns the Lorna; Mr. Hall the Rosalind. The Melissa, owned by Colonel
    ; Downing is named after Sir Barnacle's daughter. Gabrielle's father owns
    ; the yacht that is named after Dr. Parker's daughter.
    ; Who is Lorna's father?
    '''
    logic_puzzle_setup()
    
    fathers = 'moore,downing,hall,hood,parker'.split(sep=',')
    fixed_cat(fathers)
    daughters = fathers[:]
    yachts = fathers[:]
    daughter_names = 'mary,gabrielle,lorna,rosalind,melissa'
    yacht_names = 'mary_yacht,gabrielle_yacht,lorna_yacht,rosalind_yacht,melissa_yacht'
    
    permute_yachts = permute(yacht_names, yachts)
    for p1 in permute_yachts:
        category(yachts, p1)
        permute_daughters = permute(daughter_names, daughters)
        for p2 in permute_daughters:
            category(daughters, p2)
            # Mary Ann Moore's father has a yacht
            if is_not_associated('moore', 'mary'):
                continue
            if is_associated('moore', 'mary_yacht'):
                continue
            # Sir Barnacle's yacht is the Gabrielle
            if is_not_associated('hood', 'gabrielle_yacht'):
                continue
            if is_associated('hood', 'gabrielle'):
                continue
            # Mr. Moore owns the Lorna
            if is_not_associated('moore', 'lorna_yacht'):
                continue
            if is_associated('moore', 'lorna'):
                continue
            # Mr. Hall the Rosalind
            if is_not_associated('hall', 'rosalind_yacht'):
                continue
            if is_associated('hall', 'rosalind'):
                continue
            # The Melissa, owned by Col. Downing is named after
            # Sir Barnacle's daughter.
            if is_not_associated('downing', 'melissa_yacht'):
                continue
            if is_not_associated('hood', 'melissa'):
                continue
            # Gabrielle's father owns the yacht that
            # is named after Dr. Parker's daughter.
            parkeridx  = idx('parker')
            yacht_name = daughters[parkeridx] + '_yacht'
            gabrielidx = idx('gabrielle')
            if yachts[gabrielidx] != yacht_name:
                continue
            if is_associated('parker', 'gabrielle'):
                continue
            fmt = '%7s %9s %19s'
            print(fmt % ('father','daughter','yacht'))
            print('=' * 35)
            PrintSolution(fmt, fathers, daughters, yachts)
            # Who is Lorna's father?
            i = idx('lorna')
            print("\nLorna's father is", fathers[i].title())


def Do_One_Or_More ():
    #help(einstein)
    print()
    einstein()
    return
# None of the functions past return are executed And are actually a
# type of error, "Dead code". However useful when you comment out the
# return
    #help(floors)
    print("\n")
    floors()
    #help(lolla)
    print("\n")
    lolla()
    #help(marriage)
    print("\n")
    marriage()
    #help(sorority)
    print("\n")
    sorority()
    #help(yachts)
    print("\n")
    yachts()


if __name__ == "__main__":
    Do_One_Or_More()
