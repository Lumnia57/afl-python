from characters import Character
from random import shuffle, seed
from typing import Tuple, List
from datetime import datetime

_NUM_COLORS = 8
_MAX_GAME = 3

amount_of_colors = {
    0: 15,
    1: 15,
    2: 15,
    3: 15,
    4: 15,
    5: 10,
    6: 10,
    7: 5
}

id_to_color = {
    0: 'red',
    1: 'yellow',
    2: 'blue',
    3: 'green',
    4: 'purple',
    5: 'pink',
    6: 'black',
    7: 'rainbow'
}

color_to_id = {
    'red': 0,
    'yellow': 1,
    'blue': 2,
    'green': 3,
    'purple': 4,
    'pink': 5,
    'black': 6,
    'rainbow': 7
}

# units are (color, value)
def generate_units():
    list_colors = range(_NUM_COLORS)
    units = [c for c in list_colors for v in range(amount_of_colors[c])]
    return units

_PREVIOUS_GUESSES = []
def is_guess_correct(guess, previous_guess) -> bool:
    # cannot guess something that has already been guessed
    if guess in _PREVIOUS_GUESSES:
        return False
    # same color and higher number
    if guess[0] == previous_guess[0] and guess[1] > previous_guess[1]:
        return True
    # different color and different number
    elif guess[0] != previous_guess[0] and guess[1] != previous_guess[1]:
        return True
    return False

def add_guess(guess) -> None:
    global _PREVIOUS_GUESSES
    _PREVIOUS_GUESSES.append(guess)

def reset_guesses() -> None:
    global _PREVIOUS_GUESSES
    _PREVIOUS_GUESSES = []

def is_callout_correct(player_calling_out: Character, other_player: Character):
    guess = other_player.guess
    print(f"{player_calling_out.name}'s dice: {player_calling_out.current_dice}")
    print(f"{other_player.name}'s dice: {other_player.current_dice}")
    total_dice = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0, 
        5: 0,
        6: 0,
        7: 0
    }
    for d in player_calling_out.current_dice:
        total_dice[d] += 1
    for d in other_player.current_dice:
        total_dice[d] += 1

    if guess[0] != color_to_id['rainbow']:
        return guess[1] > total_dice[guess[0]] + total_dice[7]
    else:
        return guess[1] > total_dice[guess[0]]

def _random_splits(lst, sizes):
    seed(datetime.now().timestamp())
    shuffle(lst)
    ret = []
    pointer = 0
    for s in sizes:
        ret.append(lst[pointer:pointer+s])
        pointer+=s
    return ret

def give_dice_to_players(player1: Character, player2: Character):
    list1, list2 = _random_splits(generate_units(), [player1.num_dice, player2.num_dice])
    player1.current_dice = UnitsList(list1)
    player2.current_dice = UnitsList(list2)

class UnitsList:
    def __init__(self, list) -> None:
        self.list = list

    def __str__(self) -> str:
        string = ""
        for v in self.list:
            string += f'{id_to_color[v]} '
        return string[:-1]
    
    def __iter__(self):
        return self.list.__iter__()
    
    def __next__(self):
        return self.list.__next__()