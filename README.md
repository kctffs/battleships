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

<img width="740" alt="Start Screen" src="https://github.com/user-attachments/assets/7f342348-6f86-4b51-a17a-56680c987fc8">

 - ### Game Begins.
   - After initial start up, Battleships: Solo requests coordinates for your first strike in the coordinates.

![welcome-player](https://github.com/kctffs/battleships/assets/155545578/a5478ce7-1478-42c8-8c38-3132885677ad)

 - ### Board & Ships.
   - The board is presented to the player with a 10 x 10 square full of `~` waves and a x-axis, y-axis labelled with numbers.
     - The numbers provided correlate with the coordinates needed to type into the game.
   - Battleships are randomised onto the board in quantites of `[5, 4, 4, 3, 2, 2]` and also face in the various North, East, South, West directions.
   - As mentioned in the legend, the board has `~` for waves and untouched areas, `-` for misses, `x` for battleships hit and `@` for sunken battleships.

![sunk-ship](https://github.com/kctffs/battleships/assets/155545578/093f857a-2a36-48b1-87e8-262d5b488653)

 - ### Input Feedback.
   - Incorporating a variety of messages that cover every aspect of input data when playing the game ensures no confusion or poor gaming experience.
     - For guesses that are under `0` or guesses exceeding `99` the game suggests coordinates between `0` and `99`.
     - For guesses that are either symbols, letters or words; the game provides a message stating to use coordinates between `0` and `99`
     - For guesses that have already been previously made the game informs the player of their mistakes and asks for another.

![invalid-message](https://github.com/kctffs/battleships/assets/155545578/18928a68-5f0d-405a-90d2-7841be41ac52)
![invalid-message2](https://github.com/kctffs/battleships/assets/155545578/19299412-ce9a-4487-a965-8ea9ac5be156)
![invalid-message3](https://github.com/kctffs/battleships/assets/155545578/fc699f06-dddf-4ccd-bf2a-1c1f5b7469a3)

 - ### Experience.
   - Battleships: Solo offers the player 50 chances to sink all the generated ships on the board.
     - When all ships have been sunk succdssfully within the limit a congratulations message appears.
     - If the player fails to sink all the ships in the given limit, the game resets and waits until it is rerun for another try.

 - ### Future Features.
   - The most obvious future feature would be to include an additional board so the game becomes a PVC (Player vs Computer).
     - This would expand the game and definitely build more gaming relations towards the user as the experience is more competitive.
   - In unique various of the Battleship games, bonus features such as air strikes and UAVs are incorporated that will bring more attention towards the game.
     - This would result in a more interactive experience for the player and would encourage playtime.

## Testing.

 - Putting the code for Battleships: Sollo into the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) threw some initial erros over layout issues.
   - Quick changes to the layout resulted in 100%, passing.
 - Testing the game also through the **Heroku** terminal when deployed.

<img width="1415" alt="PEP8 CI Linter Proof" src="https://github.com/user-attachments/assets/6bcf1a62-4259-40f7-83e9-c535d1b00dc5">

 - ### Deployment.
   - The deployment of Battleships: Solo was through the mock terminal created by Code Institute on Heroku.
     - There are multiple steps for this process and they are as follows:
       - Create a new Heroku app on the **Heroku** site.
       - Set the config var to key - `PORT` and value - `8000`.
       - Set the buildbacks to `Python` and `NodeJS` in that specific order.
       - Link Heroku to the repository. For example, **GitHub**.
       - Deploy.
   - [The link to the deployed version is here.](https://battleships-solo-19b656a2afe3.herokuapp.com/)

 - ### Bugs.
   - Bugs encountered throughout the process where inevitable as this was the first `Python` project however, the main bugs where to do with carless coding.
     - For example, forgetting to return the battleships after altering the lists from the function. This was resolved after disecting the code to find the problem.
     - Another bug arose in the `while` loop where the output wanted was `True` and was recieving `False`. This was resolved after understanding the inital miss input that was erorring the code by reversing the `True` and `False`.

 - ### Unfixed Bugs.
   - When the battleships are randomised and generated onto the board, they sometimes have the possibility of passing from `9` to `0`.
     - This is a bug that has not been resloved as troubleshooting and trying to achieve helo came to no avail.
       - There will of course be a way to fix this and it is to do with the `%` operator however, this was a piece of code that could be better. As a sly solution (which is not the correct solution) the board could be interpreted as a sphere and therefore the placements of the battleships become logical and the bug is no more.

## Credits.

 - ### Content.
   - The idea for creating a unique version of the Battleships game came from the assesment guide.
   - External research and understanding of the game came from the [Wikipedia page](https://en.wikipedia.org/wiki/Battleship_(game)) on the original.
   - For deployment on a mock terminal on **Heroku** created by [Code Institute.](https://codeinstitute.net/)

 - ### Code.
   - Along with the assessment example from **Code Institute**, inpiration for the game and especially defining and the returning empty lists code came from a [YouTube video](https://youtu.be/aMLSS-JVYZk?si=GbFvP93vXYA-87lE&t=1346) at `22:26` by DrCodie.
     - Side note: In the video, they state the code is not theres and is from the internet. As there is no reference, I have credited the video I got the inspiration from instead.
         
