# Battleships: Solo.

Battleships: Solo is a unique take on the old school strategy game of Battleships. Battleships: Solo is a single player game where the user is playing against a board of warships and trying to locate, hit and sink the enemies in the amount of moves given.

Battleships: Solo has no specific audience as the game is easily understandable and clear for all ages, as long as you have a spare hour to compensate for the addictiveness.

## Features.

 - ### First Instance.
   - Battleships: Solo start off with a welcoming message that instantly brings interactivity towards game and user.
   - Information and a brief summary of the rules are presented underneath for a clear understanding of the way the game will run.
   - Having a legend in the start up is also a huge bonus for the game as it dissmisses any confusion the player may have if heading into the game without previous playtime.
   - Username input is the last on the starting screen as it connects the player to the game.
     - After entering the username, another message is granted by motivating the player for the battle ahead.
    
img

 - ### Game Begins.
   - After initial start up, Battleships: Solo requests coordinates for your first strike in the coordinates.
  
img

 - ### Board & Ships.
   - The board is presented to the player with a 10 x 10 square full of `~` waves and a x-axis, y-axis labelled with numbers.
     - The numbers provided correlate with the coordinates needed to type into the game.
   - Battleships are randomised onto the board in quantites of `[5, 4, 4, 3, 2, 2]` and also face in the various North, East, South, West directions.
   - As mentioned in the legend, the board has `~` for waves and untouched areas, `-` for misses, `x` for battleships hit and `@` for sunken battleships.

img

 - ### Input Feedback.
   - Incorporating a variety of messages that cover every aspect of input data when playing the game ensures no confusion or poor gaming experience.
     - For guesses that are under `0` or guesses exceeding `99` the game suggests coordinates between `0` and `99`.
     - For guesses that are either symbols, letters or words; the game provides a message stating to use coordinates between `0` and `99`
     - For guesses that have already been previously made the game informs the player of their mistakes and asks for another.

img

 - ### Experience.
   - Battleships: Solo offers the player 50 chances to sink all the generated ships on the board.
     - When all ships have been sunk succdssfully within the limit a congratulations message appears.
     - If the player fails to sink all the ships in the given limit, the game resets and waits until it is rerun for another try.

img

 - ### Future Features.
   - The most obvious future feature would be to include an additional board so the game becomes a PVC (Player vs Computer).
     - This would expand the game and definitely build more gaming relations towards the user as the experience is more competitive.
   - In unique various of the Battleship games, bonus features such as air strikes and UAVs are incorporated that will bring more attention towards the game.
     - This would result in a more interactive experience for the player and would encourage playtime.

## Testing.

 - Putting the code for Battleships: Sollo into the [PEP8 Linter] and passing first time with a few warnings of spacing, layout issues.
   - Quick changes to the layout resulted in 100%, passing with flying colours.
 - Testing the game also through the **Heroku** terminal when deployed.

 - ### Deployment.
   - The deployment of Battleships: Solo was through the mock terminal created by Code Institute on Heroku.
     - There are multiple steps for this process and they are as follows:
       - Create a new Heroku app on the **Heroku** site.
       - Set the config var to key - `PORT` and value - `8000`.
       - Set the buildbacks to `Python` and `NodeJS` in that specific order.
       - Link Heroku to the repository. For example, **GitHub***.
       - Deploy.

 - ### Bugs.
   - Bugs encountered throughout the process where inevitable as this was the first `Python` project however, the main bugs where to do with carless coding.
     - For example, forgetting to return the battleships after altering the lists from the function. This was resolved after disecting the code to find the problem.
     - Another bug was arose in the `while` loop where the output wanted was `True` and was recieving `False`. This was resolved after understanding the inital miss input that was erorring the code.

 - ### Unfixed Bugs.
   - When the battleships are randomised and generated onto the board, they sometimes have the possibility of passing from `9` to `0`.
     - This is a bug that has not been resloved as troubleshooting and trying to achieve helo came to no avail.
       - There will of course be a way to fix this and it is to do with the `%` operator however, this was a piece of code that could be better. As a sly solution (which is not the correct solution) the board could be interpreted as a sphere and therefore the placements of the boats become logical and the bug is no more.

## Credits.

 - ### Content.
   - The idea for creating a unique version of the Battleships game came from the assesment guide.
         
