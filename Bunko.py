import doctest


import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def roll_one_die() -> int:
    """ 
    Simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    
    die = random.randint(MIN_ROLL, MAX_ROLL)


    return die
   

WIN_SCORE = 21
REGULAR_SCORE = 5
LOW_SCORE = 1

def take_turn(name: str, current_points: int, round_number: int)->int:
    """
    Repeatedly simulates the roll of the three dice, calculates the roll score 
    and adds the roll score to the players current points. It ontinues to do 
    this until the player has a roll score that is worth 0 or the player 
    has accrued at least 21 total points. Returns the updated total number
    of points the player has accrued
    """
    print('Player', name, 'is taking a turn in round', round_number)
    
    rolls_score = 1
    while rolls_score != 0 and current_points < 21:
        rolls = []
        for i in range(3):
            roll_initialization = roll_one_die()
            rolls.append(roll_initialization)
        print('Three dice rolled: ', rolls[0], rolls[1], rolls[2])

        rolls_score = 0
        if rolls[0] == rolls[1] and rolls [1] == rolls[2] \
           and rolls[0] == round_number:
            rolls_score += WIN_SCORE
        elif rolls[0] == rolls[1] and rolls [1] == rolls[2] \
             and rolls[0] != round_number:
            rolls_score += REGULAR_SCORE
        else:
            if rolls[0] == round_number:
                rolls_score += LOW_SCORE
            if rolls[1] == round_number:
                rolls_score += LOW_SCORE
            if rolls[2] == round_number:
                rolls_score += LOW_SCORE
        print('scored: ', rolls_score)
    
        current_points += rolls_score
        print('Total points: ', current_points)
    return current_points
    
    
def play_round(player_1: str, player_2: str, round_number: int)->str:
    """
    Alternates turns starting with the first player until one of the players 
    reaches at least 21 points. The round stops immediately when a player 
    reaches 21, not allowing the other player to have another turn. Returns
    the name of the winner of the round
    """
    p_1_points = 0
    p_2_points = 0
    
   
    while p_1_points < 21 and p_2_points < 21:
        p_1_points = take_turn(player_1, p_1_points, round_number)
        if p_1_points < 21:
            p_2_points = take_turn(player_2, p_2_points, round_number)
    
    if p_1_points >= p_2_points:
        winner = player_1
    elif p_2_points >= p_1_points:
        winner = player_2
    
    if p_1_points >= 21:
        winner = player_1
    else:
        winner = player_2

    print(f'''the winner of this round is: {winner}
{player_1} has {p_1_points} points and {player_2} has {p_2_points} points''')    
    
    return (winner)
