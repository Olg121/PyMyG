import pygame
import threading
import sys
from datetime import datetime
from datetime import timedelta
from collections import deque
from time import sleep


pygame.init()
pygame.font.init()

class Menu: 
    def __init__(self, punkts = [120, 140, u'Punct', (250 , 250, 30), (128, 0, 0) , 0 ]):
        self.punkts = punkts 
    def render(self, window, font, num_punct): 
        for i in self.punkts:
            if num_punct == i[5]: 
                window.blit(font.render(i[2] , 1 , i[4]), (i[0] , i[1]))
            else :
                window.blit(font.render(i[2] , 1 , i[3]), (i[0] , i[1]))
    def menu(self): 
        done = True
        punkt = 0
        font_menu = pygame.font.Font(None, 128)
        
        while(done): 
            
            window.blit(screen, (0 , 0))
            pygame.display.flip()
            screen.fill((0 , 100, 200))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0]<i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                     punkt = i[5]
                self.render(screen, font_menu, punkt)
                  
            for e in pygame.event.get(): 
                if(e.type == pygame.QUIT): 
                    sys.EXIT(0);
                if(e.type == pygame.KEYDOWN):
                    if(e.key == pygame.K_ESCAPE):
                        sys.exit()
                    if(e.key == pygame.K_UP):
                        if(punkt > 0):
                            punkt -= 1
                    if(e.key == pygame.K_DOWN):
                        if(punkt < len(self.punkts) - 1):
                            punkt += 1
                if(e.type == pygame.MOUSEBUTTONDOWN and e.button == 1):
                    if(punkt == 0):
                        done = False
                    elif(punkt == 1):
                        sys.exit()



window = pygame.display.set_mode((504,504))
screen = pygame.Surface((504, 504))
font = pygame.font.Font(None, 200)
  

class Pair():
    time = datetime.now()
    i = int

P = [(120, 120, u'Game' , (250 , 250 , 30), (250 , 30 , 250), 0),
      (150, 250, u'Quit' , (250 , 250 , 30), (250 , 30 , 250), 1)]
menu = Menu(P)
menu.menu()       
def main():
    
    start()



    
class sprite:
    def __init__(self, xpos, ypos, fileName):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(fileName)
        self.bitmap.set_colorkey((0 , 0 , 0))
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
          
class Field:
    def __init__(self):
        
        self.warning = pygame.image.load("s1.jpg") 
        self.danger = pygame.image.load("s2.jpg")
        self.field = []
        self.temp = 1
        self.condition = []
        self.listX = []
        self.listY = []
        for i in range(2 , 502 , 50):
            for j in range(2, 502, 50):
                 self.field.append(  sprite(i,j,"s.jpg" ) )
                 self.condition.append(self.temp)
                 self.listX.append(i)
                 self.listY.append(j)
    def getField(self):
        return self.field

    def getCondition(self):
        return self.condition

    def render(self):
        i = 0        
        while i < len(self.field):
            temp = self.field[i] 
            self.field[i].render()
            i += 1


    def changeSpriteToWarning(self, i):
         x = self.listX[i]
         y = self.listY[i]
         self.field[i] = sprite(x , y ,"s1.jpg")

    def changeSpriteToDanger(self, i):
         x = self.listX[i]
         y = self.listY[i]
         self.field[i] = sprite(x , y ,"s2.jpg")

    def changeConditionTo2(self, i):
         self.condition[i] = 2
        

    def changeConditionTo3(self,i):
         self.condition[i] = 3
  


def move(player1, y , x):
     if(player1.x + x > 0 and player1.x + x < 475 and player1.y + y > 0 and player1.y + y < 475):
           player1.x += x
           player1.y += y

