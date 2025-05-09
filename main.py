import os
from random import randint
import time
from Models.Unit import Unit

if True:
    LandBattleQuestions = ['is the weather extremely bad? (e.g. storms)', 'is attacker in native biome?', 'is defender in native biome?', 'does the attacker have to cross a river without a bridge to reach the defender?', 'has the defender been cut off from supplies?']
    NavalBattleQuestions = ['does the defender have naval superiority in the area?', 'does the attacker have naval superiority in the area?']
    LandVsNavalBattleQuestions = ['has the defender set up fortifications?', 'has the attacker launched a bombardment before the attack?', 'is the weather extremely bad? (e.g. storms)', 'does the attacker have naval superiority in the area?']
    NavalVsLandBattleQuestions = ['is the weather extremely bad? (e.g. storms)', 'does the defender have naval superiority in the area?']
    LandBattleModifiers = [-1, 2, -2, -1, 3]
    NavalBattleModifiers = [-2, 2]
    LandVsNavalModifiers = [-2, 1, -1, 2]
    NavalVsLandModifiers = [1, -2]
    LandTroops = ['infantry', 'light infantry', 'militia', 'cavalry', 'artillery', 'mortar', 'rocket artillery']
    Tokens = [['●', '○', '◌', '₻', '‰', 'λ', '↗'], ['▴', '⌂', 'Δ', '▲', '₷']]
    Ships = ['Sloop', 'Brig', 'Frigate', 'Ship of the Line', 'Early Ironclad']
    ShipBonuses = [0, 1, 2, 4, 8]
    Bonus = 0
    AtkDieroll = 0
    DefDieroll = 0
    matrix = []
    AtkUnits = []
    DefUnits = []
    AtkDie = ['\033[31m❶\033[0m', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '❿', '⓫', '⓬', '⓭', '⓮', '⓯', '⓰', '⓱', '⓲', '⓳', '\033[32m⓴\033[0m']
    DefDie = ['\033[31m①\033[0m', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '\033[32m⑳\033[0m']
    biome = ''
    biomes = ['mountains', 'forest', 'sea', 'plains', 'desert', 'beach', 'city']
    units = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    matrix_height = 'a'
    matrix_width = 'b'
    texture = [
    r'\͞\/\/͞/ /▲\ |͞■͞>  _ __ /͞` /͞\ |\ | /͞\ | | |= (( ͞|͞',
    r' \_/\_/ /_/\\|_|\\ (O)|͞ \_, \O/ | \| \_X \_/ |_ ))  | ']

def startup():
    declare_alt_matrix()
    alt_show_matrix()
    print('''Copyright © 2025 @thenameisq. All rights reserved.
Use of this software is permitted only by members of the Discord server Winds of Change, and only within that server. 
Modification, distribution, or any other use is prohibited without the express written permission of the author.''')
    time.sleep(3)
    fadeout()

def declare_alt_matrix():
    global matrix, matrix_width
    matrix_width = max(len(line) for line in texture)
    matrix = []
    for line in texture:
        padded_line = line.ljust(matrix_width)
        matrix.append(list(padded_line))

def alt_show_matrix():
    for row in matrix:
        print("".join(row))

def fadeout():
    global matrix
    while any(char != ' ' for row in matrix for char in row):
        x = randint(0, matrix_width - 1)
        y = randint(0, 1)
        if matrix[y][x] != ' ':
            matrix[y][x] = ' '
            os.system('cls' if os.name == 'nt' else 'clear')
            alt_show_matrix()

