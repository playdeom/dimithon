import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)
field=[
    [-1,-1,-1], # 1,2,3
    [-1,-1,-1], # 4,5,6
    [-1,-1,-1]  # 7,8,9
]
field_locate=[
    [[100,100],[100,300],[100,500]],
    [[300,100],[300,300],[300,500]],
    [[500,100],[500,300],[500,500]]
]
def where(x,y):
    if x<200:
        if y<200:
            return [0,0]
        elif y<400:
            return [0,1]
        else:
            return [0,2]
    elif x<400:
        if y<200:
            return [1,0]
        elif y<400:
            return [1,1]
        else:
            return [1,2]
    else:
        if y<200:
            return [2,0]
        elif y<400:
            return [2,1]
        else:
            return [2,2]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            #left click
            x,y=pygame.mouse.get_pos()
            cx,cy=where(x,y)
            field[cx][cy]=0
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==3:
            x,y=pygame.mouse.get_pos()
            cx,cy=where(x,y)
            field[cx][cy]=1
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==2:
            x,y=pygame.mouse.get_pos()
            cx,cy=where(x,y)
            field[cx][cy]=-1
    font=pygame.font.Font(None,100)
    screen.fill("white")
    for i in range(200,601,200):
        pygame.draw.line(screen,black,[i,0],[i,600],5)
        pygame.draw.line(screen,black,[0,i],[600,i],5)
    for i in range(3):
        for j in range(3):
            if field[i][j]==0:
                pygame.draw.circle(screen,blue,field_locate[i][j],50)
            if field[i][j]==1:
                pygame.draw.circle(screen,red,field_locate[i][j],50)
    who_win=-1
    for i in range(3):
        if field[i]==[0,0,0]:
            who_win=0
            break
        if field[i]==[1,1,1]:
            who_win=1
            break
    for i in range(3):#가로
        arr=[]
        for j in range(3):
            arr.append(field[j][i])
        if arr==[0,0,0]:
            who_win=0
            break
        if arr==[1,1,1]:
            who_win=1
            break
    arr=[]
    arr2=[]
    for i in range(3):
        arr.append(field[i][i])
        arr2.append(field[i][2-i])
    if [0,0,0]==arr or [0,0,0]==arr2:
        who_win=0
    if [1,1,1]==arr or [1,1,1]==arr2:
        who_win=1
    if who_win!=-1:
        out=font.render("Blue win!" if not who_win else "Red win!",True,blue if not who_win else red)
        out_make=out.get_rect()
        out_make.centerx=300
        out_make.centery=300
        screen.fill("black")
        screen.blit(out,out_make)
        running=False
        pygame.display.update()
        pygame.time.delay(3000)
    pygame.display.update()
    clock.tick(60)
pygame.quit()