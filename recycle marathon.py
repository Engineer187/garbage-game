import pygame 
import random
WIDTH=800
HIGHT=800
TITLE="recycle marathon"
screen=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption(TITLE)
pen=pygame.image.load("images\\pen.png")
paper_bag=pygame.image.load("images\\paper bag.png")
crate=pygame.image.load("images\\crate.png")
chips=pygame.image.load("images\\chipsimg.png")
bottle=pygame.image.load("images\\bottleimg.png")
battery=pygame.image.load("images\\batteryimg.png")
bag=pygame.image.load("images\\bag.png")
bin_pic=pygame.image.load("images\\bin.png")
bg=pygame.image.load("images\\bg2.png")
num=random.randint(1,2)
Recycle_list=[pen,paper_bag,crate]
no_recycle_list=[bottle,chips,battery,bag]

class Bin(pygame.sprite.Sprite):
    def __init__ (self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Recycle(pygame.sprite.Sprite):
    def __init__ (self,image,x,y):
        super().__init__()
        self.image=image
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Non_recycle(pygame.sprite.Sprite):
    def __init__ (self,image,x,y):
        super().__init__()
        self.image=image
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
bin_groop=pygame.sprite.Group()
Recycle_=pygame.sprite.Group()
Non_recycle_=pygame.sprite.Group()
bin=Bin(bin_pic,0,0)
bin_groop.add(bin)
for i in range(20):
    x=random.randint(1,800)
    y=random.randint(1,800)
    item=random.choice(Recycle_list)
    item=Recycle(item,x,y)
    Recycle_.add(item)
for i in range(30):
    x=random.randint(1,800)
    y=random.randint(1,800)
    item=random.choice(no_recycle_list)
    item=Non_recycle(item,x,y)
    Non_recycle_.add(item)
RUN=True
while RUN == True :
    screen.blit(bg,(0,0))
    Recycle_.draw(screen)
    Non_recycle_.draw(screen)
    bin_groop.draw(screen)
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            RUN = False




    pygame.display.update()