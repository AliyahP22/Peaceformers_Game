import random
import simplegui

# Global variables
rooms = ["Room 1", "Room 2", "Room 3", "Surprise Room"] #Different rooms, but same background/frame
inventory = [] #initializer list
health_total = {room: 10 for room in rooms}
events = ["monster", "potions", "treasures", "none"]

# Variables used in game
resources_size = 20
player_position = [300, 300]
player_size = 20
score = 0 #intial score
health = 3 #initial total of health
win = False
lose = False
position_resources = [] #initializer list

def random_resources(): #places resources in random places on the frame
    x = random.randint(1, 400)    
    y = random.randint(1, 400)  
    position_resources.append([x, y]) #adds coordinates to the original initializer list

random_resources() #call function

def random_events():
    global health, score
    event = random.randint(1,4)
    if event == 1:
        health -= 1
        return "Oh no a monster stole some resources! Lost a life"
    elif event == 2:
        score += 5
        health +=1
        return "A potion! You gained 5 resources and a life!"
    elif event == 3:
        score +=15
        return "You found the treaure! You gained 15 resources! Be sure to share"
    else:
        return "Sorry, nothing happens"
                

def win_or_lose():
    global win, lose
    if score>=100:
        win = True
        return "Congrats! You helped the village"
       
        
    if health<=1:
        lose = True
        return "Game over"
        

def check_points():
    global score, resources
    for resource in position_resources[:]:
        if (abs(player_position[0] - resource[0]) < (player_size + resources_size) / 2 and abs(player_position[1] )- resource[1]) < (player_size + resources_size) / 2: 
            position_resources.remove(resource) #checks if the resources and player come in contact
            score += 1     
            random_resources() #call function
            break 
            
           
           
def keydown(key): #allows user to control their player icon with their keyboard
    global player_position, lose
    if not lose:
        if key == simplegui.KEY_MAP['left']:
            player_position[0] -= 10 #allows user to move left with left key
        elif key == simplegui.KEY_MAP['right']:
            player_position[0] += 10 #allows user to move right with right key
        elif key == simplegui.KEY_MAP['up']:
            player_position[1] -= 10 #allows user to move up with up arrow
        elif key == simplegui.KEY_MAP['down']:
            player_position[1] += 10 #allows user to move down with down arrow
       
            
            
def draw(canvas): #background graphics 
    global win, lose, health
    canvas.draw_circle((545, 63), 50, 5, "goldenrod", "gold")
    canvas.draw_line((1,500),(600,500), 50, "forestgreen")
    canvas.draw_line((1,600),(600,600), 200, "forestgreen")
    
    for resource in position_resources:
        canvas.draw_circle(resource, resources_size / 2, 2, "black", "cyan") #graphic for resources
        canvas.draw_circle(player_position, player_size / 2, 5, "black", "pink") #graphic for user icon
        
    check_points() #calls function for win or lose
    canvas.draw_text(f"Score: {score}", (10,20), 20, "black")
    canvas.draw_text(f"Health: {health}", (10,40), 20, "black")
    #displays health and score status on the screen as user plays
    
    
    result = win_or_lose()
    if result:
        canvas.draw_text(result,[150,300],30,"Red") #displays messages 
        
        
        

def restart_game(): #allows user to restart if they desire
    global score, health, win, lose, player_position, position, resources
    score = 0
    health = 3
    win = False
    lose = False
    player_position = [300,300]
    position_resources = []
    random_resources()
                
frame = simplegui.create_frame("My Peaceformers Game", 600, 600)
frame. set_draw_handler(draw)
frame. set_canvas_background("lightskyblue")
frame.set_keydown_handler(keydown) #calls function to allow user to use keyboard

#add buttons
frame.add_button("Trigger Random Event", random_events, 150)
#if user presses this, random event would happen based on the random_event function
frame.add_button("Restart Game", restart_game, 150)
frame.start()







