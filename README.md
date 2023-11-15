# Battleship Game Coding Project

### [Here is the live version of the Battleship Game on Heroku](https://p3battleships-bf6b19640af6.herokuapp.com/)

### [Here is a link to the Battleship Game - Github Repository](https://github.com/OV00VO/p3battleship)

# Battleship Game

![Responsive](https://github.com/OV00VO/p3battleships/assets/136384344/eaba6842-f08b-4246-8035-41b3ed0de1e1)

### How to play the Battleship Game: 
Battleship is a Player versus Computer game in which each player secretly places their ships, selectable from 5 to 10 ships, they all vary in size. The battleships are placed randomly on a game board that is up to 10 by 10 grid. The player and the computer then takes turns attacking their opponent's grid, by using coordinates based a scope.

### Input of Playername, Username, Alias or Avatar name

When launching the game by clicking the Run Program button, the user can type their name or use an alias, in this case an alias of Avatar.
  
![Startscreen](https://github.com/OV00VO/p3battleships/assets/136384344/9648e43e-3e3d-48e0-aace-21a207377d48)

### How the player communicate with the game

To get a clear view on how to use coordinates in the game, the upper left corner of the game bord has the coordinates of (1, 1). On the largest game board the diagonal last coordinate is (10, 10). The user only types in the move, in the future named an Attack, this by only using numbers within the right scope, not by using the coordination system such as (1, 1), the player first selects a horizontal row X from (X, y), and then selects a column on Y (x, Y).

![Game](https://github.com/OV00VO/p3battleships/assets/136384344/c28fe04e-d5cd-4433-b001-d6d576a2ebf5)

### How the computer output communicates with the player

The computer mark the attacks of hits with "X" and misses with "O" the Players Battleships is marked with "#". The first player to sink all of their opponent's ships, wins the game.

![Gameboard1](https://github.com/OV00VO/p3battleships/assets/136384344/9430a731-1e51-4f50-8104-43c216fa658e)

In this version there is a Player against Computer function and it uses a randomized placements of battleships on the game boards. The player can see the placements of starts with the first move but not the computer battleship placements. The game works in the same way as the traditional Battleship game, that player that first sinks all of the opponents battleships win the game.

For further information about the physical game, rules and other game logic visit: [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

## User Stories

### User Story 1: Player Interaction
As a player, I want to easily understand the game's feedback on my moves.

#### Acceptance Criteria:

1. **Scenario:** Making a Successful Attack
   - **Given:** I am in the middle of a game.
   - **When:** I make a successful attack on an opponent's ship.
   - **Then:** The game should clearly indicate that it was a "Hit!" and update the display to reflect the hit on the opponent's board.

2. **Scenario:** Making an Unsuccessful Attack
   - **Given:** I am in the middle of a game.
   - **When:** I make an unsuccessful attack, missing the opponent's ship.
   - **Then:** The game should clearly indicate that it was a "Miss!" and update the display to reflect the miss on the opponent's board.

3. **Scenario:** Viewing Opponent's Moves
   - **Given:** I am in the middle of a game.
   - **When:** The opponent makes a move.
   - **Then:** The game should clearly display the opponent's move, indicating whether it was a hit or miss.

4. **Scenario:** End of Game
   - **Given:** The game is concluding.
   - **When:** The game ends.
   - **Then:** The final result, including the winner and score, should be clearly communicated to me.

#### Additional Considerations:

- The feedback messages should use clear and concise language, avoiding ambiguity.
- The visual representation of the game board should provide a quick overview of the current state, highlighting Hit and Miss locations effectively.
- The end-game screen should provide a summary of the game, making it easy to understand the outcome and final scores.
- Any prompts or messages presented to the player should be user-friendly and avoid technical jargon that might confuse casual players.

### User Story 2: Code Readability and Maintainability from the Developers Perspective
As a developer, I want the code to follow best practices for readability and maintainability.

#### Acceptance Criteria:

1. **Code Structure:**
   - **Given:** I am reviewing the codebase.
   - **When:** I explore the project directories and files.
   - **Then:** The code should be organized logically, with clear separation of concerns and a consistent folder structure.

2. **Comments and Documentation:**
   - **Given:** I am reading through the code.
   - **When:** I encounter complex or non-trivial sections.
   - **Then:** The code should include helpful comments and documentation explaining the purpose and functionality of the complex sections.

3. **Variable and Function Naming:**
   - **Given:** I am reviewing variable and function names.
   - **When:** I come across a variable or function.
   - **Then:** The names should be descriptive, following a consistent naming convention, and providing a clear understanding of their purpose.

4. **Code Formatting:**
   - **Given:** I am examining the code.
   - **When:** I review the formatting.
   - **Then:** The code should follow a consistent style guide, with proper indentation, spacing, and alignment for improved readability.

5. **Avoidance of Magic Numbers:**
   - **Given:** I am analyzing numerical values in the code.
   - **When:** I encounter numeric constants without clear context.
   - **Then:** The code should avoid the use of magic numbers and instead use named constants or variables to enhance code readability.

6. **Error Handling:**
   - **Given:** I am inspecting error-handling mechanisms.
   - **When:** I come across sections dealing with potential errors.
   - **Then:** The code should include appropriate error handling with descriptive messages, making it easier to diagnose issues during development and maintenance.

7. **Testing:**
   - **Given:** I am assessing the test suite.
   - **When:** I review the tests.
   - **Then:** The tests should cover critical functionalities, providing adequate code coverage, and be organized in a way that aligns with the project structure.

#### Additional Considerations:

- Refactoring should be performed when necessary to improve code quality.
- The use of design patterns and best practices should be considered where applicable.
- Code should be written with future maintainers in mind, anticipating potential changes and updates to the project.
- Continuous integration and automated code analysis tools should be utilized to catch potential issues early in the development process.

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

# Data Model - Board Class

When creating a game such as this Battleship game, the Board class serves as the cornerstone, shaping the game's structure and data flow. This class, instantiated for both players and the computer, orchestrates crucial aspects of gameplay. The Board class provides a robust, organized, and scalable framework for managing player actions, ship positions, and game progression.

## Core Features
* Board Size and Configuration - Manages grid size and ship placement for a customizable gaming experience.
* Guess Tracking - Records player guesses, crucial for hit and miss determination.
* Player and Board Identification - Identifies player and computer boards, ensuring a personalized gaming environment.
* Gameplay Facilitation Methods - Includes `print_board` for visual representation and `add_ships` for strategic ship placement.

## Advantages of the Board Class
* Modularity and Extensibility - Facilitates easy feature additions without disrupting core logic.
* Readability and Organization - Enhances code readability and organization by centralizing board-related operations.
* Scalability and Customization - Adaptable to varied game complexities and user preferences.
* Encapsulation of Game State - Maintains clean data management, minimizing conflicts and ensuring game integrity.

# Testing

## Manual Testing Steps
  
1. **Game Initialization:**
   - **Action:** Launch the game.
   - **Expected Result:** The welcome screen is displayed with instructions and prompts.
   - **Observed Result:** Verify that the welcome screen appears as expected.

2. **Board Customization:**
   - **Action:** Choose a board size and number of battleships.
   - **Expected Result:** The game board is initialized with the selected parameters.
   - **Observed Result:** Confirm that the board size and number of battleships match the chosen values.

3. **Ship Placement:**
   - **Action:** Start a new game and observe ship placement.
   - **Expected Result:** Battleships are randomly placed on both player and computer game boards.
   - **Observed Result:** Verify that ships are distributed randomly with correct orientations.

4. **Player Attack:**
   - **Action:** Enter valid coordinates to attack a position on the computer's board.
   - **Expected Result:** The result of the attack (hit or miss) is displayed.
   - **Observed Result:** Confirm that the attack result is correctly shown, and the game board is updated.

5. **Computer Attack:**
   - **Action:** Observe the computer's turn.
   - **Expected Result:** The computer makes a valid attack on the player's board.
   - **Observed Result:** Verify that the computer's attack is valid, and the player's board is updated accordingly.

6. **Game Conclusion:**
   - **Action:** Play until the game concludes.
   - **Expected Result:** The game declares a winner, and the final score is displayed.
   - **Observed Result:** Confirm that the game concludes correctly with the expected winner and score.

7. **Error Handling:**
   - **Action:** Intentionally provide invalid input during gameplay.
   - **Expected Result:** The game handles errors gracefully with informative messages.
   - **Observed Result:** Verify that the game displays appropriate error messages and continues without crashing.

8. **User Interface:**
   - **Action:** Interact with different elements on the user interface.
   - **Expected Result:** Buttons, prompts, and displays respond appropriately.
   - **Observed Result:** Confirm that the user interface elements function as expected.

9. **Scalability:**
   - **Action:** Test the game with different board sizes and battleship numbers.
   - **Expected Result:** The game adjusts to different configurations without issues.
   - **Observed Result:** Confirm that the game is scalable and maintains functionality with varied parameters.

## Bugs

### Resolved Bugs

* Resolved line length issues by adjusting lines for improved code readability.
* Conducted code refactoring to enhance organization and readability, particularly addressing sections with excessive length or formatting issues.
* Corrected indentation and formatting in conditional statements, addressing issues such as E128 (continuation line under-indented).
* Modified string concatenation in various sections to conform to specified line length.
* Addressed syntax issues, including fixing missing parentheses, correcting indentation errors, and ensuring proper code structure.
* Verified and corrected variable names for consistency and clarity.
* Ensured correct functioning of game logic, addressing potential issues related to ship placement, attacks, and game outcome determination.

* ### Bug 1: Player's Guess Text Display Issue

- **Error Message:** `Line 185: E501 line too long (97 > 79 characters)`
- **Line Numbers:** 185
- **Solution:** Adjusted string concatenation to resolve line length issue.

### Bug 2: Computer's Turn Display Issue

- **Error Message:** `Line 196: E501 line too long (102 > 79 characters)`
- **Line Numbers:** 196
- **Solution:** Split the computer's turn display into multiple lines for better readability.

### Bug 3: Display Board Functionality

- **Error Message:** `Line 205: E501 line too long (119 > 79 characters)`
- **Line Numbers:** 205
- **Solution:** Refactored display_board function to improve formatting and avoid line length issues.

### Bug 4: Computer's Guess String Concatenation

- **Error Message:** `Line 217: E501 line too long (118 > 79 characters)`
- **Line Numbers:** 217
- **Solution:** Split string concatenation for computer's guess to meet line length guidelines.

### Remaining Bugs
There are still som UX and UI bugs that could be fixed for a better game experience. Based on presets for the deployment the Code Institute Template for deployment was not adjusted to the gameplan itself. This project was based on not using other import of libraries that the standard Python Random library, no other libraries or similar was used in the project. By using different libraries for instance the Graphic library the game could be improved further.

### Validator Testing PEP8
(0) errors were returned from [PEP8 Validator fron Code Institute](https://pep8ci.herokuapp.com/) at final check.

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
