from datetime import date, datetime
# import datetime
from tkinter import messagebox
import turtle
import random
import time
import os

os.system('cls')

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

words = [
    "cat", "dog", "run", "sun", "hat", "man", "fan", "ice", "red", "pen",
    "book", "ball", "frog", "duck", "lamp", "cake", "bell", "door", "snake", "beach",
    "apple", "chair", "table", "water", "house", "music", "happy", "grass", "ocean", "sunny",
    "glove", "lemon", "queen", "shoes", "watch", "fence", "sword", "storm", "ghost", "beard",
    "fairy", "frank", "candy", "earth", "beard", "kite", "zebra", "snake", "frank", "queen",
    "giant", "clock", "money", "piano", "juice", "santa", "puzzle", "summer", "orange", "rocket",
    "cookie", "banana", "purple", "sponge", "guitar", "jacket", "rocket", "rocket", "rocket"
]

# words = ['Mahdi Salloum']
chosen_word = random.choice(words)
print(chosen_word)
chosen_word_length = len(chosen_word)

correctly_guessed_letters = []
incorrectly_guessed_letters = []
letters_list = []
for letter in chosen_word:
    letter = letter.lower()
    letters_list.append(letter)
    # print(f"letter_{letter}")

class Body():
    def drawHead(self):
        game_turtle.penup()
        game_turtle.goto(-0.5, 90)
        game_turtle.setheading(0)
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

def flashBodyPart(turtle, function):
    screen.onscreenclick(None)
    turtle.color('black')
    function()
    time.sleep(0.05)
    turtle.color('red')
    function()
    time.sleep(0.05)
    turtle.color('black')
    function()
    time.sleep(0.05)
    turtle.color('red')
    function()
    time.sleep(0.05)
    turtle.color('black')
    function()
    time.sleep(0.05)
    turtle.color('red')
    function()
    time.sleep(0.05)
    turtle.color('black')
    function()
    time.sleep(0.05)
    screen.onscreenclick(inGameDecider)

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

    drawHomepageGraphic()

def get_input_with_limit(title, prompt, length_requirement):
    user_input = screen.textinput(title, prompt)
    try:
        while len(user_input) > length_requirement or len(user_input) < length_requirement:
            user_input = screen.textinput(title, f"Please enter a valid input\nIt should be {length_requirement} letter")
        playGame(user_input)
    except:
        pass

# In-game click decider for in-game buttons
def inGameDecider(x,y):
    if -225 < x < -125:
        if 200 < y < 237.5:
            # Close the screen
            screen.bye()
    if -100 < x < 100:
        if -125 < y < -50:
            global total_guesses
            total_guesses += 1
            get_input_with_limit("Guess", "Guess a letter!", 1)

# Post-game click decider for post-game buttons
def postGameDecider(x,y):
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
            playGame(None)
            # print(letters_list)

        elif -140 < y < -65:
            # Open the scores notepad
            try:
                os.system('start scores.txt')
            except:
                messagebox.showinfo('Error', "You have not played any games yet.\nClick play to begin!")    
        elif -230 < y < -155:
            # Close the screen
            screen.bye()

# Draw the letter spaces
def drawLetterSpaces():
    # letter_spaces.goto(-200, -150) # -200 on x-axis for a 5-letter word
    letter_spaces.goto(-(chosen_word_length*40), -190)
    for letter in chosen_word:
        time.sleep(0.05)
        # Draw line
        letter_spaces.pendown()
        letter_spaces.forward(50)
        # Write letter - REMOVE THIS LATER
        # letter_spaces.penup()
        # letter_spaces.backward(25)
        # letter_spaces.write(letter.upper(), move=False, align='center', font=('Calibri', 25, 'bold'))
        # letter_spaces.forward(25)
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


    # Draw outline
    game_turtle.color(240/255, 240/255, 240/255)  # Gray color (RGB values scaled from 0 to 1)
    # game_turtle.color('black')
    body = Body()
    body.drawHead()
    body.drawBody()
    body.drawLeftArm()
    body.drawRightArm()
    body.drawLeftLeg()
    body.drawRightLeg()

