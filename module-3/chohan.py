
import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
Note: If you roll a total of 2 or 7, you will receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('mss: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('mss: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    total = dice1 + dice2
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = total % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Check for bonus:
    if total == 2 or total == 7:
        print(f'You rolled a total of {total}! You receive a 10 mon bonus!')
        purse += 10  # Add bonus to purse

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        house_fee = pot * 12 // 100  # 12% house fee
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    # Check if the player has run out of money:
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()


    ##Cuitlahuac Hernandez 
