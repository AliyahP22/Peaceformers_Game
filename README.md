# Peaceformers Game

Instructions:
To play this game, the user(which is the pink circle) would use their keyboard to control the player in capturing all of the resources(the cyan circles). The main objective of this game is to gather as much resources as they can to share out to the village and maintain peace. Each time the player collects a resource, they would gain points. If desired, users can press the 'Trigger Random Event' Button that can result in either a reward or a penalty. If the user gets a penalty, they would lose a health, but rewards can boost their score and health. If the user reaches a score of 100 points, they win, but if they lose all their health, they lose the game. Players can expect to see graphics created by the simplegui library along with buttons that can restart the game and trigger a random event.


Game Mechanics:
  Player Movement: Users would be able to use the left, right, up and down arrow keys on their keyboard to control the sprite around the canvas

  Resources (to be collected):
    Using the random.randint function, resources would be placed randomly on the canvas. User would manuever the player to collect the resources. Each time they collect a resource, they would gain a point

Random Events:
Using the random.randint function, users would either get a penalty or a reward. If the user gets event 1, which is a monster, they would lose a health. Potions would gain a health and some resources. Treasure would result in 15 resources. Users may also get an event in which neither a penalty or reward occurs. 

How to win?: Get a score of 100 points
How to lose?: Get a health of 1 or less. If so, press the 'Restart Game' button to try again.

Code Structure:
Uses: Import random and import simplegui. Import simplegui was used to create the graphics of this game. 

Global variables:
health_total: Keeps track of health
Event: list of random events that can occur in game
Rooms: room names in the game
resource_sizes: initial size of each resource
player_position: current and initial position of player
player_size: Initial size of player sprite
score: Keeps track of the current score throughout the game
Health: Health status of plaer

Functions:
random_events(): This function generates a random event based on random.randint and based on the resulting number, would trigger a event that corresponds to health and/or resources

win_or_lose(): Checks for win or loss conditions and updates while the game is running

check_points(): Checks to see if the resources collides with the player sprite and if so, increases score

random_resources(): Generates resources in random positions throughout the canvas

keydown(key): Allows user to control player with their keyboard 

restart_game(): Resets everything to its initial starting values and with the touch of the 'Restart Game' button, users can replay the game


