import pygame

# -----------------------------------------------
# -----------------------------------------------

"""
Justin Andrews
Spring 2020
CS455 - Artificial Intelligence
Final Project - Peg Game

File Description:
This file contains functions needed to display the game.

Function Declarations:
    board(screen)
    
    placeHolder(screen, x, y)
    
    placePeg(screen, x, y)
    
    setBoard(pegs, screen)
"""

# -----------------------------------------------
# -----------------------------------------------
# DISPLAY VARIABLES


# load image to be used for the board
boardImage = pygame.image.load('images/pegBoard.png')

# set board x location
boardX = 200

# set board y location
boardY = 100

# load peg and peg place holder images
pegImage = pygame.image.load('images/redPeg.png')
holderImage = pygame.image.load('images/blackCircle.png')

# centers of peg holes for reference
pegHoleCenterX = [501, 446, 555, 388, 502, 614, 330, 445, 552, 673, 275, 386, 500, 609, 733]
pegHoleCenterY = [186, 277, 275, 372, 375, 373, 469, 469, 469, 468, 565, 565, 565, 565, 565]

# where to actually place pegs and peg place holders
pegHoleX = [x - 17.5 for x in pegHoleCenterX]
pegHoleY = [y - 17.5 for y in pegHoleCenterY]


# -----------------------------------------------
# -----------------------------------------------


def board(screen):

    """
    Function Description:
    This function draws the board to the screen. It also draws 3 text boxes to the screen that act as buttons.
    The first text box is used to initiate the Breadth First Search algorithm.
    The second text box is used to initiate the Depth First Search algorithm.
    The thirds text box is used to clear the array of clicks if a miss click was made while doing a move.

    :param screen: this function takes the parameter screen which is used to display the graphics to the screen
    :return: this function has no return, the output is purely graphical
    """

    # DRAW BOARD
    # place board at x,y
    screen.blit(boardImage, (boardX, boardY))

    # FORMAT TEXT
    # format text for search algorithm buttons
    textFormatAlgorithm = pygame.font.SysFont("arial", 32)

    # DRAW BFS BUTTON
    # create text for BFS search algorithm button
    textBFS = textFormatAlgorithm.render("Click here to run BFS search algorithm!", True, (0, 0, 0))

    # place BFS search algorithm text on screen
    screen.blit(textBFS, (10, 10))

    # DRAW DFS BUTTON
    # create text for DFS search algorithm button
    textDFS = textFormatAlgorithm.render("Click here to run DFS search algorithm!", True, (0, 0, 0))

    # place DFS search algorithm text on screen
    screen.blit(textDFS, (530, 10))

    # DRAW CLEAR CLICKS BUTTON
    # format text for clear clicks button
    textFormatClicks = pygame.font.SysFont("arial", 25)

    # create text for clear clicks button
    text = textFormatClicks.render("Click here to clear clicks!", True, (0, 0, 0))

    # place clear clicks text on screen
    screen.blit(text, (390, 680))


# -----------------------------------------------


def placeHolder(screen, x, y):

    """
    Function Description:
    This function draws black circles to the board to indicate what peg holes are empty.

    :param screen: this function takes the parameter screen to display the graphics to the screen
    :param x: this function takes x, the x location of the graphic
    :param y: this function takes y, the y location of the graphic
    :return: this function has no return, the output is purely graphical
    """

    # place empty hole at x,y
    screen.blit(holderImage, (x, y))


# -----------------------------------------------


def placePeg(screen, x, y):

    """
    Function Description:
    This function draws the pegs to the board to indicate the game pieces.

    :param screen: this function takes the parameter screen to display the graphics to the screen
    :param x: this function takes x, the x location of the graphic
    :param y: this function takes y, the y location of the graphic
    :return: this function has no return, the output is purely graphic
    """

    # place peg on screen at x,y
    screen.blit(pegImage, (x, y))


# -----------------------------------------------


# create starting board positions
# this function takes emptyLoc which is the location of the peg hole that will start empty
# peg hole numbering starts at 0 and goes to 14 from top to bottom, left to right (see attached reference image)
def setBoard(pegs, screen):

    """
    Function Description:
    This function sets the board with pegs and black circles to represent the empty holes.
    This function is called to update the board with the new game state of pegs after moves are completed.

    :param pegs: this function takes the parameter pegs, an array of true and false values
     to represent if pegs are at that peg hole - true, or if the hole is empty - false
    :param screen: this function takes the parameter screen to display the graphics to
    :return pegs: return the array pegs that holds true and false values for peg positions
    """

    # arrange True and False to correspond with correct peg locations
    for i in range(len(pegs)):

        # if peg not in hole
        if not pegs[i]:

            # place black circle to show that no peg is at that location
            placeHolder(screen, pegHoleX[i], pegHoleY[i])

        # if peg in hole
        else:

            # place peg at location
            placePeg(screen, pegHoleX[i], pegHoleY[i])

    # return array of where pegs are located
    return pegs
