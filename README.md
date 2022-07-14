# NoughtsAndCrosses
🔅🔅🔅 A simple console based python application which simulates a noughts and crosses game. This program uses a modular and Object-Oriented approach for better code readability 🔅🔅🔅

  
<p align="center">
  <img width="376" alt="Screenshot 2022-07-14 at 19 04 29" src="https://user-images.githubusercontent.com/39672050/179054749-1e6eb473-3920-405b-99e9-2633de755e19.png">
</p>

<br>
Fully modular and object approach to Noughts and Crosses. This project is to enable new learners to abstract a beginners project in a clear way.
</p>


# 🤔 Aims..

To create a Noughst and Crosses game which:
1. Allows the users to start as many games as they would like untill they want to stop.
2. Enables two players to alernatly place moves on the board using rows and columns 
3. Validates the moves and inputs of each player 
5. Ends when there is a winner or a draw


# ✨ Objects and Files 

The Prject Struture:

<img width="343" alt="Screenshot 2022-07-14 at 19 32 15" src="https://user-images.githubusercontent.com/39672050/179056830-578812b2-059b-4d14-8161-0f935349f3ab.png">

1. board.py : A class of the board which includes functions to check for the winner, updateing the board , printing the board and resetting the board
2. game_fucntions.py : this function is a module which includes functions that is used within the main class and noughts and crosses class. Essential this is a helper module to keep the main file as small as possible.
3. main.py: This is where the rounds are simulated for each round and where all classes are used to create the game.
4. noughts_and_crosses.py : This simulates 1 round of the noughts and crosses game untill a win and a draw has been found.
5. player.py : This player class is essential to create two players who can place a valid move on the board as well as tracking the turns of the game.


