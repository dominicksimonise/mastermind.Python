import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        valid_guess = True
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                valid_guess = False
                break
        if valid_guess:
            break
    return guess

def check_code(guess, real_code):
    correct_pos = sum(1 for guess_color, real_color in zip(guess, real_code) if guess_color == real_color)
    incorrect_pos = sum(min(guess.count(color), real_code.count(color)) for color in COLORS) - correct_pos
    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code.")
    print("The valid colors are", COLORS)
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        player_guess = guess_code()
        correct_pos, incorrect_pos = check_code(player_guess, code)
        print(f"Attempt {attempt}/{TRIES}: Correct Position: {correct_pos} | Incorrect Positions: {incorrect_pos}")
        if correct_pos == CODE_LENGTH:
            print(f"Congratulations! You guessed the code in {attempt} tries!")
            break
    else:
        print("You ran out of tries. The code was:", *code)

if __name__ == "__main__":
    game()
