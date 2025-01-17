import simplegui
import random

def draw(canvas): #setting of game
     canvas.draw_circle((545, 65), 50, 5, "goldenrod", "gold")
     canvas.draw_line((1, 500), (600, 500), 50, "forestgreen")
     canvas.draw_line((1,600),(600,600),200, "forestgreen")
#Villagers of game
     canvas.draw_circle([150, 100], 30, 2, 'Black', 'white')
     # Body (line)
     canvas.draw_line([150, 130], [150, 250], 4, 'Black')
     # Arms (lines) 
     canvas.draw_line([150, 150], [100, 200], 4, 'Black') 
     canvas.draw_line([150, 150], [200, 200], 4, 'Black') 
     # Legs (lines) 
     canvas.draw_line([150, 250], [100, 350], 4, 'Black') 
     canvas.draw_line([150, 250], [200, 350], 4, 'Black')


rooms = { #different frames
    "Room 1": {
        "description": "You are in a dark, damp room. There's a door to the north.",
        "exits": ["Go North"],
        "event": "monster",
        "item": "Sword"
    },
    "Room 2": {
        "description": "This room smells of old wood. You see a chest in the corner.",
        "exits": ["Go South", "Go North"],
        "event": "treasure",
        "item": "Potion"
    },
    "Room 3": {
        "description": "You are in a cave with glowing crystals. There's a door to the south.",
        "exits": ["Go South"],
        "event": "none",
        "item": "Torch"
    }
}

inventory = []
health_total = 10
score = 0
current_room = "Room 1"


























frame = simplegui.create_frame("My G4C Game", 600,600)
frame.set_draw_handler(draw)
frame.set_canvas_background("lightskyblue")




frame.start()


