
import os,sys
import pygame  #lazy but responsible (avoid namespace flooding)

class Character:
    def __init__(self,rect):
        self.rect = pygame.Rect(rect)
        self.image = pygame.image.load('pussy2.png').convert_alpha()
        #self.image.fill((255,255,255))

    def update(self,surface):
        self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image,self.rect)

def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)


def game_event_loop(Player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()



pygame.init()
Screen = pygame.display.set_mode((1000,600))
MyClock = pygame.time.Clock()
MyPlayer = Character((0,0,100,100))


while 1:
    main(Screen,MyPlayer)
    pygame.display.update()
    MyClock.tick(60)