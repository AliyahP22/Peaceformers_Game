import simplegui

def draw(canvas):
     canvas.draw_circle((545, 65), 50, 5, "goldenrod", "gold")
     canvas.draw_line((1, 500), (600, 500), 50, "forestgreen")
     canvas.draw_line((1,600),(600,600),200, "forestgreen")




































frame = simplegui.create_frame("My G4C Game", 600,600)
frame.set_draw_handler(draw)
frame.set_canvas_background("lightskyblue")




frame.start()
