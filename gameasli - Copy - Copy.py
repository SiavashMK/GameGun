import pygame,sys,time,random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

#----------------SCREEN
screen=pygame.display.set_mode((1364,716))
pygame.display.set_caption('jump')
Clock=pygame.time.Clock()
#----------------COLOR
black=(255,255,255)
red=(230,0,0)
#----------------BG IMAGE
BG=pygame.image.load('BG6.png')
heart=pygame.image.load('heart.png')
heart_rect=heart.get_rect()
heart_rect.x=650
heart_rect.y=-1000
#----------------PLAYER1
player_surface=pygame.image.load('character2.png')
player_rect=player_surface.get_rect(center=(100,600))
health_v=100
health1=pygame.image.load('health1.png')
Hx=50
Hwidth=143.5
tir=pygame.image.load('toop3.png')
tir_list = []
tir_rect = tir.get_rect()
kheshab=20
c=0
C=False
#----------------PLAYER2
player_surface2=pygame.image.load('player2.png')
player_rect2=player_surface2.get_rect(center=(1264,610))
health_v2=100
health2=pygame.image.load('health2.png')
Hx2=1170
Hwidth2=144

tir2=pygame.image.load('bullet.png')
tir_list2 = []
tir_rect2 = tir2.get_rect()
kheshab2=20
c2=0
C2=False
#-----------------SOUND BG

soundObj = pygame. mixer.music.load('Adrenaline Rock.MP3')
pygame. mixer.music.play(-1, 0.0)

soundObj2=pygame.mixer.Sound('bulletSound.wav')
soundObj2.set_volume(0.2)

soundObj3=pygame.mixer.Sound('bulletSound2.wav')
soundObj3.set_volume(0.2)

soundObj4=pygame.mixer.Sound('generic_reload.wav')
soundObj4.set_volume(10)

soundObj5=pygame.mixer.Sound('fiveseven_clipin.wav')
soundObj5.set_volume(10)

gameover=pygame.image.load('winner.png')
gameover.convert()

gameover2=pygame.image.load('winner2.png')
gameover2.convert()
#----------------Font1
game_font=pygame.font.Font(None,50)
health_num=game_font.render(str(health_v),True,black)
health_num_rect=health_num.get_rect(center=(110,60))

game_font2=pygame.font.Font(None,30)
player_num=game_font2.render('PLAYER 1',True,black)
player_num_rect=player_num.get_rect(center=(250,30))

kheshab_num=game_font2.render(str(kheshab),True,black)
kheshab_num_rect=kheshab_num.get_rect(center=(250,60))

kheshablogo=pygame.image.load('toop3.png')
kheshablogo_rect=kheshablogo.get_rect(center=(215,60))
#----------------Font2
health_num2=game_font.render(str(health_v2),True,black)
health_num_rect2=health_num2.get_rect(center=(1250,60))
health_red2=pygame.draw.rect(screen,red,((1150,540),(100,20)))
player_num2=game_font2.render('PLAYER 2',True,black)
player_num_rect2=player_num2.get_rect(center=(1110,30))

kheshab_num2=game_font2.render(str(kheshab2),True,black)
kheshab_num_rect2=kheshab_num.get_rect(center=(1110,60))

kheshablogo2=pygame.image.load('bullet.png')
kheshablogo_rect2=kheshablogo.get_rect(center=(1145,60))


game_menu=pygame.image.load('Menu2.png')
game_menu.convert()

game_guide=pygame.image.load('Guide.png')
game_guide.convert()

game_restart=pygame.image.load('restart.png')
game_restart.convert()

runing=True
active=False
run2=False
a=0
a2=0
keys=pygame.key.get_pressed()

screen.blit(BG,(0,0))
screen.blit(player_surface,player_rect)
screen.blit(player_surface2,player_rect2)
screen.blit(health_num,health_num_rect)
screen.blit(health_num2,health_num_rect2)
screen.blit(health1,(10,10))
screen.blit(health2,(1160,10))
screen.blit(player_num,player_num_rect)
screen.blit(player_num2,player_num_rect2)
health_red=pygame.draw.rect(screen,red,((Hx,23),(Hwidth,13)))
health_red2=pygame.draw.rect(screen,red,((Hx2,23),(Hwidth2,13)))
screen.blit(game_menu,(0,0))
#----------------WHILE------------------
while runing:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
#----------------ACTIVE TRUE------------            
            if event.key==pygame.K_RETURN:
                active=True