def declare_matrix():
    global matrix, matrix_width, matrix_height, biome, biomes
    biometextures = ['\033[90m▲▲\033[0m', '\033[32m▒▒\033[0m', '\033[34m≈≈\033[0m', '\033[92m░░\033[0m', '\033[33m≈≈\033[0m', '\033[33m≈≈\033[0m', '\033[92m░░\033[0m']
    character = biometextures[biomes.index(biome)]
    matrix = []
    for a in range(matrix_height):
        row = []
        for b in range(matrix_width):
            if biome == 'beach' and b >= matrix_width / 2:
                row.append(biometextures[2])
            elif biome == 'city' and (a in range(matrix_height // 2 - 5, matrix_height // 2 + 5) and b in range(matrix_width // 2 - 5, matrix_width // 2 + 5)):
                row.append('\033[90m█\033[0m')
            else:
                row.append(character)
        matrix.append(row)

def show_matrix():
    os.system('cls' if os.name == 'nt' else 'clear')
    global matrix_width, AtkUnits, DefUnits, Atkunits, Defunits
    declare_matrix()
    for x in range(len(AtkUnits)):
        matrix[AtkUnits[x].posY][AtkUnits[x].posX] = f'\033[35m{units[x]}{Tokens[0 if Atkunits[x].unittype == 'land' else 1][LandTroops.index(AtkUnits[x].type) if  Atkunits[x].unittype == 'land' else Ships.index(AtkUnits[x].type)]}\033[0m'
    for x in range(len(DefUnits)):
        matrix[DefUnits[x].posX][DefUnits[x].posY] = f'\033[36m{units[x]}\033[0m'
    print(f'\033[90m╔{'═' * matrix_width * 2}╗\033[0m')
    for row in matrix:
        print(f'\033[90m║\033[0m{"".join(row)}\033[90m║\033[0m')
    print(f'\033[90m╚{'═' * matrix_width * 2}╝\033[0m')

def add_troop():
    global biome, units, ships, LandTroops, matrix_height, matrix_width
    unittype = ''
    while not (unittype == 'land' or unittype == 'sea'):
        unittype = input('choose unit type: "land" or "sea". you know the drill.') if biome == 'beach' else 'land' if biome != 'sea' else 'sea'
    print(f'the field is {matrix_width} characters wide, and {matrix_height} characters high.')
    while True:
        try:
            X = int(input('X location on map(both axes start from 0 in the top-right corner and increase from there):'))
            Y = int(input('Y location on map:'))
            if X >= matrix_width or X < 0 or Y >= matrix_height or Y < 0:
                raise RuntimeError('invalid coordinates')
            else:
                break
        except RuntimeError as e:
            input(str(e))
    if unittype == 'sea':
        for x in Ships:
            print(x)
        Type = ''
        while not Type in Ships:
            Type = input('choose ship type. you know the drill: copy-paste.')
    else:
        for x in LandTroops:
            print(x)
        Type = ''
        while not Type in LandTroops:
            Type = input('choose troop type. you know the drill: copy-paste.')
    unit = Unit(X, Y, unittype, Type)
    if 'def' in input('add to \033[36mDefense\033[0m or \033[35mOffense\033[0m?').lower():
        DefUnits.append(unit)
    else:
        AtkUnits.append(unit)

def dieroll():
    global AtkDieroll, DefDieroll
    DieMax = 20
    for x in range(randint(20, 50)):
        os.system('cls' if os.name == 'nt' else 'clear')
        AtkDieroll = randint(0, DieMax - 1)
        DefDieroll = randint(0, DieMax - 1)
        print(f'\033[35mAttacker:{AtkDie[AtkDieroll]}\033[36mDefender:{DefDie[DefDieroll]}\033[0m')
        time.sleep(0.05)

def checkUnits(unitList, attributeToCheck, expectedValue):
    if attributeToCheck == 'unitType':
        for x in unitList:
            if x.unitType == expectedValue:
                return True
        return False
    else:
        for x in unitList:
            if x.type == expectedValue:
                return True
        return False

def fight():
    global Ships, ShipBonuses, Bonus, LandBattleQuestions, NavalBattleQuestions, LandVsNavalBattleQuestions, LandBattleModifiers, NavalBattleModifiers, LandVsNavalModifiers, AtkDie, DefDie, AtkDieroll, DefDieroll, AtkUnits, DefUnits, units, biome
    while True:
        try:
            Attacker = AtkUnits[units.index(input('select attacker (u know the drill):'))]
            Defender = DefUnits[units.index(input('select defender:'))]
            Bonus += int(input('morale points attacker:'))
            Bonus -= int(input('morale points defender:'))
            Bonus += int(input('doctrine bonus attacker:'))
            Bonus -= int(input('doctrine bonus defender:'))
        except:
            print('how did you fuck this part up? womp womp')
            return 'crash'
        else:
            break
    if Attacker.unitType == 'land' and Defender.unitType == 'land':
        situation = 1
    elif Attacker.unitType == 'sea' and Defender.unitType == 'sea':
        situation = 2
    elif Attacker.unitType == 'sea' and Defender.unitType == 'land':
        situation = 3
    elif Attacker.unitType == 'land' and Defender.unitType == 'sea':
        situation = 4
    if 1 == situation:
        if biome == 'beach':
            if checkUnits(AtkUnits, 'unitType', 'sea'):
                Bonus += 1
            if checkUnits(DefUnits, 'unitType', 'sea'):
                Bonus -= 1
            if Attacker['type'] == 'cavalry':
                Bonus -= 2
            if Defender['type'] == 'cavalry':
                Bonus += 2
        if checkUnits(AtkUnits, 'type', 'artillery'):
            Bonus += 2
        if checkUnits(DefUnits, 'type', 'artillery'):
            Bonus -= 2
        if biome == 'mountains':
            Bonus -= 2
            if Attacker['type'] == 'cavalry':
                Bonus -= 1
            elif Attacker['type'] == 'artillery' or Attacker['type'] == 'mortar' or Attacker['type'] == 'rocket artillery':
                Bonus += 1
            if Defender['type'] == 'cavalry':
                Bonus += 1
            elif Defender['type'] == 'artillery' or Defender['type'] == 'mortar' or Defender['type'] == 'rocket artillery':
                Bonus -= 1
        elif biome == 'forest' or biome == 'city':
            Bonus -= 1
        elif biome == 'desert':
            if Attacker['type'] == 'cavalry':
                Bonus -= 2
            if Defender['type'] == 'cavalry':
                Bonus += 2
        elif biome == 'city':
            Bonus -= int(input('enter the level of fortifications made to the city(0-4):'))
        Questions = LandBattleQuestions
        Bonuses = LandBattleModifiers
    elif 2 == situation:
        Questions = NavalBattleQuestions
        Bonuses = NavalBattleModifiers
        for x in Ships:
            print(x)
        Bonus += ShipBonuses[Ships.index(Attacker['type'])]
        Bonus -= ShipBonuses[Ships.index(Defender['type'])]
    elif 3 == situation:
        Questions = LandVsNavalBattleQuestions
        Bonuses = LandVsNavalModifiers
        Bonus += ShipBonuses[Ships.index(Attacker['type'])]
    else:
        Questions = NavalVsLandBattleQuestions
        Bonuses = NavalVsLandModifiers
        Bonus -= ShipBonuses[Ships.index(Defender['type'])]
    for x in range(len(Questions)):
        if 'y' in input(f'{Questions[x]}(y/n)'):
            Bonus += Bonuses[x]
    input('press enter when ready.')
    dieroll()
    result = AtkDieroll - DefDieroll + Bonus
    if result < 0:
        if abs(result) > 7:
            AtkUnits.remove(Attacker)
        input(f'the defender won with a difference of {abs(result)}! {'The attacker has been killed.' if abs(result) > 7 else ''}')
    elif result > 0:
        if result > 7:
            DefUnits.remove(Defender)
        input(f'the attacker won with a difference of {abs(result)}! {'The defender has been killed.' if result > 7 else ''}')
    else:
        input("it's a tie!")

def init():
    global biome, biomes, matrix_height, matrix_width
    for x in biomes:
        print(x)
    while not biome in biomes:
        biome = input('choose biome. (tip:copy-paste the name)')
    while not (isinstance(matrix_height, int) and isinstance(matrix_width, int)):
        matrix_height = int(input('height of battlefield:'))
        matrix_width = int(input('width of battlefield:'))
    declare_matrix()

def show_stats():
    global AtkUnits, DefUnits, units
    print('\033[35mAttacker:\033[0m')
    for x in range(len(AtkUnits)):
        print(f'\033[35m{units[x]}:\033[0m{AtkUnits[x - 1].type}')
    print('\033[36mDefender:\033[0m')
    for x in range(len(DefUnits)):
        print(f'\033[36m{units[x]}:\033[0m{DefUnits[x - 1].type}')
    input('press enter to continue...')

def move_troops():
    global AtkUnits, DefUnits, units, matrix_height, matrix_width
    letter = input("give the piece's letter:")[0]
    while True:
        try:
            y = int(input('enter new y position:'))
            x = int(input('enter new x position:'))
            if x >= matrix_width or x < 0 or y >= matrix_height or y < 0:
                raise RuntimeError('invalid coordinates')
        except RuntimeError as e:
            print(str(e))
        else:
            break
    if 'def' in input('Defender or attacker?').lower():
        DefUnits[units.index(letter)].update_coords(x, y)
    else:
        AtkUnits[units.index(letter)].update_coords(x, y)

try:
    startup()
    init()
    while True:
        show_matrix()
        Action = input('''choose action to take: 
c: show credits
end: end program
1: add unit
2: fight
3: move troops
4: show troop stats
''')
        if '1' in Action:
            add_troop()
        elif 'c' in Action:
            print('war system made for the Winds Of Change discord server.')
            print('original rules by @echo52541 on discord')
            print('coded by @thenameisq on discord.')
            input('press enter to continue...')
        elif '2' in Action:
            fight()
        elif '3' in Action:
            move_troops()
        elif 'end' in Action:
            break
        else: 
            show_stats()
except Exception as e:
    print(str(e))
    input('something crashed. please report how you crashed it to @thenameisq on discord. thanks!')