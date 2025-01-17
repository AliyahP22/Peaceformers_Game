import simplegui
import random

# Global variables
rooms = ["Room 1", "Room 2", "Room 3", "Surprise Room"]  # Added missing comma
inventory = []
health_total = {room: 10 for room in rooms}  # Sets 10 health for each room
decisions_log = []
events = ["monster", "potions", "treasures", "none"]

# Variables used in game
resources_size = 20
position_resources = []  # Changed variable to a consistent name
resources = 15
player_position = [300, 300]
player_size = 20
score = 0  # Initial score
win = False
lose = False

def random_resources():
    # Generate random resource positions
    x = random.randint(1, 500)
    y = random.randint(1, 500)
    position_resources.append([x, y])


def random_events():
    event = random.randint(1, 4)
    if event == 1:
        return "OH NO! A monster stole some of your resources! Lost a life!"
    elif event == 2:
        return "Wow a potion! You gained 5 resources and 1 life!"
    elif event == 3:
        return "CONGRATS! You found hidden treasure! 50 resources!"
    else:
        return "Sorry, nothing happens"

def win_or_lose():
    global win, lose
    if score >= 100:
        return "CONGRATS! YOU HELPED THE VILLAGE! Play again?"
    else:
        random_events()


def check_points():
    global score, resources
    for resource in position_resources[:]:  # Iterate over a copy of position_resources
        if (abs(player_position[0] - resource[0]) < (player_size + resources_size) / 2 and
                abs(player_position[1] - resource[1]) < (player_size + resources_size) / 2):
            position_resources.remove(resource)  # Remove the resource from the list
            score += 2  # Increase score
            log_event("Congrats you found resources! Be sure to share with the village")
            random_resources()  # Generate new resources

def log_event(message):
    decisions_log.append(message)
    print(message)


def keydown(key):
    global player_position, lose
    if not lose:
        if key == simplegui.KEY_MAP['left']:
            player_position[0] -= 10
        elif key == simplegui.KEY_MAP['right']:
            player_position[0] += 10
        elif key == simplegui.KEY_MAP['up']:
            player_position[1] -= 10
        elif key == simplegui.KEY_MAP['down']:
            player_position[1] += 10

            
            
                       
def draw(canvas):
    # Draw the game elements
    canvas.draw_circle((545, 65), 50, 5, "goldenrod", "gold")  # Draw a circle
    canvas.draw_line((1, 500), (600, 500), 50, "forestgreen")  # Draw first line
    canvas.draw_line((1, 600), (600, 600), 200, "forestgreen")  # Draw second line
    for resource in position_resources:
        canvas.draw_circle(resource, resources_size / 2, 2, "black", "cyan")
    canvas.draw_circle(player_position, player_size / 2, 5, "black", "pink")

check_points()
win_or_lose()
random_resources() 


frame = simplegui.create_frame("My Peaceformers Game", 600, 600)
frame.set_draw_handler(draw)
frame.set_canvas_background("lightskyblue")
frame.set_keydown_handler(keydown)
frame.start()






