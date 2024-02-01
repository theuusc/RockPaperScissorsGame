# Rock-Paper-Scissors Game

Welcome to the Rock-Paper-Scissors Game! Everyone has played a game of rock, paper, scissors at least once, and now you can try to beat the machine in this classic showdown. This project is entirely developed in Python and provides an interactive terminal interface for users.

## Index
- <a href="#-features"> Project features </a>
- <a href="#-demonstration"> Demonstration </a>
- <a href="#-playing"> How to play </a>
- <a href="#-starting"> Getting Started </a>
- <a href="#-next"> Next Steps </a>
- <a href="#-contributing"> Contributing </a>
- <a href="License"> License </a>

## Project features
- [x] The application show the options available.
- [x] The application reveal the choosed option.
- [x] The application inform the result of who won.
- [x] The application asks if the player wants to play again, if 'yes' the game reset if 'no' the game shall close.

## Demonstration
![simulation](https://github.com/theuusc/RockPaperScissorsGame/README/assets/130078547/b66dbdaa-cea6-48f9-81ad-4d216223179e)

## How to Play

1. **Welcome Message:**
   - The game starts with a welcome message displaying the available options:
     - Type `0` for Rock
     - Type `1` for Paper
     - Type `2` for Scissors

2. **Player's Turn:**
   - The player is asked to choose an option by typing `0` for Rock, `1` for Paper, or `2` for Scissors.

3. **Gameplay:**
   - The player and the computer each make their move.
   - The winner is determined based on the following rules:
     ```python
     if computer == 0:
         # Rules for Rock
         # ...

     elif computer == 1:
         # Rules for Paper
         # ...

     elif computer == 2:
         # Rules for Scissors
         # ...
     ```

4. **Game Over:**
   - After three rounds, the game is over.
   - The player is prompted to choose whether to play again.
     - Type `y` for Yes
     - Type `n` for No

## Getting Started

To try the Rock-Paper-Scissors Game, follow these steps:

1. **Access Google Drive:**
   - [Google Drive Link](https://drive.google.com/drive/folders/15SfSYauucn_aS8DY9PCT9blIsXXa2rX2)

2. **Download Project Files:**
   - Download the project files from the Google Drive link.

3. **Run the Game:**
   
   Option 1:
   - After downloading the file, open it and execute the "rpsgame".
     
   Option 2:
   - Open your terminal.
   - Navigate to the project directory.
   - Run the game using the following command:
     ```bash
     python rpsgame.py
     ```

5. **Play the Game:**
   - Follow the on-screen instructions to make your move (rock, paper, or scissors).
   - See if you can beat the computer!
  
## Next steps
- [ ] Create a graphic interface

## Contributing

Contributions to the Rock-Paper-Scissors Game are welcome! If you have ideas for improvements or would like to contribute to the code, feel free to submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute the code with appropriate attribution.
