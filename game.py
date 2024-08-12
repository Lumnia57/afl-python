import utils
import characters

print('Welcome to A Familiar Lie (Official Alpha Not Remastered (tm))')

player1 = characters.PlayerCharacter(input('What is your name ? '))
player2 = characters.DumbAssNpc()

print('FIGHT !!!!')

n_game = 1

p1_points = 0
p2_points = 0

while n_game <= utils._MAX_GAME:
    print(f'-- Beginning of game {n_game} --')
    while player1.num_dice != 0 and player2.num_dice != 0:
        utils.give_dice_to_players(player1, player2)
        utils.reset_guesses()
        continuing = True
        guess_made = False
        p1_choice_lie = False
        while continuing:
            print(f"{player1.name}'s turn..")
            print(f'Your dice: {player1.current_dice}')
            print(f'{player2.name} has {player2.num_dice} dice left')
            if guess_made:
                p1_choice_lie = player1.think_other_is_lying()

            if p1_choice_lie:
                # HANDLE LIE
                continuing = False
                win_p1 = utils.is_callout_correct(player1, player2)
                if win_p1:
                    print('Yippee ! You win !')
                    player2.num_dice -= 1
                    break
                else:
                    print('You lose :(')
                    player1.num_dice -= 1
                    break
            else:
                player1.pick_and_make_guess(player2.guess)

            if continuing:
                print(f"{player2.name}'s turn..")
                p2_choice_lie = player2.think_other_is_lying()
                if p2_choice_lie:
                    # HANDLE LIE
                    print(f'({player2.name}) You are lying !!!! #angy')
                    continuing = False
                    win_p2 = utils.is_callout_correct(player2, player1)
                    if win_p2:
                        print(f'{player2.name} wins..')
                        player1.num_dice -= 1
                        break
                    else:
                        print(f'{player2.name} loses !')
                        player2.num_dice -= 1
                        break
                else:
                    player2.pick_and_make_guess(player1.guess)
                    guess_made = True
    
    if player1.num_dice == 0:
        print(f'{player2.name} wins.. :( weeeeh')
        p2_points += 1
    elif player2.num_dice == 0:
        print(f'{player1.name} wins :) YAYYYY')
        p1_points += 1

    n_game += 1

print('End of game')

if p1_points > p2_points:
    print('You win YIPPEEEEEEEEEEEEEEEE WAHOOOOOOOOOOOOO')
else:
    print('You lose BOOOOHOOOOOHOOOO ;w;')