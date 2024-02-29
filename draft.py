import turtle
import random
import time

words = ['About', 'Alert', 'Argue', 'Also', 'Able', 'Acid' 'Hear', 'Beach', 'Fix', 'Own', 'Bed', 'Hen']
chosen_word = random.choice(words)

letters_dictionary = {}
for letter in chosen_word:
    letter = letter.lower()
    letters_dictionary[f"letter_{letter}"] = letter
    print(f"letter_{letter}")



chosen_word_length = len(chosen_word)

optionsTurtle = turtle.Turtle()
optionsTurtle.speed(0)
optionsTurtle.hideturtle()


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
    # 3. View directions on how to play the game
    # 4. Exit the game
    # This should be spanned out across a 600x500 canvas
    optionsTurtle.penup()
    optionsTurtle.goto(0,180)
    optionsTurtle.write("Welcome to Hangman", align="center", font=("Calibri", 35, "bold"))
    
    # Write the directions for how to play
    optionsTurtle.penup()
    optionsTurtle.goto(0,45)
    # optionsTurtle.write(f"                                                                In this game,\nyou must guess the hidden word one letter at a time before the full body\nis drawn out\n                        After every turtle click, you will earn one point\n   Every time you click a turtle, it will stamp and move to a new location\n                                                    Good Luck!", align="center", font=("Calibri", 12, "bold"))

    # Draw "Play" button
    optionsTurtle.pencolor("black")
    optionsTurtle.width(3)
    optionsTurtle.fillcolor("orange")
    drawButtons(x=-100, y=-50, text="Play", fontsize=35, up=10)
    drawButtons(x=-100, y=-140, text="View History", fontsize=25, up=17)
    drawButtons(x=-100, y=-230, text="Exit", fontsize=35, up=10)


def decider(x,y):
    # print(f"{x}, {y}")
    if -100 < x < 101:
        if -50 < y < 25:
            # Play the game
            optionsTurtle.clear()
            screen.onscreenclick(None)
            drawLetterSpaces()
        elif -140 < y < -65:
            # Open the scores notepad
            pass
        elif -230 < y < -155:
            # Close the screen
            screen.bye()


screen = turtle.Screen()
screen.setup(500, 500)

letter_spaces = turtle.Turtle()
letter_spaces.speed(0)
letter_spaces.color('black')
letter_spaces.hideturtle()
letter_spaces.penup()
# letter_spaces.goto(-200, -150) # -200 on x-axis for a 5-letter word

# Draw the letter spaces
def drawLetterSpaces():
    letter_spaces.goto(-(chosen_word_length*40), -150)
    for i in range(chosen_word_length):
        time.sleep(0.05)
        letter_spaces.pendown()
        letter_spaces.forward(50)
        letter_spaces.penup()
        letter_spaces.forward(35)

drawOptions()
screen.onscreenclick(decider)


screen.mainloop()