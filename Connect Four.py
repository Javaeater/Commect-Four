import numpy as np
import pygame
import sys
import math


BLUE =(10,5,230)
GREY = (192,192,192)
RED = (155, 17, 30)
GOLD = (255,215,0)
BLACK = (0,0,0)
ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = int(100)
RAD = int(SQUARESIZE/2 - 4)
game_over = False
turn = 0

#Creates a game board matrix
def create_game_board():
    board = np.zeros((6,7))
    return board

#Drop game piece at player coloum and next open row
def piece_drop(board, row, col, piece):
    board[row][col] = piece

#Checks if coloum is full
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

#Finds next open row
def next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#Flip the numpy matrix from top to bottom to bottom to top.
def print_board(board):
    print(np.flip(board, 0))

#Check if game has been won
def game_won(board, piece):

    #Check the horizontal locations for a win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            #Check vertical for win
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True


        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True


        for c in range(COL_COUNT -3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

#Draw the game board
def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(displayscreen, BLUE, (c*SQUARESIZE, r* SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(displayscreen, GREY, ((c*SQUARESIZE+SQUARESIZE//2), (r* SQUARESIZE + SQUARESIZE+SQUARESIZE //2)), RAD)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(displayscreen, RED,((c * SQUARESIZE + SQUARESIZE // 2), height -(r * SQUARESIZE + SQUARESIZE // 2)),RAD)
            elif board [r][c] == 2:
                pygame.draw.circle(displayscreen, GOLD,((c * SQUARESIZE + SQUARESIZE // 2), height -(r * SQUARESIZE + SQUARESIZE // 2)),RAD)

#check if the game is a tie
def is_tie(board):
    count = 0
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 0:
                count += 1


    if count == 0:
        return True

#check if the row is full
def is_full(board, col):
    count = 0


    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            count += 1


    if count == 0:
            return True


pygame.init()
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
board = create_game_board()
displayscreen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("futura", 75)

# Main loop
while not game_over:

    #allow for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Check for mouse movement
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(displayscreen, GREY, (0,0, width, SQUARESIZE))
            xpos = event.pos[0]
            if turn == 0:
                pygame.draw.circle(displayscreen, RED, (xpos, (SQUARESIZE//2)), RAD)
            else:
                pygame.draw.circle(displayscreen, GOLD, (xpos, (SQUARESIZE // 2)), RAD)
        pygame.display.update()

        #Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(displayscreen, GREY, (0, 0, width, SQUARESIZE))
            if turn == 0:
                xpos = event.pos[0]
                col = int(math.floor(xpos/SQUARESIZE))


                if is_full(board, col):
                    label = myfont.render("Row Full", 1, BLACK)
                    displayscreen.blit(label, (150, 15))
                    pygame.display.update()
                    turn += 1


                if is_valid_location(board, col):
                     row = next_open_row(board, col)
                     piece_drop(board, row, col, 1)
                     draw_board(board)


                     if game_won(board, 1):
                         label = myfont.render("Player 1 wins!", 1, RED)
                         displayscreen.blit(label, (150,15))
                         pygame.display.update()
                         pygame.time.wait(3000)
                         game_over = True

                     if is_tie(board):
                         label = myfont.render("Game Tie", 1, BLACK)
                         displayscreen.blit(label, (170, 15))
                         pygame.display.update()
                         pygame.time.wait(3000)
                         game_over = True


            #Second player mouse click
            else:
                xpos = event.pos[0]
                col = int(math.floor(xpos/SQUARESIZE))


                if is_full(board, col):
                    label = myfont.render("Row Full", 1, BLACK)
                    displayscreen.blit(label, (150, 15))
                    pygame.display.update()
                    turn += 1

                if is_valid_location(board, col):
                    row = next_open_row(board, col)
                    piece_drop(board, row, col, 2)
                    draw_board(board)


                    if game_won(board,2):
                        label = myfont.render("Player 2 wins!!", 2, GOLD)
                        displayscreen.blit(label, (150, 15))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        game_over = True


                    if is_tie(board):
                        label = myfont.render("Game Tie", 1, BLACK)
                        displayscreen.blit(label, (170, 15))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        game_over = True

            #print_board(board)
            draw_board(board)
            turn += 1
            turn = turn % 2