#----------------GUIDE------------------                
            elif event.key==pygame.K_RALT or event.key==pygame.K_LALT:
                screen.blit(BG,(0,0))
                screen.blit(player_surface,player_rect)
                screen.blit(player_surface2,player_rect2)
                screen.blit(health_num,health_num_rect)
                screen.blit(health_num2,health_num_rect2)
                screen.blit(health1,(10,10))
                screen.blit(health2,(1160,10))
                screen.blit(player_num,player_num_rect)
                screen.blit(player_num2,player_num_rect2)
                health_red=pygame.draw.rect(screen,red,((Hx,23),(Hwidth,13)))
                health_red2=pygame.draw.rect(screen,red,((Hx2,23),(Hwidth2,13)))
                screen.blit(game_guide,(0,0))
#-------------BACKSPACE----------                
            if event.key==8:
                screen.blit(BG,(0,0))
                screen.blit(player_surface,player_rect)
                screen.blit(player_surface2,player_rect2)
                screen.blit(health_num,health_num_rect)
                screen.blit(health_num2,health_num_rect2)
                screen.blit(health1,(10,10))
                screen.blit(health2,(1160,10))
                screen.blit(player_num,player_num_rect)
                screen.blit(player_num2,player_num_rect2)
                health_red=pygame.draw.rect(screen,red,((Hx,23),(Hwidth,13)))
                health_red2=pygame.draw.rect(screen,red,((Hx2,23),(Hwidth2,13)))
                screen.blit(game_menu,(0,0))
              
                    
    if active==True:
#movements player2 -----------------------------------   
        keys=pygame.key.get_pressed()
        if keys[pygame.K_k]:
            player_rect2.x+=2
            tir_rect2.x+=2
            if player_rect2.x>=1300:
                player_rect2.x=1300
        if keys[pygame.K_h]:
            player_rect2.x-=2
            tir_rect2.x-=2
            if player_rect2.x<=950:
                player_rect2.x=950
        if keys[pygame.K_u]:
            player_rect2.y-=10
            if player_rect2.y<=-80:
                player_rect2.y=680
        if keys[pygame.K_j]:
            player_rect2.y+=10
            if player_rect2.y>=680:
                player_rect2.y=-80        
#movements player1------------------------------------    
        if keys[pygame.K_d]:
            player_rect.x+=2
            tir_rect.x+=2
            if player_rect.x>=350:
                player_rect.x=350        
        if keys[pygame.K_a]:
            player_rect.x-=2
            tir_rect.x-=2
            if player_rect.x<=0:
                player_rect.x=0
        if keys[pygame.K_w]:
            player_rect.y-=10
            if player_rect.y<=-80:
                player_rect.y=680
        if keys[pygame.K_s]:
            player_rect.y+=10
            if player_rect.y>=680:
                player_rect.y=-80
   

    pygame.display.flip()       
#------------screen.blit---------------    
    if active==True:           
        screen.blit(BG,(0,0))
        screen.blit(player_surface,player_rect)
        screen.blit(player_surface2,player_rect2)
        screen.blit(health_num,health_num_rect)
        screen.blit(health_num2,health_num_rect2)
        screen.blit(health1,(10,10))
        screen.blit(health2,(1160,10))
        screen.blit(player_num,player_num_rect)
        screen.blit(player_num2,player_num_rect2)
        screen.blit(kheshab_num,kheshab_num_rect)
        screen.blit(kheshab_num2,kheshab_num_rect2)
        screen.blit(kheshablogo,kheshablogo_rect)
        screen.blit(kheshablogo2,kheshablogo_rect2)
        health_red=pygame.draw.rect(screen,red,((Hx,23),(Hwidth,13)))
        health_red2=pygame.draw.rect(screen,red,((Hx2,23),(Hwidth2,13)))
        heart_rect.y+=1
        if heart_rect.y>=700:
            heart_rect.y=-800
        screen.blit(heart,heart_rect)
#-----------------shoot1----------        
        b=pygame.time.get_ticks()
        
        if b-a>250:
            keys2=pygame.key.get_pressed()
            
            if keys2[pygame.K_e] and kheshab>=1:
                soundObj2.play()
                bullet_position_x = player_rect.x+70
                bullet_position_y = player_rect.y+75
                tir_rect = tir.get_rect(center = (bullet_position_x, bullet_position_y))           
                tir_list.append(tir_rect)
                kheshab-=1
                kheshab_num=game_font2.render(str(kheshab),True,black)
                if kheshab==0:
                    kheshab=0
                    kheshab_num=game_font2.render(str(kheshab),True,black)
                    C=True
                    
                a=b
        if C==True:
            c+=10
            if c==1500:
                soundObj4.play()
            if c>=3000:
                kheshab=20
                kheshab_num=game_font2.render(str(kheshab),True,black)
                c=0
                C=False
        if health_v2==(0):   #gameover2        
            screen.blit(gameover,(160,130))
            screen.blit(game_restart,(530,500))
            active=False
        for tir_rect in tir_list:
            tir_rect.x+=20
            screen.blit(tir,tir_rect)
            screen.blit(player_surface,player_rect)
