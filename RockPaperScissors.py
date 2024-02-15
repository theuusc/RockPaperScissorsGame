import PySimpleGUI as sg
from random import randint
from time import sleep

sg.theme('DarkAmber')

# Game initialization
def main():
    items = ("Rock", "Paper", "Scissors")
    player_score = 0
    computer_score = 0

# GUI layout
    layout = [
        [sg.Text('Welcome to the Rock-Paper-Scissors game')],
        [sg.Button('Rock', key='Rock', size=(8, 2)), sg.Button('Paper', key='Paper', size=(8, 2)), sg.Button('Scissors', key='Scissors', size=(8, 2))],
        [sg.Multiline('', size=(30, 5), key='result')],
        [sg.Text(f'Score: Player - {player_score} | Computer - {computer_score}', size=(30, 1), key='score')],
        [sg.Button('Play Again'), sg.Button('Exit')]
    ]

# Create window
    window = sg.Window('Rock-Paper-Scissors Game', layout)

    while True:  # Event handling
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):   # Handle window closure or exit button
            break

        if event in ('Rock', 'Paper', 'Scissors'): # Handle user's choice
            player = items.index(event)
            computer = randint(0, 2)

            animate_choices(window, 'ROCK', 'PAPER', 'SCISSORS', sleep_duration=1)  # Animate computer's choice

            result_text = f"\nThe computer chose {items[computer]}\nThe player chose {items[player]}\n" # Display choices and determine winner
            window['result'].update(result_text)

            winner = determine_winner(player, computer)
            window['result'].update(winner + '\n')

            if winner != "IT'S A TIE":  # Update score if there is a winner
                player_score, computer_score = update_score(window, winner, player_score, computer_score)
            
        if event == 'Play Again': # Handle play again button
            window['result'].update('')
            player_score = 0
            computer_score = 0
            window['score'].update(f'Score: Player - {player_score} | Computer - {computer_score}')
        elif event == 'Exit':
            break
# Close the window
    window.close()

# Determine the winner of the game
def determine_winner(player, computer):
    if player == computer:
        return "IT'S A TIE"
    elif (player + 1) % 3 == computer:
        return "COMPUTER WON"
    else:
        return "PLAYER WON"

# Update the scores based on the game result
def update_score(window, winner, player_score, computer_score):
    if winner == "PLAYER WON":
        player_score += 1
    elif winner == "COMPUTER WON":
        computer_score += 1

    window['score'].update(f'Score: Player - {player_score} | Computer - {computer_score}')

    return player_score, computer_score

# Animate choices for a more interactive experience
def animate_choices(window, *choices, sleep_duration):
    for choice in choices:
        window['result'].update('')
        window.refresh()
        sleep(sleep_duration)
        window['result'].update(choice)
        window.refresh()
        sleep(sleep_duration)

# Entry point of the script
if __name__ == "__main__":
    main()
