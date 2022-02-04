import pygame
from pygame.locals import *
import time
pygame.init()

brown = (200,100,10)
blue = (100,100,200)
white = (255,255,255)
z = 0; i=0; cross = [0,0,0,0,0,0,0,0] ; ring = [0,0,0,0,0,0,0,0]

class Square(pygame.sprite.Sprite):
    def __init__(self,*args):
        super(Square,self).__init__(*args)
        
        self.surf = []
        #for i in range(9):self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        self.surf.append(pygame.image.load('bluesquare.png'))
        
        self.rect = []
        
        self.rect.append (self.surf[0].get_rect())
        self.rect.append(self.surf[1].get_rect( topleft = (self.rect[0].width,self.rect[0].top)))
        self.rect.append(self.surf[2].get_rect( topleft = (self.rect[1].right,self.rect[1].top)))
        
        self.rect.append(self.surf[3].get_rect( topleft = (0,self.rect[0].bottom)))
        self.rect.append(self.surf[4].get_rect( topleft = (self.rect[3].right,self.rect[3].top)))
        self.rect.append(self.surf[5].get_rect( topleft = (self.rect[4].right,self.rect[4].top)))
        
        self.rect.append(self.surf[6].get_rect( topleft = (0,self.rect[3].bottom)))
        self.rect.append(self.surf[7].get_rect( topleft = (self.rect[6].right,self.rect[6].top)))
        self.rect.append(self.surf[8].get_rect( topleft = (self.rect[7].right,self.rect[7].top)))

    def mouseClick(self,x,y,z):
        if 0 < x < self.rect[0].right and 0 < y < self.rect[0].bottom:
            i = 0
            if z == 1: 
                zd = self.drawCross(z,i)
                cross[0] +=1; cross[3] += 1; cross[6] += 1
            else: 
                zd = self.drawRing(z,i)
                ring[0] += 1; ring[3] += 1; ring[6] += 1
        elif self.rect[1].left < x < self.rect[1].right and 0 < y < self.rect[1].bottom:
            i = 1
            if z == 1: 
                zd = self.drawCross(z,i)
                cross[0] +=1; cross[4]+=1
            else: 
                zd = self.drawRing(z,i)
                ring[0] +=1; ring[4]+=1
        elif self.rect[2].left < x < self.rect[2].right and 0 < y < self.rect[2].bottom:
            i = 2
            if z == 1: 
                zd = self.drawCross(z,i)
                cross[0] += 1; cross[5] += 1; cross[7] += 1
            else: 
                zd = self.drawRing(z,i)
                ring[0] += 1; ring[5] += 1; ring[7] += 1
        
        elif 0 < x < self.rect[3].right and self.rect[3].top < y < self.rect[3].bottom:
            i = 3
            if z == 1: 
                zd = self.drawCross(z,i)
                cross[1] += 1; cross[3]+=1
            else: 
                zd = self.drawRing(z,i)
                ring[1] += 1; ring[3]+=1
        elif self.rect[4].left < x < self.rect[4].right and self.rect[4].top < y < self.rect[4].bottom:
            i = 4
            if z == 1: 
                zd = self.drawCross(z,i)
                cross[1] += 1; cross[4]+=1; cross[6] += 1; cross[7] += 1
            else: 
                zd = self.drawRing(z,i)
                ring[1] += 1; ring[4]+=1; ring[6] += 1; ring[7] += 1
        elif self.rect[5].left < x < self.rect[5].right and self.rect[5].top < y < self.rect[5].bottom:
            i = 5
            if z == 1: 
                zd = self.drawCross(z,i)
                cross[1] += 1; cross[5] += 1
            else: 
                zd = self.drawRing(z,i)
                ring[1] += 1; ring[5] += 1
        
        elif 0 < x < self.rect[6].right and self.rect[6].top < y < self.rect[6].bottom:
            i = 6
            if z == 1:
                zd = self.drawCross(z,i)
                cross[2] += 1; cross[3] += 1; cross[7] += 1
            else:
                zd = self.drawRing(z,i)
                ring[2] +=1; ring[3] += 1; ring[7] += 1
        elif self.rect[7].left < x < self.rect[7].right and self.rect[7].top < y < self.rect[7].bottom:
            i = 7
            if z == 1:
                zd = self.drawCross(z,i)
                cross[2] += 1; cross[4]+=1
            else:
                zd = self.drawRing(z,i)
                ring[2] += 1; ring[4]+=1
        elif self.rect[8].left < x < self.rect[8].right and self.rect[8].top < y < self.rect[8].bottom:
            i = 8
            if z == 1:
                zd = self.drawCross(z,i)
                cross[2] += 1; cross[5] += 1; cross[6] += 1
            else:
                zd = self.drawRing(z,i)
                ring[2] += 1; ring[5] += 1; ring[6] += 1
        return zd, i
    
    def drawCross(self,z,i):
        z = 0
        self.surf[i] = pygame.image.load('blackcross.png')
        screen.blit(self.surf[i], (self.rect[i].left, self.rect[i].top))
        return z

    def drawRing(self,z,i):
        z = 1
        self.surf[i] = pygame.image.load('bluering.png')
        screen.blit(self.surf[i], (self.rect[i].left, self.rect[i].top))
        return z
   
    def line(self,cross,ring):
        if cross[0] == 3 or ring[0] == 3:
            pygame.draw.line(screen,brown,(square.rect[0].left,square.rect[0].centery),(square.rect[2].right,square.rect[2].centery),8)
            return False
        elif cross[1] == 3 or ring[1] == 3:
            pygame.draw.line(screen,brown,(square.rect[3].left,square.rect[3].centery),(square.rect[5].right,square.rect[5].centery),8)
            return False
        elif cross[2] == 3 or ring[2] == 3:
            pygame.draw.line(screen,brown,(square.rect[6].left,square.rect[6].centery),(square.rect[8].right,square.rect[8].centery),8)
            return False
        elif cross[3] == 3 or ring[3] == 3:
            pygame.draw.line(screen,brown,(square.rect[0].centerx,square.rect[0].top),(square.rect[6].centerx,square.rect[6].bottom),8)
            return False
        elif cross[4] == 3 or ring[3] == 3:
            pygame.draw.line(screen,brown,(square.rect[1].centerx,square.rect[1].top),(square.rect[7].centerx,square.rect[7].bottom),8)
            return False
        elif cross[5] == 3 or ring[5] == 3:
            pygame.draw.line(screen,brown,(square.rect[2].centerx,square.rect[2].top),(square.rect[8].centerx,square.rect[8].bottom),8)
            return False
        elif cross[6] == 3 or ring[6] == 3:
            pygame.draw.line(screen,brown,(square.rect[0].left,square.rect[0].top),(square.rect[8].right,square.rect[8].bottom),10)
            return False
        elif cross[7] == 3 or ring[7] == 3:
            pygame.draw.line(screen,brown,(square.rect[2].right,square.rect[2].top),(square.rect[6].left,square.rect[6].bottom),10)
            return False
        else: return True

    def message(self,msg,color,position):
        fontStyle = pygame.font.SysFont(None,50)
        msg = fontStyle.render(msg,True,color)
        screen.blit(msg,position)
        pygame.display.update()

