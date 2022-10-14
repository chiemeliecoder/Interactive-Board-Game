# Chiemelie Ezeokeke
# Fall 2020
# Project/Lab 11
# 3rd December 2020

import graphicsPlus as gr #import graphicsPlus
import time  #import time
import math as m #import math

#Created the function to make the checkerboard and put it in a list.
def init_checkerboard(x,y,scale):
    board = []
    Box = gr.Rectangle(gr.Point(x-scale*5, 710), gr.Point(x+scale*970, y-scale*80))
    Box.setFill("tan")

    board.append(Box)

    return board #List is returned

#function to create checker boxes on the board this is done instead of making 64 boxes a board behind and a boxes on top and 
# they are created in a list using x,y and scale parameters used to position the boxes
def init_checkerboxes(x,y,scale):
    
    Boxes =[]
    Box2 = gr.Rectangle(gr.Point(x+scale*65, y), gr.Point(x+scale*180, 20))
    Box2.setFill("sienna")
    
    Boxes.append(Box2)

    Box3 = gr.Rectangle(gr.Point(x+scale*420, y), gr.Point(x+scale*300, 20))
    Box3.setFill("sienna")
    
    Boxes.append(Box3)

    Box4 = gr.Rectangle(gr.Point(x+scale*670, y), gr.Point(x+scale*550, 20))
    Box4.setFill("sienna")
    
    Boxes.append(Box4)

    Box5 = gr.Rectangle(gr.Point(x+scale*920, y), gr.Point(x+scale*800, 20))
    Box5.setFill("sienna")
    
    Boxes.append(Box5)

    Box6 = gr.Rectangle(gr.Point(296+scale*0, 190), gr.Point(x+scale*65, 100))
    Box6.setFill("sienna")
    
    Boxes.append(Box6)

    Box7 = gr.Rectangle(gr.Point(530+scale*0, 190), gr.Point(x+scale*300, 100))
    Box7.setFill("sienna")
    
    Boxes.append(Box7)

    Box8 = gr.Rectangle(gr.Point(900+scale*0, 190), gr.Point(x+scale*420, 100))
    Box8.setFill("sienna")
    
    Boxes.append(Box8)

    Box9 = gr.Rectangle(gr.Point(1020+scale*0, 190), gr.Point(x+scale*800, 100))
    Box9.setFill("sienna")
    
    Boxes.append(Box9)

    Box10 = gr.Rectangle(gr.Point(415+scale*0, 280), gr.Point(x+scale*180, 190))
    Box10.setFill("sienna")
    
    Boxes.append(Box10)

    Box11 = gr.Rectangle(gr.Point(650+scale*0, 280), gr.Point(x+scale*420, 190))
    Box11.setFill("sienna")
    
    Boxes.append(Box11)

    Box12 = gr.Rectangle(gr.Point(900+scale*0, 280), gr.Point(x+scale*670, 190))
    Box12.setFill("sienna")
    
    Boxes.append(Box12)

    Box13 = gr.Rectangle(gr.Point(1150+scale*0, 280), gr.Point(x+scale*920, 190))
    Box13.setFill("sienna")
    
    Boxes.append(Box13)

    Box14 = gr.Rectangle(gr.Point(295+scale*0, 370), gr.Point(x+scale*65, 280))
    Box14.setFill("sienna")
    
    Boxes.append(Box14)

    Box15 = gr.Rectangle(gr.Point(530+scale*0, 370), gr.Point(x+scale*300, 280))
    Box15.setFill("sienna")
    
    Boxes.append(Box15)

    Box16 = gr.Rectangle(gr.Point(770+scale*0, 370), gr.Point(x+scale*550, 280))
    Box16.setFill("sienna")
    
    Boxes.append(Box16)

    Box17 = gr.Rectangle(gr.Point(1020+scale*0, 370), gr.Point(x+scale*800, 280))
    Box17.setFill("sienna")
    
    Boxes.append(Box17)

    Box18 = gr.Rectangle(gr.Point(414+scale*0, 450), gr.Point(x+scale*180, 370))
    Box18.setFill("sienna")
    
    Boxes.append(Box18)

    Box19 = gr.Rectangle(gr.Point(769+scale*0, 450), gr.Point(x+scale*300, 370))
    Box19.setFill("sienna")
    
    Boxes.append(Box19)

    Box20 = gr.Rectangle(gr.Point(1020+scale*0, 450), gr.Point(x+scale*550, 370))
    Box20.setFill("sienna")
    
    Boxes.append(Box20)

    Box21 = gr.Rectangle(gr.Point(1270+scale*0, 450), gr.Point(x+scale*800, 370))
    Box21.setFill("sienna")
    
    Boxes.append(Box21)

    Box22 = gr.Rectangle(gr.Point(294+scale*0, 540), gr.Point(x+scale*65, 450))
    Box22.setFill("sienna")
    
    Boxes.append(Box22)

    Box23 = gr.Rectangle(gr.Point(530+scale*0, 540), gr.Point(x+scale*300, 450))
    Box23.setFill("sienna")
    
    Boxes.append(Box23)

    Box24 = gr.Rectangle(gr.Point(900+scale*0, 540), gr.Point(x+scale*420, 450))
    Box24.setFill("sienna")
    
    Boxes.append(Box24)

    Box25 = gr.Rectangle(gr.Point(1020+scale*0, 540), gr.Point(x+scale*800, 450))
    Box25.setFill("sienna")
    
    Boxes.append(Box25)

    Box26 = gr.Rectangle(gr.Point(413+scale*0, 620), gr.Point(x+scale*180, 540))
    Box26.setFill("sienna")
    
    Boxes.append(Box26)

    Box27 = gr.Rectangle(gr.Point(650+scale*0, 620), gr.Point(x+scale*420, 540))
    Box27.setFill("sienna")
    
    Boxes.append(Box27)

    Box28 = gr.Rectangle(gr.Point(900+scale*0, 620), gr.Point(x+scale*670, 540))
    Box28.setFill("sienna")
    
    Boxes.append(Box28)

    Box29 = gr.Rectangle(gr.Point(1150+scale*0, 620), gr.Point(x+scale*920, 540))
    Box29.setFill("sienna")
    
    Boxes.append(Box29)

    Box30 = gr.Rectangle(gr.Point(293+scale*0, 710), gr.Point(x+scale*65, 620))
    Box30.setFill("sienna")
    
    Boxes.append(Box30)

    Box31 = gr.Rectangle(gr.Point(530+scale*0, 710), gr.Point(x+scale*300, 620))
    Box31.setFill("sienna")
    
    Boxes.append(Box31)

    Box32 = gr.Rectangle(gr.Point(770+scale*0, 710), gr.Point(x+scale*550, 620))
    Box32.setFill("sienna")
    
    Boxes.append(Box32)

    Box33 = gr.Rectangle(gr.Point(1020+scale*0, 710), gr.Point(x+scale*800, 620))
    Box33.setFill("sienna")
    
    Boxes.append(Box33)

    Boxout = gr.Rectangle(gr.Point(20+scale*0, 500), gr.Point(250, 700))
    Boxout.setFill("black")
    Boxes.append(Boxout)

    Boxout2 = gr.Rectangle(gr.Point(1300+scale*9, 15), gr.Point(1530, 200))
    Boxout2.setFill("lemonchiffon")
    Boxout2.setOutline("lemonchiffon")
    Boxes.append(Boxout2)
    
    return Boxes #list is returned


