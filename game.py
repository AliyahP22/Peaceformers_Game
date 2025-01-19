import random
import simplegui
# Global variables
rooms = ["Room 1", "Room 2", "Room 3", "Surprise Room"]
inventory = []
health_total = {room: 10 for room in rooms}
decisions_log = []
events = ["monster", "potions", "treasures", "none"]

# Variables used in game
resources_size = 20
position_resources = []  # Initialize as empty list
random_resources()  # Generate the first resource position
resources = 15
player_position = [300, 300]
player_size = 20
score = 0  # Initial score
health = 10  # Starting health
win = False
lose = False

def random_resources():        
    # Generate random resource positions       
    x = random.randint(1, 500)        
    y = random.randint(1, 600)        
    position_resources.append([x, y])  
    # Append [x, y] pair to position_resources   
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
        win = True                
        return "CONGRATS! YOU HELPED THE VILLAGE! Play again?"        
    elif health <= 0:                
        lose = True                
        return "GAME OVER! You ran out of health! Play again?"        
    return None
def check_points():        
    global score, resources       
    for resource in position_resources[:]:  # Iterate over a copy of position_resources                
        if (abs(player_position[0] - resource[0]) < (player_size + resources_size) / 2 and 
            abs(player_position[1] - resource[1]) < (player_size + resources_size) / 2):                        
            position_resources.remove(resource)  # Remove the resource from the list
            score += 2  # Increase score                        log_event("Congrats you found resources! Be sure to share with the village")                        random_resources()  # Generate new resources            break  # Stop checking once you’ve collected one resource
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
    global win, lose, health    
    # Draw the game elements        
    canvas.draw_circle((545, 65), 50, 5, "goldenrod", "gold")  # Draw a circle (decorative)       
    canvas.draw_line((1, 500), (600, 500), 50, "forestgreen")  # Draw first line (decorative)       
    canvas.draw_line((1, 600), (600, 600), 200, "forestgreen")  # Draw second line (decorative)       
    # Draw resources and player        
    for resource in position_resources:                
        canvas.draw_circle(resource, resources_size / 2, 2, "black", "cyan")            
        canvas.draw_circle(player_position, player_size / 2, 5, "black", "pink")        
        # Check for points        
check_points()       
# Display score and health        
    canvas.draw_text(f"Score: {score}", [10, 20], 20, "White")       
    canvas.draw_text(f"Health: {health}", [10, 40], 20, "White")                
    # Check for win/lose condition        
    result = win_or_lose()        
    if result:                
        canvas.draw_text(result, [150, 300], 30, "Red")        
        # Simulate random event (every frame)        
        event_message = random_events()        
        log_event(event_message)        # Apply random event effects        
        if "monster" in event_message:                
            health -= 1       
        elif "potion" in event_message:               
            resources += 5                
            health += 1       
        elif "treasure" in event_message:                
            resources += 50
# Start the frame
frame = simplegui.create_frame("My Peaceformers Game", 600, 600)
frame.set_draw_handler(draw)
frame.set_canvas_background("lightskyblue")
frame.set_keydown_handler(keydown)
frame.start()