def gameLost():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(-200,-65)
    turtle.pencolor("black")
    turtle.width(5)
    turtle.fillcolor("yellow")
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write("Game's Over!", align="center", font=("Calibri", 50, "bold"))
    turtle.penup()
    turtle.goto(0,-50)
    turtle.pendown()
    turtle.write(f"     Total Guesses: {total_guesses}\nCorrect Word: {chosen_word}", align="center", font=("Calibri", 20, "bold"))
    turtle.penup()
    turtle.goto(0,-65)
    # turtle.write(f"(Click anywhere to go back home)", align="center", font=("Calibri", 12, "bold"))
    screen.onscreenclick(postGameDecider)
    file = open("scores.txt", "a")
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    file.write(f"Date Played: Date Played: {today} @ {current_time}\nGame Lost -- Word to guess: {chosen_word} -- Number of Guesses: {total_guesses}\n{'-'*60}\n")
    file.close()

def gameWon():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(-200,-65)
    turtle.pencolor("black")
    turtle.width(5)
    turtle.fillcolor("yellow")
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.write("You Won!", align="center", font=("Calibri", 50, "bold"))
    turtle.penup()
    turtle.goto(0,-50)
    turtle.pendown()
    turtle.write(f"     Total Guesses: {total_guesses}", align="center", font=("Calibri", 20, "bold"))
    turtle.penup()
    turtle.goto(0,-65)
    # turtle.write(f"(Click anywhere to go back home)", align="center", font=("Calibri", 12, "bold"))
    screen.onscreenclick(postGameDecider)
    file = open("scores.txt", "a")
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    file.write(f"Date Played: {today} @ {current_time}\nGame Won -- Word to guess: {chosen_word} -- Number of Guesses: {total_guesses}\n{'-'*60}\n")
    file.close()

# Track the number of incorrect guesses
incorrect = -1
total_guesses = 0

def playGame(input):
    global incorrect
    body = Body()
    game_turtle.color('black')

    input = str(input).lower()
    drawButtons(x=-100, y=-125, text="Take a Guess!", fontsize=20, up=20)

    # Check if the guessed letter has already been guessed
    if input in correctly_guessed_letters:
        messagebox.showinfo("Error!", "You already guessed this letter")
    elif input in incorrectly_guessed_letters:
        messagebox.showinfo("Error!", "You already guessed this letter")

    else:
        # Tracker to track if the guessed letter is found in the word
        found_letter = False


        # Loop through each letter in the word
        # the 'index' will give you what positoin the letter in the word  is
        for index, letter in enumerate(chosen_word):
            if letter.lower() == input:
                found_letter = True

                # Write the guessed letter in the corresponding space
                letter_spaces.goto(-(chosen_word_length*40) + (index * 85), -190)
                letter_spaces.penup()
                letter_spaces.forward(25)
                letter_spaces.write(input.upper(), move=False, align='center', font=('Calibri', 25, 'bold'))

        # If the guessed letter was found in the word
        if found_letter:
            # Add the guessed letter to the list of guessed letters
            correctly_guessed_letters.append(input)
            # print(correctly_guessed_letters)

            # If all letters have been guessed, end the game
            if len(correctly_guessed_letters) == len(set(letters_list)):
                # print(f'YOU FINISHED THE GAME IN {total_guesses} GUESSES')
                gameWon()
                
        else:
            incorrectly_guessed_letters.append(input)
            incorrect += 1
            if incorrect == 1:
                body.drawHead()
                flashBodyPart(game_turtle, body.drawHead)
            if incorrect == 2:
                body.drawBody()
                flashBodyPart(game_turtle, body.drawBody)
            if incorrect == 3:
                body.drawLeftArm()
                flashBodyPart(game_turtle, body.drawLeftArm)
            if incorrect == 4:
                body.drawRightArm()
                flashBodyPart(game_turtle, body.drawRightArm)
            if incorrect == 5:
                body.drawLeftLeg()
                flashBodyPart(game_turtle, body.drawLeftLeg)
            if incorrect == 6:
                body.drawRightLeg()
                flashBodyPart(game_turtle, body.drawRightLeg)
                gameLost()


drawOptions()
screen.onscreenclick(decider)


screen.mainloop()
