For this script, please make sure you have the most current version of Python installed (3.11.3 as of current writing)
To install and/or update python, please visit https://www.python.org/downloads/ and follow the instructions for download and installation.

I ran this script two different ways, both on a machine running Windows 10.  The first was using Microsoft VS (Visual Studio) Code,
and the second was by double clicking the file where I had it saved on my computer.  Either method should work.

For VS Code, please download the file and open it using VS Code, or copy the code into an open window within VS Code and select "Run."

For running directly from a saved location, simply go to where you have the file saved, and double click the file.
This method will create a pop up terminal window.

Input is text based.  The game will tell you what you (the player) have for cards and will tell you the value of the Dealer's face up card,
and that they have a face down card.  You will have to manually add the value of your cards to know your total.

As mentioned, input is text based.  You will be given your initial cards and asked if you would like to hit (get another card)
or stand (not get another card).  If you choose to hit, you will be given the option to hit or stand again unless your card value
exceeds 21.  Following the completion of the game, you will be asked if you would like to play again (options are y/n).
Selecting "y" will restart the game.  Selecting "n" will end the game and exit the program.

For anyone unfamiliar with the game, the goal of Blackjack is to get as close as you can to a value of 21 without going over (referred to as a bust).
If you tie with the dealer (sometimes called a push) then the dealer automatically wins as the dealer wins all ties.

The values in Blackjack are as follows:
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
10 = 10
Jack = 10
Queen = 10
King = 10
Ace = 1 OR 11 (this depends on your current total. For example: 3 & Ace = 14, Jack & Ace = 21 (This is also blackjack depending on the jack) BUT 8 + 3 + Ace = 12)


Code inspiration for structure/syntax came from two sources:
https://www.askpython.com/python/examples/blackjack-game-using-python
https://github.com/gsamarakoon/Fun-projects-for-Python/blob/master/A%20game%20of%20BlackJack.ipynb
