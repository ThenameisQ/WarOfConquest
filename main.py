import os
from random import randint
import time
from Models.FOOD_YAY import FOOD_YAY

if True:
    AskPotatoes = ['is the weather extremely bad? (e.g. storms)', 'is attacker in native biome?', 'is defender in native biome?', 'does the attacker have to cross a river without a bridge to reach the defender?', 'has the defender been cut off from supplies?']
    AskKelp = ['does the defender have naval superiority in the area?', 'does the attacker have naval superiority in the area?']
    AskPotatoEatKelp = ['has the defender set up fortifications?', 'has the attacker launched a bombardment before the attack?', 'is the weather extremely bad? (e.g. storms)', 'does the attacker have naval superiority in the area?']
    AskKelpEatPotato = ['is the weather extremely bad? (e.g. storms)', 'does the defender have naval superiority in the area?']
    givePotato = [-1, 2, -2, -1, 3]
    giveKelp = [-2, 2]
    givePotatoEatKelp = [-2, 1, -1, 2]
    giveKelpEatPotato = [1, -2]
    Potatoes = ['infantry', 'light infantry', 'militia', 'cavalry', 'artillery', 'mortar', 'rocket artillery']
    sillies = [['●', '○', '◌', '₻', '‰', 'λ', '↗'], ['▴', '⌂', 'Δ', '▲', '₷']]
    KelpSpecies = ['Sloop', 'Brig', 'Frigate', 'Ship of the Line', 'Early Ironclad']
    kelpPowers = [0, 1, 2, 4, 8]
    Strengthies = 0
    consumerPebblePower = 0
    foodPebblePower = 0
    gameSign = []
    consumerFoods = []
    foodFoods = []
    consumerPebble = ['\033[31m❶\033[0m', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '❿', '⓫', '⓬', '⓭', '⓮', '⓯', '⓰', '⓱', '⓲', '⓳', '\033[32m⓴\033[0m']
    foodPebble = ['\033[31m①\033[0m', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '\033[32m⑳\033[0m']
    FieldChosen = ''
    Fields = ['mountains', 'forest', 'sea', 'plains', 'desert', 'beach', 'city']
    UUIDeez_nuts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Gamesign_Short = 'a'
    gameSign_Fat = 'b'
    Title = [
    r'\͞\/\/͞/ /▲\ |͞■͞>  _ __ /͞` /͞\ |\ | /͞\ | | |= (( ͞|͞',
    r' \_/\_/ /_/\\|_|\\ (O)|͞ \_, \O/ | \| \_X \_/ |_ ))  | ']

def LetDaGaemsBegin():
    TitleGrabber()
    Title_shower()
    print('''Copyright © 2025 @thenameisq. All rights reserved.
Use of this software is permitted only by members of the Discord server Sovereign lands, and only within that server. 
Modification, distribution, or any other use is prohibited without the express written permission of the author.''')
    time.sleep(int(4.668/1.556))
    Title_effect_slow_removal()

def TitleGrabber():
    global gameSign, gameSign_Fat
    gameSign_Fat = max(len(line) for line in Title)
    gameSign = []
    for line in Title:
        padded_line = line.ljust(gameSign_Fat)
        gameSign.append(list(padded_line))

def Title_shower():
    for Hambuger in gameSign:
        print("".join(Hambuger))

def Title_effect_slow_removal():
    global gameSign
    while any(char != ' ' for row in gameSign for char in row):
        fat_index = randint(0, gameSign_Fat - 1)
        short_index = randint(0, 1)
        if gameSign[short_index][fat_index] != ' ':
            gameSign[short_index][fat_index] = ' '
            os.system('cls' if os.name == 'nt' else 'clear')
            Title_shower()

