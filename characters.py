import utils
from typing import Tuple
from random import randint

class Character():
    def __init__(self, name: str = 'Fucking.... John or something') -> None:
        self.name = name
        self.current_dice = []
        self.guess = (-1, -1)
        self.num_dice = 6

    def give_dice(self, dice) -> None:
        self.current_dice = dice

    def make_guess(self, guess: Tuple[int,int]) -> None:
        self.guess = guess
        utils.add_guess(guess)
        print(f"({self.name}) There are {guess[1]} {utils.id_to_color[guess[0]]} units.")

    def pick_and_make_guess(self, previous_guess: Tuple[int, int]) -> None:
        print('Generic pick_and_make_guess function called.. To override')
        pass

    def think_other_is_lying(self):
        print('Generic think_other_is_lying function called.. To override')
        pass

class PlayerCharacter(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def pick_and_make_guess(self, previous_guess: Tuple[int, int]) -> None:
        guess_color = previous_guess[0]
        guess_number = previous_guess[1]

        guess_is_correct = False
        while not guess_is_correct:
            guess_color = input(f'What is your guess (color) ? Pick from: {list(utils.id_to_color.values())} ')
            while guess_color not in utils.id_to_color.values():
                print("Incorrect, you're silly !")
                guess_color = input(f'What is your guess (color) ? Pick from: {list(utils.id_to_color.values())} ')

            guess_number = int(input(f'What is your guess (number) ? '))
            while guess_number <= 0:
                print("Incorrect, you're silly !")
                guess_number = int(input(f'What is your guess (number) ? '))

            guess_is_correct = utils.is_guess_correct((utils.color_to_id[guess_color], guess_number), previous_guess)
            if not guess_is_correct:
                print("You're guess is not correct.... do it again")
        self.make_guess((utils.color_to_id[guess_color], guess_number))

    def think_other_is_lying(self):
        choice = ''
        while choice != 'y' and choice != 'n':
            choice = input('Do you think the other player is lying ? (y/n) ')
        if choice == 'y':
            print(f'({self.name}) You are lying bitch !!!')
        return choice == 'y'

class DumbAssNpc(Character):
    def __init__(self, name: str = 'Dawn') -> None:
        super().__init__(name=name)

    def pick_and_make_guess(self, previous_guess: Tuple[int, int]) -> None:
        guess = previous_guess
        while not utils.is_guess_correct(guess, previous_guess):
            guess = (randint(0, utils._NUM_COLORS-1), randint(1, self.num_dice*2))
        self.make_guess(guess=guess)

    def think_other_is_lying(self):
        rand = randint(1,10)
        if rand <= 2:
           return True
        else:
            return False 