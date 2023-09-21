import pygame,os

X_WON = pygame.USEREVENT + 1
O_WON = pygame.USEREVENT + 2

class Player:
    def __init__(self,name,type,dimensions):
        self.name = name
        self.type = type
        self.image = pygame.transform.scale(pygame.image.load(type+'.png'),dimensions)
    
    def check(self,st):
        if (st[0][0] == self.type and st[1][1] == self.type and st[2][2] == self.type) or (st[0][2] == self.type and st[1][1] == self.type and st[2][0] == self.type):
            if st[1][1] == "X":
                pygame.event.post(pygame.event.Event(X_WON))
            else:
                pygame.event.post(pygame.event.Event(O_WON))
        for i in range (3):
            if st[i] == [self.type,self.type,self.type] or (st[0][i] == self.type and st[1][i] == self.type and st[2][i] == self.type) :
                if st[i][i] == "X":
                    pygame.event.post(pygame.event.Event(X_WON))
                else:
                    pygame.event.post(pygame.event.Event(O_WON))