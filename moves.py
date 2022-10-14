# Chiemelie Ezeokeke
# Fall 2020
# Project/Lab 11
# 3rd December 2020

import math #import math
import ChessZelle #import ChessZelle
import graphicsPlus as gr #import graphicsPlus as gr
import time #import time
import random #import random


def move( shapes, dx, dy ):
    # Draw all of the objects in shapes by dx in the x-direction
    # and dy in the y-direction
    # for each item in shapes
        # call the move method on item with dx and dy as arguments
    for sharon in shapes:
        sharon.move(dx, dy)

# What the for loop should be doing is iterating over the list of Graphic Objects

#created a function to to calculate 
def near(p1,p2,radius):
    dx = p1.getX() - p2.getX()
    dy = p1.getY() - p2.getY()
    return dx*dx + dy*dy < radius*radius #return True or False

def inbox(p1,rectangle):
    minX = min(rectangle.getP1().getX(), rectangle.getP2().getX())
    minY = min(rectangle.getP1().getY(), rectangle.getP2().getY())
    maxX = max(rectangle.getP1().getX(), rectangle.getP2().getX())
    maxY = max(rectangle.getP1().getY(), rectangle.getP2().getY())

    return minX <= p1.getX() <= maxX and minY <= p1.getY() <= maxY #Comparison of the center point of the click on the boxes. created aminimun and Maximun value.

#defined a function to draw the shapes
def draw(shape,win):
    for item in shape:
        item.draw(win)

#define the move function to test the moves.
def moves():
    win = gr.GraphWin("checkers", 1550, 1300)  #window drawn name of the window and the size of the window

    block = ChessZelle.init_checkerboard(300,100,1)  #checkerboard is drawn
    draw(block,win)
    block2 = ChessZelle.init_checkerboxes(350,100,1) #checkerboard is drawn
    draw(block2,win)

    white = ChessZelle.init_whitecheckers() # white checker is drawn
    draw(white,win)

    blackp = ChessZelle.init_blackcheckers()  # black checker is drawn
    draw(blackp,win)



  

    #variable active piece and original colour 
    active_piece = None

    original_color = "lemonchiffon"

    #Whose turn

    turn = 'white'  #whose turn is created 

    txt =  gr.Text(gr.Point(150,50), "white Turn") #text to show whose turn it is 
    txt.setSize(30)
    txt.setStyle("bold")
    txt.draw(win) #text to be drawn

    done = False #if the event isn't done

    while not done:    #while the event is not done 

        # check for a key press
        key = win.checkKey()    #when q is pressed close the window
        if key == 'q':
            done = True

           # check for a mouse click
        pt = win.checkMouse()

        if pt != None:
            if active_piece == None:
                #if there is no active checker piece
                if turn == 'white':
                #if white turn variable
                    current_player = white 
                else:
                    current_player = blackp

                for checks in current_player:
                    #find out if the user clicked on a checker pieces
                    if near(pt,checks.getCenter(),checks.getRadius()):
                        #if the user clicked on a checker piece 
                        original_color = checks.getFill()
                        checks.setFill("green")
                        #make the circle green (active checker piece)
                        #save checker piece currently active
                        active_piece = checks
                        break
            #else:
            else:
                for boxes in block2:
                    if inbox(pt,boxes):
                        #if the user clicked on a square.
                        cx = (boxes.getP1().getX() + boxes.getP2().getX())//2
                        cy = (boxes.getP1().getY() + boxes.getP2().getY())//2
                        ax = active_piece.getCenter().getX()
                        ay = active_piece.getCenter().getY()
                        active_piece.move(cx-ax,cy-ay)
                        #if clicked on square. Move active checker piece to that square.
                        active_piece.setFill(original_color)
                        #variable active piece and original colour 
                        #then deactivate the checker piece. (change color back to original)
                        active_piece = None
                        if turn == 'white':        
                            txt.setText("Black Turn")
                            txt.setSize(30)
                            txt.setStyle('bold')
                            turn = 'black'
                        else:
                            turn = 'white'
                            txt.setText("White Turn") #set text to white when white turn and black to black turn
                        break

            
        win.update()
        time.sleep(0.02)

#code is executed here
if __name__ == "__main__":
    moves()


        

