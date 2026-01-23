import pygame as pg
import random
import time

pg.init()
pause=pg.image.load('/Users/User/моя программа/pause.png')
retry=pg.image.load('/Users/User/моя программа/retry.png')
window_width=1500
window_height=900
screen=pg.display.set_mode([window_width,window_height])
pg.display.set_caption('кружочек')

a=255
b=255
c=255

c_speed=1

pl_speed=1

a01=0
a02=0

l='0'
l1='0'

x_c=740
y_c=470

x=50
y=360
x1=1440
y1=360

font=pg.font.Font('/Users/User/моя программа/static/Roboto-BlackItalic.ttf',43)
t=font.render('ПЕРВЫЙ ИГРОК ПОБЕДИЛ !', True, 'RED')
t_1=font.render('ВТОРОЙ ИГРОК ПОБЕДИЛ !', True, 'RED')
t_2=font.render('0', True, 'RED')
t_3=font.render('0', True, 'RED')

pause_rect=pause.get_rect(topleft=(0,0))
retry_rect=retry.get_rect(topleft=(710,600))
running=True

a1=random.randint(0,1)
a2=random.randint(0,1)

while running:

    circle=pg.draw.circle(screen,'RED',(x_c,y_c),10,2)
    player1=pg.draw.rect(screen,(a,b,c),(x,y,10,150))
    player2=pg.draw.rect(screen,(a,b,c),(x1,y1,10,150)) 

    screen.blit(pause,(0,0))
    screen.blit(t_2,(680,10))
    screen.blit(t_3,(770,10))

    pg.display.update()




    keys=pg.key.get_pressed()
    if keys[pg.K_w] and y!=0:
        y-=pl_speed
    if keys[pg.K_s] and y!=750:
        y+=pl_speed
    if keys[pg.K_UP] and y1!=0:
        y1-=pl_speed
    if keys[pg.K_DOWN] and y1!=750:
        y1+=pl_speed


    if a1==1:
        x_c+=c_speed
    else:
        x_c-=c_speed
    if a2==1:
        if y_c>890:
            a2=0
        else:
            y_c+=c_speed
    else:
        if y_c<10:
            a2=1
        else:
            y_c-=c_speed


    if x_c==x+20 and y_c>y and y_c<y+150:
        a1=1
        a6=random.randint(1,5)
        if a6==1:
            c_speed=1
        else:
            c_speed=2
    if x_c==x1-10 and y_c>y1 and y_c<y1+150:
        a1=0


                                   #Цвет можно менять
    a-=1                        #R
    b-=1                        #G
    c-=1                        #B
    if a==0 or b==0 or c==0:
        a=255
        b=255
        c=255
    
    screen.fill((0,0,0))  
    
    
    if x_c+10>=1500 :
        a01+=1
        x_c=730
        y_c=460
        a1=random.randint(0,1)
        a2=random.randint(0,1)
        c_speed=1
        l=str(1+int(l))


    if x_c-10<=0 :
        a02+=1
        x_c=740
        y_c=470
        a1=random.randint(0,1)
        a2=random.randint(0,1)
        c_speed=1
        l1=str(1+int(l1))


    
    if a01==5 :
        screen.blit(t,(490,450))
        c_speed=0
        pl_speed=0
        screen.blit(retry,(710,600))
    if a02==5 :
        screen.blit(t_1,(490,450))
        c_speed=0
        pl_speed=0
        screen.blit(retry,(710,600))
    for event in pg.event.get():
        '''if event.type==pg.MOUSEBUTTONDOWN:'''

        if event.type==pg.QUIT:
            running=False
    t_2=font.render(l, True, 'RED')
    t_3=font.render(l1, True, 'RED')

pg.quit()