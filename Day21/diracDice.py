from collections import deque

position_player_one = 4
position_player_two = 10

times_dice_rolled = 0
max_score = 1000
score_player_one = 0
score_player_two = 0
result = 0

def determine_position(dice_roll_sum, player_position):
    # The position is always the last digit of the sum (0 means 10)
    last_digit = (dice_roll_sum + player_position) % 10
    if last_digit == 0:
        return 10
    else:
        return last_digit


# The dice with 100 values
deterministic_dice = list(range(1, 101))
deterministic_dice = deque(deterministic_dice)
# allows for deterministic_dice.rotate(1) to throw the dice

while result == 0:
    # Player one plays
    dice_first_throw = deterministic_dice[0]
    deterministic_dice.rotate(-1)
    dice_second_throw = deterministic_dice[0]
    deterministic_dice.rotate(-1)
    dice_third_throw = deterministic_dice[0]
    deterministic_dice.rotate(-1)
    score_player_one = determine_position(dice_first_throw + dice_second_throw + dice_third_throw, position_player_one) + score_player_one
    position_player_one = determine_position(dice_first_throw + dice_second_throw + dice_third_throw, position_player_one)
    times_dice_rolled = times_dice_rolled + 3

    if max_score < score_player_one:
        result = times_dice_rolled * score_player_two

    # Player twp plays
    dice_first_throw = deterministic_dice[0]
    deterministic_dice.rotate(-1)
    dice_second_throw = deterministic_dice[0]
    deterministic_dice.rotate(-1)
    dice_third_throw = deterministic_dice[0]
    deterministic_dice.rotate(-1)
    score_player_two = determine_position(dice_first_throw + dice_second_throw + dice_third_throw, position_player_two) + score_player_two
    position_player_two = determine_position(dice_first_throw + dice_second_throw + dice_third_throw, position_player_two)
    times_dice_rolled = times_dice_rolled + 3

    if max_score < score_player_two:
        result = times_dice_rolled * score_player_one


print(str(result))