def start():
    pygame.display.set_caption("MyGame")
    
    sq = sprite(20 , 20, "s.jpg")
    sq.render()
    A = Field()
    font = pygame.font.Font(None, 25)
    Player1 = sprite(5 , 5, "player1.png")
    Player2 = sprite(470 , 470, "player2.png")
    Run = True
    pygame.key.set_repeat(1 , 1)
    P1MoveUp = False
    P1MoveDown = False
    P1MoveLeft = False
    P1MoveRigth = False
    P2MoveUp = False
    P2MoveDown = False
    P2MoveLeft = False
    P2MoveRigth = False
    Q = [] 
    win = 0
    while Run:
         curCondition = A.getCondition()

    
         I = int(Player1.x / 50) * 10+ (int(Player1.y / 50))
         if(curCondition[I] == 1):
            A.changeConditionTo2(I) 
            A.changeSpriteToWarning(I)
            Q.append((I , datetime.now()))
         elif(curCondition[I] == 3):
            Run = False 
            win = 1
            break; 
         I = int(Player2.x / 50) * 10+ (int(Player2.y / 50))
         if(curCondition[I] == 1):
            A.changeConditionTo2(I) 
            A.changeSpriteToWarning(I)
            Q.append((I , datetime.now()))
         elif(curCondition[I] == 3):
            Run = False
            win = 2
            break; 
         J = int(Player1.x / 50) * 10+ (int(Player1.y / 50))
         if curCondition[I] == 3 and curCondition[J] == 3:
            win = 0
   

        

         if(len(Q) > 0):
             if((datetime.now() - Q[0][1]).total_seconds() > 3): 
                 A.changeConditionTo3(Q[0][0])
                 A.changeSpriteToDanger(Q[0][0])
                 Q.pop(0)
         for e in pygame.event.get():
             if e.type == pygame.QUIT:
                   Run = False
             if e.type == pygame.KEYDOWN:
                 if e.key == pygame.K_d:
                     P1MoveLeft = False
                     P1MoveRigth = True
                 if e.key == pygame.K_a:
                     P1MoveLeft = True
                     P1MoveRigth = False
                 if e.key == pygame.K_w:
                     P1MoveDown = False
                     P1MoveUp = True
                 if e.key == pygame.K_s:
                     P1MoveUp = False
                     P1MoveDown = True
                 if e.key == pygame.K_LEFT:
                     P2MoveLeft = True
                     P2MoveRigth = False
                 if e.key == pygame.K_RIGHT:
                     P2MoveLeft = False
                     P2MoveRigth = True
                 if e.key == pygame.K_UP:
                     P2MoveDown = False
                     P2MoveUp = True
                 if e.key == pygame.K_DOWN:
                     P2MoveUp = False
                     P2MoveDown = True
            
            
             if e.type == pygame.KEYUP:
                 if e.key == pygame.K_d:
                     P1MoveRigth = False
                 if e.key == pygame.K_w:
                     P1MoveUp = False
                 if e.key == pygame.K_s:
                     P1MoveDown = False
                 if e.key == pygame.K_a:
                     P1MoveLeft = False
            
                 if e.key == pygame.K_LEFT:
                     P2MoveLeft = False
                 if e.key == pygame.K_RIGHT:
                     P2MoveRigth = False
                 if e.key == pygame.K_DOWN:
                     P2MoveDown = False
                 if e.key == pygame.K_UP:
                     P2MoveUp = False
  
       
                 
         if P1MoveRigth:
             move(Player1 , 0 , 3)
    
         if P1MoveLeft:
             move(Player1,  0 , -3)
     
         if P1MoveDown:
             move(Player1,  3 ,  0) 
       
         if P1MoveUp: 
             move(Player1, -3 ,  0) 

         if P2MoveRigth:
             move(Player2 , 0 , 3)
    
         if P2MoveLeft:
             move(Player2,  0 , -3)
     
         if P2MoveDown:
             move(Player2,  3 ,  0) 
       
         if P2MoveUp: 
             move(Player2, -3 ,  0) 


         window.blit(screen, (0, 0))
         pygame.display.flip()
         A.render()
         Player1.render()
         Player2.render()
    if(win == 2):
        sans = "First player win" 
    else: 
        sans = "Second player win"
    
        
    while(True):
        screen.fill([255, 255, 255]); 
        pygame.display.flip()
        text = font.render(sans, True, [0 , 0 , 0])
        screen.blit(text, [170, 250] )
        window.blit(screen, (0 , 0) )        

main()