#------------health2--------------        
            if tir_rect.colliderect(player_rect2):
                del tir_list[0]
                health_v2-=10
                health_num2=game_font.render(str(health_v2),True,black)
                Hx2+=15
                Hwidth2-=15
            elif tir_rect.colliderect(heart_rect):
                del tir_list[0]
                heart_rect.y=-800
                
                if health_v<=90:
                    health_v+=10
                    health_num=game_font.render(str(health_v),True,black)
                    Hwidth+=15
                else:
                    health_v=100
                    health_num=game_font.render(str(health_v),True,black)
                    Hwidth=143.5
                    
            elif tir_rect.x>1364:
                del tir_list[0]
    pygame.display.flip()
#-----------------shoot2----------
    if active==True:           
        b2=pygame.time.get_ticks()
        if b2-a2>250:
            if keys[pygame.K_y]and kheshab2>=1:
                soundObj3.play()
                bullet_position_x2 = player_rect2.x-5
                bullet_position_y2 = player_rect2.y+55
                tir_rect2 = tir2.get_rect(center = (bullet_position_x2, bullet_position_y2))            
                tir_list2.append(tir_rect2)
                kheshab2-=1
                kheshab_num2=game_font2.render(str(kheshab2),True,black)
                if kheshab2==0:
                    kheshab2=0
                    kheshab_num2=game_font2.render(str(kheshab2),True,black)
                    C2=True
                a2=b2
        if C2==True:
            c2+=10
            if c2==2000:
                soundObj5.play()
            if c2>=3000:
                kheshab2=20
                kheshab_num2=game_font2.render(str(kheshab2),True,black)
                c2=0
                C2=False
        if health_v==(0):   #gameover1 
            screen.blit(gameover2,(160,130))
            screen.blit(game_restart,(530,500))
            active=False
        for tir_rect2 in tir_list2:
            tir_rect2.x-=20
            screen.blit(tir2,tir_rect2)       
#------------health1--------------        
            if tir_rect2.colliderect(player_rect):
                del tir_list2[0]
                health_v-=10
                Hwidth-=15           
                health_num=game_font.render(str(health_v),True,black)

            elif tir_rect2.colliderect(heart_rect):
                del tir_list2[0]
                heart_rect.y=-800
                
                if health_v2<=90:
                    health_v2+=10
                    health_num2=game_font.render(str(health_v2),True,black)
                    Hwidth2+=15
                    Hx2-=15
                else:
                    health_v2=100
                    health_num2=game_font.render(str(health_v2),True,black)
                    Hwidth2=144


            
            elif tir_rect2.x<0:
                del tir_list2[0]
#-------------RESTATR---------------
    if active==False:
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                player_rect=player_surface.get_rect(center=(100,600))
                health_v=100
                Hx=50
                Hwidth=143.5
                tir_list = []
                tir_rect = tir.get_rect()
                player_rect2=player_surface2.get_rect(center=(1264,610))
                health_v2=100
                Hx2=1170
                Hwidth2=144
                tir_list2 = []
                tir_rect2 = tir2.get_rect()
                kheshab=20
                c=0
                C=False
                kheshab2=20
                c2=0
                C2=False

                health_num=game_font.render(str(health_v),True,black)
                health_num_rect=health_num.get_rect(center=(110,60))
                player_num=game_font2.render('PLAYER 1',True,black)
                player_num_rect=player_num.get_rect(center=(250,30))
                kheshab_num=game_font2.render(str(kheshab),True,black)
                health_num2=game_font.render(str(health_v2),True,black)
                health_num_rect2=health_num2.get_rect(center=(1250,60))
                health_red2=pygame.draw.rect(screen,red,((1150,540),(100,20)))
                player_num2=game_font2.render('PLAYER 2',True,black)
                player_num_rect2=player_num2.get_rect(center=(1110,30))
                kheshab_num2=game_font2.render(str(kheshab),True,black)
                heart_rect.y=-1000
                
                screen.blit(BG,(0,0))
                screen.blit(player_surface,player_rect)
                screen.blit(player_surface2,player_rect2)
                screen.blit(health_num,health_num_rect)
                screen.blit(health_num2,health_num_rect2)
                screen.blit(health1,(10,10))
                screen.blit(health2,(1160,10))
                screen.blit(player_num,player_num_rect)
                screen.blit(player_num2,player_num_rect2)
                health_red=pygame.draw.rect(screen,red,((Hx,23),(Hwidth,13)))
                health_red2=pygame.draw.rect(screen,red,((Hx2,23),(Hwidth2,13)))
                screen.blit(game_menu,(0,0))               
    pygame.display.flip()
    Clock.tick(100)
