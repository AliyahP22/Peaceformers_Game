import simplegui
import random

#global variables that would be used 
rooms = ["Room 1", "Room 2", "Room 3" "Surprise Room"]

#variables 
inventory = []
health_total = {room:10 for room in rooms} #sets 10 health for each room
decisions_log = []
events = ["monster", "potions", "treasures", "none"]

#variables used in game
resources_sizes = 20
positions_resources = []
resources = 15
position_resources = []
player_position = [300,300]
player_size = 20
score = 0 #initial score

win = False
lose = False 
def random_resources():
    x = random.randint(1,500)
    y = random.randint(1,500)
    position_resources.append([x,y])
    position_resources.append([x,y])
    position_resources.append([x,y])
    position_resources.append([x,y])
    
def random_events():
    events = random.randint(1,4)
    if events == 1:
        return "OH NO! A monster stole some of your resources! Lost a life!"
        health_total -=1
    elif events == 2:
        return "Wow a potion! You gained 5 resources and 1 live!"
        health_total += 1 
    elif events == 3:
        return "CONGRATS! You found hidden treasure! 50 resources! Go share it with the village"
    else:
        return "Sorry, nothing happens"

def win_or_lose():
    if score >=100:
        return "CONGRATS! YOU HELPED THE VILLAGE! Play again?"
        win = True 
        lose = False 
    else:
        win = False 
        lose = True 
        random_events()
                          

def check_points():
    for resource in positions_resources[:]:
        if (abs(player_position[0] - resource[0]) < (player_size + resources_sizes) / 2 and abs(player_position[1] - resource[1]) < (player_size + resources_sizes) / 2):
            position_resources.remove(resource) #Checks to see if player comes in contact with the resources
            score +=2
            log_event("Congrats you found resources! Be sure to share with the village")
            random_resources()
            
            
def keydown(key):
    #Handles player movement
    if not lose:
        if key == simplegui.KEY_MAP['left']:
            player_position[0] -= 10
        elif key == simplegui.KEY_MAP['right']:
            player_position[0] += 10
        elif key == simplegui.KEY_MAP['up']:
            player_position[1] -= 10
        elif key == simplegui.KEY_MAP['down']:#allows user to use keyboard to control
            player_position[1] += 10

            
            
            
win_or_lose()
random_resources()
 
def draw(canvas):
    canvas.draw_circle((545, 65), 50, 5, "goldenrod", "gold")
    canvas.draw_line((1, 500), (600, 500), 50, "forestgreen")
    canvas.draw_line((1,600),(600,600),200, "forestgreen")
    
    #drawing resources
    for resource in position_resources:
        canvas.draw_circle(resource, resources_sizes / 2, 2, "black", "cyan")
    #drawing player
        canvas.draw_circle(player_position, player_size/2, 5, "black", "pink")
    
    

frame = simplegui.create_frame("My Peaceformers Game", 600,600)
frame.set_draw_handler(draw)
frame.set_canvas_background("lightskyblue")




frame.start()








