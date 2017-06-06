# minesweeper
Simulates the classic game "Minesweeper" in a text-based version with Python. Missing the feature of 'flagging' mines.
I was first inspired to build this in my senior year of high school for AP Comp Sci's final project, but I wasn't able to complete the project in time.

--TUTORIAL--
First, you need to enter the desired dimensions of the 'minefield' and the desired number of mines at:
\# of rows:
\# of columns:
\# of mines:

The program randomnly generates a row and column pair to be the position of a mine, as many times as the # of mines entered.

With these dimensions, the program prints the minefield. For example, a 4x5 minefield would look like this:
? ? ? ? ?
? ? ? ? ?
? ? ? ? ?
? ? ? ? ?, with the upper left corner being (0,0) and the bottom right corner being (3,4).

Then, you enter a row and column pair at:
Guess Row:
Guess Column:

If the point you guessed is a mine, the game will print the minefield with all of the mines' spots revealed as 'X's, followed by a "Game Over" message.

Otherwise, the program will update and print the minefield, revealing how many mines are adjacent to the position. If the position is adjacent to no mines, the positions adjacent to the chosen position will also have their adjacents checked.


If you guess all of the points on the 'minefield' except the mines, the game will print a "CONGRATULATIONS! You win!" message.