#created a function to draw the white checker pieces which are circles using gr.circle
def init_whitecheckers():
    wcheckers = []
    
    #example of function on a board
    anchor1 = recCenter(415,100,530,20)
    wpiece1 = gr.Circle(anchor1,40)
    wpiece1.setFill("lemonchiffon")
    wpiece1.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece1)

    
    anchor2= recCenter(650,100,770,20)
    wpiece2 =  gr.Circle(anchor2, 40)
    wpiece2.setFill("lemonchiffon")
    wpiece2.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece2)

    anchor3 = recCenter(900,100,1020,20)
    wpiece3 = gr.Circle(anchor3, 40)
    wpiece3.setFill("lemonchiffon")
    wpiece3.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece3)

    anchor4 = recCenter(1150,100,1270,20)
    wpiece4 = gr.Circle(anchor4, 40)
    wpiece4.setFill("lemonchiffon")
    wpiece4.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece4)

    anchor5 = recCenter(296,190,415,100)
    wpiece5 =  gr.Circle(anchor5, 40)
    wpiece5.setFill("lemonchiffon")
    wpiece5.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece5)

    anchor6 = recCenter(1650,190,530,100)
    wpiece6 = gr.Circle(anchor6, 40)
    wpiece6.setFill("lemonchiffon")
    wpiece6.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece6)

    anchor7 = recCenter(770,190,900,100)
    wpiece7 = gr.Circle(anchor7, 40)
    wpiece7.setFill("lemonchiffon")
    wpiece7.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece7)

    anchor8 = recCenter(1020,190,1150,100)
    wpiece8 =  gr.Circle(anchor8, 40)
    wpiece8.setFill("lemonchiffon")
    wpiece8.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece8)

    anchor9= recCenter(415,280,530,190)
    wpiece9 = gr.Circle(anchor9, 40)
    wpiece9.setFill("lemonchiffon")
    wpiece9.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece9)

    anchor10= recCenter(650,280,770,190)
    wpiece10 = gr.Circle( anchor10, 40)
    wpiece10.setFill("lemonchiffon")
    wpiece10.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece10)

    anchor11 = recCenter(900,280,1020,190)
    wpiece11 =  gr.Circle (anchor11, 40)
    wpiece11.setFill("lemonchiffon")
    wpiece11.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece11)

    anchor12= recCenter(1150,280,1270,190)
    wpiece12 = gr.Circle(anchor12, 40)
    wpiece12.setFill("lemonchiffon")
    wpiece12.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece12)

    anchor13= recCenter(530,190,650,100)
    wpiece13 = gr.Circle(anchor13, 40)
    wpiece13.setFill("lemonchiffon")
    wpiece13.setOutline("lemonchiffon")
    
    wcheckers.append(wpiece13)

    # could do "wcheckers = [wpiece1, wpiece2 ... wpiece12 ] instead of appending each time


    return wcheckers