square = Square()
clock = pygame.time.Clock()
screenWidth, screenHeight = square.rect[8].right, square.rect[8].bottom
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Tik Tok Toe')

running = True
while running:
    screen.fill(blue)
    
    for j in range(9):
        screen.blit(square.surf[j],square.rect[j])
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_x:
                z = 1
            elif event.key == K_o:
                z = 0
        elif event.type == MOUSEBUTTONDOWN:
            mousex,mousey = pygame.mouse.get_pos()
            z,i = square.mouseClick(mousex,mousey,z)
    # for vertex in square.rect[1]:
    #     print(vertex)

    running = square.line(cross,ring)

    pygame.display.flip()
    clock.tick(5)
    
square.message("Game Over",white,(screenWidth/6,screenHeight/2.5))
time.sleep(3)
pygame.quit()
quit()

'draw line,lines circle,etc'
#     if 0 < x < screenWidth//3 and screenHeight//3*2 < y < screenHeight :
#         if pygame.mouse.get_pressed()[0]:
#             if z == 1:            
#                 # pygame.draw.lines(screen,blue,1,((100,400),(150,450),(50,450)),5) 
#                 pygame.draw.rect(screen,blue,(100,400,30,10))
#                 z = 0 ; count1 += 1                
#             else:    
#                 pygame.draw.circle(screen,blue,(100,400),20,2) 
#                 z = 1 ; count0 += 1
#     if screenWidth//3 < x < screenWidth//3*2 and screenHeight//3*2 < y < screenHeight :
#         if pygame.mouse.get_pressed()[0]:
#             if z == 1:                
#                 # pygame.draw.line(screen,blue,(250,400),(290,440),10) 
#                 pygame.draw.rect(screen,blue,(250,400,30,10))
#                 z = 0 ; count1 += 1

