# Battleship Project

### [Here is the live version of the Battleship Game on Heroku](https://p3battleships-bf6b19640af6.herokuapp.com/)

### [Here is the Github Repository](https://github.com/OV00VO/p3battleship)

# Battleships Game

![Responsive](https://github.com/OV00VO/p3battleships/assets/136384344/eaba6842-f08b-4246-8035-41b3ed0de1e1)

### How to play the Battleship Game: 
Battleship is a two-player game in which each player secretly places their ships, selectable from 5 to 10 ships, on a up to 10 by 10 grid and takes turns attacking their opponent's grid. 

Players mark hits with "X" and misses with "O". The first player to sink all of their opponent's ships wins the game. In this version there is Player against the Computer.

For further information about the physical game, rules and other game logic visit: [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

# Features

## Existing Features
The Battleships game features dynamic board initialization, random placement of battleships, turn-based gameplay, player interaction through coordinate input, and detailed game display. It includes status information, error handling, and a clear screen function. 

The game allows customization of board size and ship number, and it concludes with a winner declaration and score display. Overall, it offers an engaging and interactive gaming experience.

![Gameplan 1](https://github.com/OV00VO/p3battleships/assets/136384344/9c490aa2-1809-4d6c-a119-d8b78592a7b2)

## Game Features
* **Board Generation** - Random placement of Battleships for both players.
* **Turn-Based Gameplay** - Alternating moves for players to attack specific coordinates.
* **Dynamic Display** - Real-time display of each player's fleet status.
* **Score Tracking** - Records hits and misses for both player and computer. 
* **Game Conclusion** - Declares a winner and displays the final score.
* **Customizable Parameters** - Adjustable board size and the number of battleships.
* **Error Handling** - Manages invalid user input for a smoother experience.
* **Clear Screen Function** - Enhances display and user experience.
* **User Inputs** - Accepts user inputs for various gameplay actions.
* **Score Maintenance** - Tracks hits, misses, and overall performance.
* **Gameboard Customization** - Allows the adjustment of the gameboard size.
* **Battleship Selection** - Enables the choice of the total number of battleships.
* **Data Model Implementation** - Utilizes a data model Bord class to represent and manage the game state.

![Scoreboard](https://github.com/OV00VO/p3battleships/assets/136384344/b289bf80-2754-40c6-b15e-9404ce71e568)

## Additional Future Features
* **Manual Battleship Placement** - Allows players to manually place Battleships on the gameboard.
* **Game Timer** - Introduces a game timer for time-based gameplay.
* **Screen-Clearing Feature** - Utilizes the os.system import for a screen-clearing function.
* **Multiplayer Mode** - Enables player versus player battles for a multiplayer experience.
* **Enhanced Visuals** - Incorporates improved graphics and visual effects.
* **Audio Integration** - Adds sound effects or background music for an immersive atmosphere.
* **High-Score System** - Implements a high-score system to track and display top performances.
* **In-Game Tutorials** - Provides tutorials or hints to guide new players in understanding rules and strategies.
* **Cross-Platform Expansion** - Expands the game to other platforms, including mobile devices or online gaming platforms.
* **Manual Battleship Placement** - Allows players to manually place Battleships on the gameboard.
  
# Testing

## Bugs

### Solved Bugs
* Resolved line length issues by adjusting lines for improved code readability.
* Conducted code refactoring to enhance organization and readability, particularly addressing sections with excessive length or formatting issues.
* Corrected indentation and formatting in conditional statements, addressing issues such as E128 (continuation line under-indented).
* Modified string concatenation in various sections to conform to specified line length.
* Addressed syntax issues, including fixing missing parentheses, correcting indentation errors, and ensuring proper code structure.
* Verified and corrected variable names for consistency and clarity.
* Ensured correct functioning of game logic, addressing potential issues related to ship placement, attacks, and game outcome determination.

### Remaining Bugs
There are still som UX and UI bugs that could be fixed for a better game experience. Based on presets for the deployment the Code Institute Template for deployment was not adjusted to the gameplan itself. This project was based on not usig other imports that the standard Pythona Random library, no other libraries or similar was used in the project. 

### Validator Testing PEP8
(0) errors were returned from PEP8online.com at final check.

![p3battleship_PEP8](https://github.com/OV00VO/p3battleships/assets/136384344/f79d4e54-c396-4410-be7e-459e5675cb44)

# Deployment
The Battleship project was deployed with Code Institute's mock terminal for Heroku.

# Deployment Steps
### Fork or Clone Repository:
* Fork the repository or clone it to your local machine using the following command:
git clone https://github.com/OV00VO/p3battleships.git

### Create a New Heroku App:
* Log in to your Heroku account.
* Click on the "New" button and select "Create new app."
* Choose a unique app name and set your preferred region.

### Set Buildpacks:
* In the Heroku app dashboard, navigate to the "Settings" tab.
* Scroll down to the "Buildpacks" section.

### Add the following buildpacks in order:
* Python
* NodeJS

### Link Heroku App to Repository:
* In the "Deploy" tab, connect your Heroku app to your GitHub repository.
* Enable automatic deploys if desired.
Deploy:

### Manually deploy your app by clicking the "Deploy Branch" button.
* Alternatively, enable automatic deploys for future updates.

### Open App:
* Once the deployment is successful, click on the "Open App" button to view your live application.

# Credits
Credits are given to the [Code Institute](https://codeinstitute.net/) projects, curriculum and previous projects in Python. 

[GeeksforGeeks - Python Programming Examples](https://www.geeksforgeeks.org/python-programming-examples/)

[Stack Overflow - Clear console in Python](https://stackoverflow.com/questions/273192/how-to-clear-console-in-python)

[PythonDex - Python Battleship Game](https://pythondex.com/python-battleship-game)
