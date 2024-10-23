import pygame
import math
import random

pygame.init()
pygame.font.init()

window=pygame.display.set_mode((400,400))
pygame.display.set_caption('snake')
window.fill((0, 0, 0))

font1 = pygame.font.SysFont('Comic Sans MS', 50)
gmover = font1.render('GAME OVER', False, (255, 0, 0))
font2 = pygame.font.SysFont('Comic Sans MS', 19)
restart = font2.render('RESTART', False, (255, 0, 0))
quit = font2.render('QUIT', False, (255, 0, 0))

btnimg = pygame.image.load('button.png').convert_alpha()


pos = pygame.mouse.get_pos()



#GAME VARS
v0 = 100
px = [91, 97, 103, 109, 115, 121]
py = [200, 200, 200, 200, 200, 200]
s=6
dir='r'
def dotDraw (x, y):
    return(pygame.draw.circle(window, (255, 255, 255), (x, y), 3, 3))

vlist = [110]
for e in range(1000):
    vlist.append(vlist[-1]-5)

bylist = [50]
for b in range(1000):
    bylist.append(50)

gapposlist = [0]
for c in range(1000):
    gapposlist.append(random.randint(-140, 140))

gaplist = [100]
for d in range(1000):
    gaplist.append(gaplist[-1]-5)
    if gaplist[-1]<0:
        break

N = 0 #STAGE NUMBER
    
#CLASSES
class Button():
    def __init__(self, x, y, text, scale, dx, dy):
        width = btnimg.get_width()
        height = btnimg.get_height()
        self.img = pygame.transform.scale(btnimg, (int(width*scale), int(height*scale/1.15)))
        self.rect = self.img.get_rect()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.text = text
    def draw(self):
        #pos = pygame.mouse.get_pos()
        #print(pos)
        #if self.rect.collidepoint(pos):
        #    print('HOVER')

        window.blit(self.img, (self.x, self.y))
        window.blit(self.text, (self.x+10+self.dx, self.y+10+self.dy))
qbutton = Button(80, 230, quit, 0.25, 16, 0)
rbutton = Button(210, 230, restart, 0.25, 0, 0)


#INITIAL DRAW
pygame.draw.rect(window, (255, 255, 255), (50, 50, 300, 300), 2)
pygame.display.update()


#CLOCK OBJ
t=-1


#MAIN GAME LOOP
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                dir='r'
            elif event.key == pygame.K_LEFT:
                dir='l'
            elif event.key == pygame.K_UP:
                dir='u'
            elif event.key == pygame.K_DOWN:
                dir='d'



    #BOUNDARIES
    for i in range(len(px)):
        if px[i]<=50 or px[i]>=350 or py[i]<=50 or py[i]>=350:
            run=False



    #CLOCK
    t+=1



    #UPDATE COORDINATES
    if dir=='r':
        px.append(px[-1]+6)
        px.pop(0)
    elif dir=='l':
        px.append(px[-1]-6)
        px.pop(0)
    elif dir=='u':
        py.append(py[-1]-6)
        py.pop(0)
    elif dir=='d':
        py.append(py[-1]+6)
        py.pop(0)



    #UPDATE DRAW
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), (50, 50, 300, 300), 2)
    for i in range(len(px)):
        dotDraw(px[i], py[i])



    if t>=5:
        N = math.floor((t-5)/60)
        gappos = gapposlist[N]
        gap0 = gaplist[N]
        print(t)
        if bylist[N]<=350:
            pygame.draw.line(window, (0, 128, 0), (50, bylist[N]), (50+(300-gap0)/2+gappos, bylist[N]), 2)
            pygame.draw.line(window, (0, 128, 0), (50+(300+gap0)/2+gappos, bylist[N]), (350, bylist[N]), 2)
            bylist[N]+=5


    #CHECK FOR COLLISION
        for k in range(len(px)):
            if px[k] <= 50+(300-gap0)/2+gappos or px[k] >= 50+(300+gap0)/2+gappos:
                if py[k] <= bylist[N]+3 and py[k] >= bylist[N]-3 :
                    game_over=True


    pygame.display.update()
    N = math.floor((t-5)/60)
    pygame.time.delay(vlist[N])


while game_over:
    #GAME OVER

    window.fill((0, 0, 0))



    #WRITE
    qbutton.draw()
    rbutton.draw()
    window.blit(gmover, (55, 80))
    print(pos)

    

    pygame.display.update()