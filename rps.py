import random
def menu():
     name = input("What´s your name? ")
     print(f'Welcome {name.title()}')
     print('1 Play the game, best of 5 wins.')
     print('2 Quit')

menu()
c = int(input())
ps = 0
cs = 0
while True:
    if c == 1:
        """Player Choice"""
        print("Enter your choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")
        choice = int(input())
        if choice == 1:
            player = 'Rock'
        elif choice == 2:
            player = 'Paper'
        elif choice == 3:
            player = 'Scissor'
        """Computer Choice"""
        comp_choice = random.randint(1, 3)
        if comp_choice == 1:
            computer = 'Rock'
        elif comp_choice == 2:
            computer = 'Paper'
        elif comp_choice == 3:
            computer = 'Scissor'

        """Pick a winner"""
        if choice == 1 and comp_choice == 3:
            print(f'{player} beats {computer} \n You win')
            print()
            ps += 1
        elif choice == 3 and comp_choice == 2:
            print(f'{player} beats {computer} \n You win')
            print()
            ps += 1
        elif choice == 2 and comp_choice == 1:
            print(f'{player} beats {computer} \n You win')
            print()
            ps += 1
        elif comp_choice == 1 and choice == 3:
            print(f'{player} beats {computer} \n You lose')
            print()
            cs += 1
        elif comp_choice == 3 and choice == 2:
            print(f'{player} beats {computer} \n You lose')
            print()
            cs += 1
        elif comp_choice == 2 and choice == 1:
            print(f'{player} beats {computer} \n You lose')
            print()
            cs += 1
        elif choice == comp_choice:
            print('Its a tie')
            print()

    if ps == 5:
        print(f'You Win {ps} to {cs}')
        v = input('Do you want to play again?(y/n) ').lower()
        cs = 0
        ps = 0
        if v == 'n':
            print('Thanks for playing')
            break
    elif cs == 5:
        print(f'Computer wins {cs} to {ps} ')
        v = input('Do you want to play again?(y/n) ').lower()
        cs = 0
        ps = 0
        if v == 'n':
            print('Thanks for playing')
            break
    elif c == 2:
        break