#created a function to draw the black checker pieces which are circles using gr.circle
def init_blackcheckers():
    bcheckers = []
    banchor1 = recCenter(294,540,415,450)
    bpiece1 = gr.Circle(banchor1, 40)
    bpiece1.setFill("black")
    bpiece1.setOutline("black")
    
    bcheckers.append(bpiece1)

    banchor2 = recCenter(530,540,650,450)
    bpiece2 =  gr.Circle(banchor2, 40)
    bpiece2.setFill("black")
    bpiece2.setOutline("black")
    
    bcheckers.append(bpiece2)

    banchor3 = recCenter(770,540,900,450)
    bpiece3 = gr.Circle(banchor3, 40)
    bpiece3.setFill("black")
    bpiece3.setOutline("black")
    
    bcheckers.append(bpiece3)

    banchor4 = recCenter(1020,540,1150,450)
    bpiece4 = gr.Circle(banchor4, 40)
    bpiece4.setFill("black")
    bpiece4.setOutline("black")
    
    bcheckers.append(bpiece4)

    banchor5 = recCenter(413,620,530,540)
    bpiece5 =  gr.Circle(banchor5, 40)
    bpiece5.setFill("black")
    bpiece5.setOutline("black")
    
    bcheckers.append(bpiece5)

    banchor6 = recCenter(650,620,770,540)
    bpiece6 = gr.Circle(banchor6, 40)
    bpiece6.setFill("black")
    bpiece6.setOutline("black")
    
    bcheckers.append(bpiece6)

    banchor7 = recCenter(900,620,1020,540)
    bpiece7 = gr.Circle(banchor7, 40)
    bpiece7.setFill("black")
    bpiece7.setOutline("black")
    
    bcheckers.append(bpiece7)
    
    banchor8 = recCenter(1150,620,1270,540)
    bpiece8 =  gr.Circle(banchor8, 40)
    bpiece8.setFill("black")
    bpiece8.setOutline("black")
    
    bcheckers.append(bpiece8)

    banchor9 = recCenter(293,710,415,620)
    bpiece9 = gr.Circle(banchor9, 40)
    bpiece9.setFill("black")
    bpiece9.setOutline("black")
    
    bcheckers.append(bpiece9)

    banchor10 = recCenter(530,710,650,620)
    bpiece10 = gr.Circle(banchor10, 40)
    bpiece10.setFill("black")
    bpiece10.setOutline("black")
    
    bcheckers.append(bpiece10)

    banchor11 = recCenter(770,710,900,620)
    bpiece11 =  gr.Circle(banchor11, 40)
    bpiece11.setFill("black")
    bpiece11.setOutline("black")
    
    bcheckers.append(bpiece11)

    banchor12 = recCenter(1020,710,1150,620)
    bpiece12 = gr.Circle(banchor12, 40)
    bpiece12.setFill("black")
    bpiece12.setOutline("black")
    
    bcheckers.append(bpiece12)

    

    return bcheckers








#created function to calculate center point of a rectangle
def recCenter(x1, y1, x2, y2):
    #get middle distance 
    distanceX = abs(x2 - x1) // 2
    print(distanceX)
    distanceY = abs(y2 - y1) // 2 #absolute value to account for Zelle graphics
    print(distanceY)
    #now add the distance to middle to get new center point for circle
    middleX = x1 + distanceX
    middleY = y2 + distanceY #(second point of rect is upper right)
    
    #returns a graphics Point object, this will be first arg of Circle (its anchor point)
    calCenter = gr.Point(middleX, middleY) 

    return calCenter

#iterate through list of shapes and draw them on window (checkers board)
#draw(checkersArray, win)
#the graphics Objects have its own draw method, called like: circle1.draw(win)


#created a draw function to draw the shapes in a list 
def draw(shape,win):
    for item in shape:
        item.draw(win)

#defined the main function where the function are tested 
def main():
    #draw graphics window
    win = gr.GraphWin("checkers", 1550, 1300)

    #draw checkers board 
    block1 = init_checkerboard(300,100,1)
    block2 = init_checkerboxes(350,100,1)
    
    #create the array of white checker pieces
    whitepieces = init_whitecheckers()

    #create the array of black checker pieces
    blackpieces = init_blackcheckers()

    #draw the sqaures on board
    draw(block1,win)
    draw(block2,win)

    #TESTER white pieces should be drawn on board
    draw(whitepieces,win)
    draw(blackpieces,win)

    # print(whitepieces)

    

    win.getMouse()

    win.close()

  
        
#code is executed here.
if __name__ == "__main__":
    main()





