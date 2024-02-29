import turtle
import random
import time

screen = turtle.Screen()
screen.setup(500, 500)

# Responsible for drawing out the spaces and the letters
letter_spaces = turtle.Turtle()
letter_spaces.speed(0)
letter_spaces.color('black')
letter_spaces.hideturtle()
letter_spaces.penup()

# Responsible for drawing out the hook and body
game_turtle = turtle.Turtle()
game_turtle.speed(0)
game_turtle.color('black')
game_turtle.hideturtle()
game_turtle.penup()

# Responsible for drawing out the start-up page graphics and buttons
optionsTurtle = turtle.Turtle()
optionsTurtle.speed(0)
optionsTurtle.hideturtle()

words = ['About', 'Alert', 'Argue', 'Also', 'Able', 'Acid' 'Hear', 'Beach', 'Fix', 'Own', 'Bed', 'Hen']
chosen_word = random.choice(words)
chosen_word_length = len(chosen_word)

letters_dictionary = {}
for letter in chosen_word:
    letter = letter.lower()
    letters_dictionary[f"letter_{letter}"] = letter
    # print(f"letter_{letter}")

class Body():
    def drawHead(self):
        game_turtle.penup()
        game_turtle.goto(-11.5, 100)
        game_turtle.pendown()     
        game_turtle.circle(13, 360)
    def drawBody(self):
        game_turtle.penup()
        game_turtle.goto(0, 90)
        game_turtle.setheading(270)
        game_turtle.pendown()
        game_turtle.forward(75)
    def drawLeftArm(self):
        game_turtle.penup()
        game_turtle.goto(0, 70)
        game_turtle.setheading(220)
        game_turtle.pendown()
        game_turtle.forward(35)
    def drawRightArm(self):
        game_turtle.penup()
        game_turtle.goto(0, 70)
        game_turtle.setheading(320)
        game_turtle.pendown()
        game_turtle.forward(35)
    def drawLeftLeg(self):
        game_turtle.penup()
        game_turtle.goto(0, 15)
        game_turtle.setheading(240)
        game_turtle.pendown()
        game_turtle.forward(35)
    def drawRightLeg(self):
        game_turtle.penup()
        game_turtle.goto(0, 15)
        game_turtle.setheading(300)
        game_turtle.pendown()
        game_turtle.forward(35)

class BodyOutline():
    def drawHead(self):
        game_turtle.penup()
        game_turtle.goto(-12.5, 105)
        game_turtle.pendown()     
        game_turtle.circle(13, 360)
    def drawBody(self):
        game_turtle.penup()
        game_turtle.goto(0, 90)
        game_turtle.setheading(270)
        game_turtle.pendown()
        game_turtle.forward(75)
    def drawLeftArm(self):
        game_turtle.penup()
        game_turtle.goto(0, 70)
        game_turtle.setheading(220)
        game_turtle.pendown()
        game_turtle.forward(35)
    def drawRightArm(self):
        game_turtle.penup()
        game_turtle.goto(0, 70)
        game_turtle.setheading(320)
        game_turtle.pendown()
        game_turtle.forward(35)
    def drawLeftLeg(self):
        game_turtle.penup()
        game_turtle.goto(0, 15)
        game_turtle.setheading(240)
        game_turtle.pendown()
        game_turtle.forward(35)
    def drawRightLeg(self):
        game_turtle.penup()
        game_turtle.goto(0, 15)
        game_turtle.setheading(300)
        game_turtle.pendown()
        game_turtle.forward(35)

def drawHomepageGraphic():
    # Draw hanging arm
    optionsTurtle.color('black')
    optionsTurtle.penup()
    optionsTurtle.goto(120,175)
    optionsTurtle.setheading(270)
    optionsTurtle.pendown()
    optionsTurtle.forward(35)
    
    # Draw body
    optionsTurtle.penup()
    optionsTurtle.goto(135, 156)
    optionsTurtle.setheading(230)
    optionsTurtle.pendown()
    optionsTurtle.forward(75)
    
    # Draw head
    optionsTurtle.penup()
    optionsTurtle.goto(132, 173)
    optionsTurtle.pendown()
    optionsTurtle.circle(13, 360)
    
    # Draw dangling arm
    optionsTurtle.penup()
    optionsTurtle.goto(120,140)
    optionsTurtle.setheading(280)
    optionsTurtle.pendown()
    optionsTurtle.forward(35)
    
    # Draw right foot (upper foot)
    optionsTurtle.penup()
    optionsTurtle.goto(85, 100)
    optionsTurtle.setheading(200)
    optionsTurtle.pendown()
    optionsTurtle.forward(35)
    
    # Draw right foot (upper foot)
    optionsTurtle.penup()
    optionsTurtle.goto(88, 100)
    optionsTurtle.setheading(270)
    optionsTurtle.pendown()
    optionsTurtle.forward(35)
    
    # Draw out the word "H _ _ P !"
    word = 'H LP'
    optionsTurtle.penup()
    optionsTurtle.setheading(0)
    optionsTurtle.goto(-225, 100)
    for letter in word:
        time.sleep(0.05)
        # Draw line
        optionsTurtle.pendown()
        optionsTurtle.forward(35)
        # Write letter
        optionsTurtle.penup()
        optionsTurtle.backward(17.5)
        optionsTurtle.write(letter, move=False, align='center', font=('Calibri', 25, 'bold'))
        optionsTurtle.forward(17.5)
        # Move forward
        optionsTurtle.penup()
        optionsTurtle.forward(20)
    # Write exclamation mark
    optionsTurtle.penup()
    optionsTurtle.write('!', move=False, align='center', font=('Calibri', 25, 'bold'))