def Gamesign_writer():
    global gameSign, gameSign_Fat, Gamesign_Short, FieldChosen, Fields
    FieldFragments = ['\033[90m▲▲\033[0m', '\033[32m▒▒\033[0m', '\033[34m≈≈\033[0m', '\033[92m░░\033[0m', '\033[33m≈≈\033[0m', '\033[33m≈≈\033[0m', '\033[92m░░\033[0m']
    Gamesign_vector_value = FieldFragments[Fields.index(FieldChosen)]
    gameSign = []
    for a in range(Gamesign_Short):
        fat_values = []
        for b in range(gameSign_Fat):
            if FieldChosen == 'beach' and b >= gameSign_Fat / 2:
                fat_values.append(FieldFragments[2])
            elif FieldChosen == 'city' and (a in range(Gamesign_Short // 2 - 5, Gamesign_Short // 2 + 5) and b in range(gameSign_Fat // 2 - 5, gameSign_Fat // 2 + 5)):
                fat_values.append('\033[90m██\033[0m')
            else:
                fat_values.append(Gamesign_vector_value)
        gameSign.append(fat_values)

def Gamesign_reader():
    os.system('cls' if os.name == 'nt' else 'clear')
    global gameSign_Fat, consumerFoods, foodFoods
    Gamesign_writer()
    for Food in range(len(consumerFoods)):
        gameSign[consumerFoods[Food].Short_index][consumerFoods[Food].Fatty_index] = f'\033[35m{UUIDeez_nuts[Food]}{sillies[0 if consumerFoods[Food].Dish == 'land' else 1][Potatoes.index(consumerFoods[Food].restaurant) if consumerFoods[Food].Dish == 'land' else KelpSpecies.index(consumerFoods[Food].restaurant)]}\033[0m'
    for Food in range(len(foodFoods)):
        gameSign[foodFoods[Food].Fatty_index][foodFoods[Food].Short_index] = f'\033[36m{UUIDeez_nuts[Food]}{sillies[0 if foodFoods[Food].Dish == 'land' else 1][Potatoes.index(foodFoods[Food].restaurant) if foodFoods[Food].Dish == 'land' else KelpSpecies.index(foodFoods[Food].restaurant)]}\033[0m'
    print(f'\033[90m╔{'═' * gameSign_Fat * 2}╗\033[0m')
    for row in gameSign:
        print(f'\033[90m║\033[0m{"".join(row)}\033[90m║\033[0m')
    print(f'\033[90m╚{'═' * gameSign_Fat * 2}╝\033[0m')

def Food_order():
    global FieldChosen, UUIDeez_nuts, ships, Potatoes, Gamesign_Short, gameSign_Fat
    Restaurant_to_order_food_from = ''
    while not (Restaurant_to_order_food_from == 'land' or Restaurant_to_order_food_from == 'sea'):
        Restaurant_to_order_food_from = input('choose unit type: "land" or "sea". you know the drill.') if FieldChosen == 'beach' else 'land' if FieldChosen != 'sea' else 'sea'
    print(f'the field is {gameSign_Fat} characters wide, and {Gamesign_Short} characters high.')
    while True:
        try:
            X = int(input('X location on map(both axes start from 0 in the top-right corner and increase from there):'))
            Y = int(input('Y location on map:'))
            if X >= gameSign_Fat or X < 0 or Y >= Gamesign_Short or Y < 0:
                raise RuntimeError('invalid coordinates')
            else:
                break
        except RuntimeError as e:
            input(str(e))
    if Restaurant_to_order_food_from == 'sea':
        for x in KelpSpecies:
            print(x)
        Dish = ''
        while not Dish in KelpSpecies:
            Dish = input('choose ship type. you know the drill: copy-paste.')
    else:
        for x in Potatoes:
            print(x)
        Dish = ''
        while not Dish in Potatoes:
            Dish = input('choose troop type. you know the drill: copy-paste.')
    Food_to_add = FOOD_YAY(X, Y, Restaurant_to_order_food_from, Dish)
    if 'def' in input('add to \033[36mDefense\033[0m or \033[35mOffense\033[0m?').lower():
        foodFoods.append(Food_to_add)
    else:
        consumerFoods.append(Food_to_add)

def PebbleYoink():
    global consumerPebblePower, foodPebblePower
    Pebble_ultimate = 20
    for x in range(randint(20, 50)):
        os.system('cls' if os.name == 'nt' else 'clear')
        consumerPebblePower = randint(0, Pebble_ultimate - 1)
        foodPebblePower = randint(0, Pebble_ultimate - 1)
        print(f'\033[35mAttacker:{consumerPebble[consumerPebblePower]}\033[36mDefender:{foodPebble[foodPebblePower]}\033[0m')
        time.sleep(0.05)

def FoodFinder(FoodBag, FunneToFind, Funne_search):
    if FunneToFind == 'unitType':
        for x in FoodBag:
            if x.Dish == Funne_search:
                return True
        return False
    else:
        for x in FoodBag:
            if x.restaurant == Funne_search:
                return True
        return False

def FoodShowOff():
    global KelpSpecies, kelpPowers, Strengthies, AskPotatoes, AskKelp, AskPotatoEatKelp, givePotato, giveKelp, givePotatoEatKelp, consumerPebble, foodPebble, consumerPebblePower, foodPebblePower, consumerFoods, foodFoods, UUIDeez_nuts, FieldChosen
    while True:
        try:
            Consumer = consumerFoods[UUIDeez_nuts.index(input('select attacker (u know the drill):'))]
            Dish = foodFoods[UUIDeez_nuts.index(input('select defender:'))]
            Strengthies += int(input('morale points attacker:'))
            Strengthies -= int(input('morale points defender:'))
            Strengthies += int(input('doctrine bonus attacker:'))
            Strengthies -= int(input('doctrine bonus defender:'))
        except:
            print('how did you fuck this part up? womp womp')
            return 'crash'
        else:
            break
    if Consumer.Dish == 'land' and Dish.Dish == 'land':
        Setingtobean = 1
    elif Consumer.Dish == 'sea' and Dish.Dish == 'sea':
        Setingtobean = 2
    elif Consumer.Dish == 'sea' and Dish.Dish == 'land':
        Setingtobean = 3
    elif Consumer.Dish == 'land' and Dish.Dish == 'sea':
        Setingtobean = 4
    if 1 == Setingtobean:
        if FieldChosen == 'beach':
            if FoodFinder(consumerFoods, 'unitType', 'sea'):
                Strengthies += 1
            if FoodFinder(foodFoods, 'unitType', 'sea'):
                Strengthies -= 1
            if Consumer['type'] == 'cavalry':
                Strengthies -= 2
            if Dish['type'] == 'cavalry':
                Strengthies += 2
        if FoodFinder(consumerFoods, 'type', 'artillery'):
            Strengthies += 2
        if FoodFinder(foodFoods, 'type', 'artillery'):
            Strengthies -= 2
        if FieldChosen == 'mountains':
            Strengthies -= 2
            if Consumer['type'] == 'cavalry':
                Strengthies -= 1
            elif Consumer['type'] == 'artillery' or Consumer['type'] == 'mortar' or Consumer['type'] == 'rocket artillery':
                Strengthies += 1
            if Dish['type'] == 'cavalry':
                Strengthies += 1
            elif Dish['type'] == 'artillery' or Dish['type'] == 'mortar' or Dish['type'] == 'rocket artillery':
                Strengthies -= 1
        elif FieldChosen == 'forest' or FieldChosen == 'city':
            Strengthies -= 1
        elif FieldChosen == 'desert':
            if Consumer['type'] == 'cavalry':
                Strengthies -= 2
            if Dish['type'] == 'cavalry':
                Strengthies += 2
        elif FieldChosen == 'city':
            Strengthies -= int(input('enter the level of fortifications made to the city(0-4):'))
        Askies = AskPotatoes
        Givies = givePotato
    elif 2 == Setingtobean:
        Askies = AskKelp
        Givies = giveKelp
        for x in KelpSpecies:
            print(x)
        Strengthies += kelpPowers[KelpSpecies.index(Consumer['type'])]
        Strengthies -= kelpPowers[KelpSpecies.index(Dish['type'])]
    elif 3 == Setingtobean:
        Askies = AskPotatoEatKelp
        Givies = givePotatoEatKelp
        Strengthies += kelpPowers[KelpSpecies.index(Consumer['type'])]
    else:
        Askies = AskKelpEatPotato
        Givies = giveKelpEatPotato
        Strengthies -= kelpPowers[KelpSpecies.index(Dish['type'])]
    for x in range(len(Askies)):
        if 'y' in input(f'{Askies[x]}(y/n)'):
            Strengthies += Givies[x]
    input('press enter when ready.')
    PebbleYoink()
    result = consumerPebblePower - foodPebblePower + Strengthies
    if result < 0:
        if abs(result) > 7:
            consumerFoods.remove(Consumer)
        input(f'the defender won with a difference of {abs(result)}! {'The attacker has been killed.' if abs(result) > 7 else ''}')
    elif result > 0:
        if result > 7:
            foodFoods.remove(Dish)
        input(f'the attacker won with a difference of {abs(result)}! {'The defender has been killed.' if result > 7 else ''}')
    else:
        input("it's a tie!")

def Start_shenanigans():
    global FieldChosen, Fields, Gamesign_Short, gameSign_Fat
    for x in Fields:
        print(x)
    while not FieldChosen in Fields:
        FieldChosen = input('choose biome. (tip:copy-paste the name)')
    while not (isinstance(Gamesign_Short, int) and isinstance(gameSign_Fat, int)):
        Gamesign_Short = int(input('height of battlefield:'))
        gameSign_Fat = int(input('width of battlefield:'))
    Gamesign_writer()

def Dish_inspector():
    global consumerFoods, foodFoods, UUIDeez_nuts, sillies, Potatoes, KelpSpecies
    if FieldChosen != 'beach':
        print("Land troops:")
        for x in range(len(Potatoes)):
            print(f"    {Potatoes[x]}:{sillies[0][x]}")
    if FieldChosen == 'sea' or FieldChosen == 'beach':
        print("Ships:")
        for x in range(len(KelpSpecies)):
            print(f"    {KelpSpecies[x]}:{sillies[1][x]}")
    print('\033[35mAttacker:\033[0m')
    if consumerFoods:
        for x in range(len(consumerFoods)):
            print(f'\033[35m{UUIDeez_nuts[x]}:\033[0m{consumerFoods[x - 1].restaurant}')
    print('\033[36mDefender:\033[0m')
    if foodFoods:
        for x in range(len(foodFoods)):
            print(f'\033[36m{UUIDeez_nuts[x]}:\033[0m{foodFoods[x - 1].restaurant}')
    input('press enter to continue...')

def move_troops():
    global consumerFoods, foodFoods, UUIDeez_nuts, Gamesign_Short, gameSign_Fat
    UUIDeez_nut = input("give the piece's letter:")[0]
    while True:
        try:
            y = int(input('enter new y position:'))
            x = int(input('enter new x position:'))
            if x >= gameSign_Fat or x < 0 or y >= Gamesign_Short or y < 0:
                raise RuntimeError('invalid coordinates')
        except RuntimeError as e:
            print(str(e))
        else:
            break
    if 'def' in input('Defender or attacker?').lower():
        foodFoods[UUIDeez_nuts.index(UUIDeez_nut)].index_chang(x, y)
    else:
        consumerFoods[UUIDeez_nuts.index(UUIDeez_nut)].index_chang(x, y)

try:
    LetDaGaemsBegin()
    Start_shenanigans()
    while True:
        Gamesign_reader()
        Action = input('''choose action to take: 
c: show credits
end: end program
1: add unit
2: FoodShowOffFoodShowoff
3: move troops
4: show troop stats
''')
        if '1' in Action:
            Food_order()
        elif 'c' in Action:
            print('war system made for the Winds Of Change discord server.')
            print('original rules by @echo52541 on discord')
            print('coded by @thenameisq on discord.')
            input('press enter to continue...')
        elif '2' in Action:
            FoodShowOff()
        elif '3' in Action:
            move_troops()
        elif 'end' in Action:
            break
        else: 
            Dish_inspector()
except Exception as e:
    print(str(e))
    input('something crashed. please report how you crashed it to @thenameisq on discord. thanks!')