import pygame, sys
from player import *
pygame.font.init()


STATUS = [[0,0,0],[0,0,0],[0,0,0]]
BLACK = (0,0,0)
GREY = (100,100,100)
WHITE = (255,255,255)
WIDTH,HEIGHT = 1300,1300
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
FONT = pygame.font.SysFont('comicsans',100)

BORDER = 12
BOX = pygame.Rect(0,0,(WIDTH-2*BORDER)/3,(HEIGHT-2*BORDER)/3)

pl = [Player("You","X",((WIDTH-2*BORDER)/3,(HEIGHT-2*BORDER)/3)),Player("Enemy","O",((WIDTH-2*BORDER)/3,(HEIGHT-2*BORDER)/3))]


def draw_window():
    WIN.fill(BLACK)
    
    BOX.y = 0
    for i in range(3):
        BOX.x = 0
        for j in range(3):
            pygame.draw.rect(WIN,WHITE,BOX)
            BOX.x += BOX.width + BORDER
        BOX.y += BOX.height + BORDER

    pygame.display.update()


def draw_winner(text):
    winner_text = FONT.render(text,1,GREY)
    WIN.blit(winner_text,(WIDTH/2-winner_text.get_width()/2,HEIGHT/2-winner_text.get_height()/2))
    pygame.display.update()
    post_end_loop()

def post_end_loop():
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def main():
    counter = 0
    draw_window()
    clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        if  STATUS[0].count(0) == 0 and STATUS[1].count(0) == 0 and STATUS[2].count(0) == 0:
            draw_winner("Tie")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == X_WON:
                draw_winner(pl[0].name + " Win")
            elif event.type == O_WON:
                draw_winner(pl[1].name + " Wins")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = [pos[0]//(BOX.width+2*BORDER//3),pos[1]//(BOX.height+2*BORDER//3)]
                if STATUS[pos[0]][pos[1]] == 0:
                    STATUS[pos[0]][pos[1]] = pl[counter%2].type
                    pl[counter%2].check(STATUS)
                    WIN.blit(pl[counter%2].image,((BOX.width + BORDER)*pos[0],(BOX.height + BORDER)*pos[1]))
                    pygame.display.update()
                    counter += 1

main()