def drawButtons(x,y, text, fontsize, up):
    optionsTurtle.penup()
    optionsTurtle.goto(x,y)
    optionsTurtle.pendown()
    optionsTurtle.begin_fill()
    for i in range(2):
        optionsTurtle.forward(200)
        optionsTurtle.left(90)
        optionsTurtle.forward(75)
        optionsTurtle.left(90)
    optionsTurtle.end_fill()
    optionsTurtle.penup()
    optionsTurtle.goto(x+100, y+up)
    optionsTurtle.write(text, align="center", font=("Calibri", fontsize, "normal"))

def drawOptions():
    # Draw out a title and list the options as buttons to click
    # 1. Play the Game
    # 2. View previous games
    # 3. Exit the game
    optionsTurtle.penup()
    optionsTurtle.goto(0,180)
    optionsTurtle.write("Welcome to Han  man", align="center", font=("Calibri", 35, "bold"))
    optionsTurtle.goto(120,170)
    optionsTurtle.write("g", align="center", font=("Calibri", 35, "bold"))
    
    # Draw all buttons button
    optionsTurtle.pencolor("black")
    optionsTurtle.width(3)
    optionsTurtle.fillcolor("orange")
    drawButtons(x=-100, y=-50, text="Play", fontsize=35, up=10)
    drawButtons(x=-100, y=-140, text="View History", fontsize=25, up=17)
    drawButtons(x=-100, y=-230, text="Exit", fontsize=35, up=10)

    # drawHomepageGraphic()

def inGameDecider(x,y):
    if -225 < x < -125:
        if 200 < y < 237.5:
            # Close the screen
            screen.bye()

# In this function, call all the functions that draw the needed graphics
def decider(x,y):
    # print(f"{x}, {y}")
    if -100 < x < 101:
        if -50 < y < 25:
            # Play the game
            optionsTurtle.clear()
            screen.onscreenclick(inGameDecider)
            drawExitButton()
            drawLetterSpaces()
            drawStand()
        elif -140 < y < -65:
            # Open the scores notepad
            pass
        elif -230 < y < -155:
            # Close the screen
            screen.bye()

# Draw the letter spaces
def drawLetterSpaces():
    # letter_spaces.goto(-200, -150) # -200 on x-axis for a 5-letter word
    letter_spaces.goto(-(chosen_word_length*40), -150)
    for letter in chosen_word:
        time.sleep(0.05)
        # Draw line
        letter_spaces.pendown()
        letter_spaces.forward(50)
        # Write letter - REMOVE THIS LATER
        letter_spaces.penup()
        letter_spaces.backward(25)
        letter_spaces.write(letter.upper(), move=False, align='center', font=('Calibri', 25, 'bold'))
        letter_spaces.forward(25)
        # Move forward
        letter_spaces.penup()
        letter_spaces.forward(35)

def drawExitButton():
    optionsTurtle.penup()
    optionsTurtle.goto(-225,200)
    optionsTurtle.pendown()
    optionsTurtle.fillcolor('orange')
    optionsTurtle.begin_fill()
    for i in range(2):
        optionsTurtle.forward(100)
        optionsTurtle.left(90)
        optionsTurtle.forward(37.5)
        optionsTurtle.left(90)
    optionsTurtle.end_fill()
    optionsTurtle.penup()
    optionsTurtle.goto(-175, 205)
    optionsTurtle.write('Exit', align="center", font=("Calibri", 15, "normal"))

# Draw the stand, includes body outline
def drawStand():
    game_turtle.color('red')
    # Draw base
    game_turtle.penup()
    game_turtle.width(5)
    game_turtle.goto(-250, 150)
    game_turtle.setheading(0)
    game_turtle.pendown()
    game_turtle.forward(250)

    # Draw hook
    game_turtle.penup()
    game_turtle.setheading(270)
    game_turtle.pendown()
    game_turtle.forward(30)

    game_turtle.color(230/255, 230/255, 230/255)  # Gray color (RGB values scaled to 0-1 range)
    body = BodyOutline()
    body.drawHead()
    body.drawBody()
    body.drawLeftArm()
    body.drawRightArm()
    body.drawLeftLeg()
    body.drawRightLeg()
    
    # THIS DRAWS THE ACTUAL BODY, JUST FOR TESTING
    # REMOVE WHEN YOU START WITH THE PROGRAM
    game_turtle.color('black')
    # game_turtle.speed(8)
    body2 = Body()
    body2.drawHead()
    body2.drawBody()
    body2.drawLeftArm()
    body2.drawRightArm()
    body2.drawLeftLeg()
    body2.drawRightLeg()



drawOptions()
screen.onscreenclick(decider)


screen.mainloop()