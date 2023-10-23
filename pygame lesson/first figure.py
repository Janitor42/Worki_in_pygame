import pygame

width=500
height=500
FPS=30

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Game")
screen.fill((0, 55, 0))

square=pygame.Surface((50,50))#создание квадрата (для создания используется surface(экран на котором рисуется)
square.fill('blue')# выбор цвета


player= pygame.image.load('folder/name.png')#загрузка изображения сохранение в переменную

myfont=pygame.font.Font(None,48) #Текст
text_surfase=myfont.render('hello',True,'red')




running = True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    screen.blit(square,(100,50))#(отрисовка квадрата в режиме игры (blit принимает 2 параметра (1 кого отрисоввывать,2 где отрисовывать))

    pygame.draw.circle(screen,'orange',(50,50),15)# круг все параметры указаны в методе можно рисовать в квадрате или
    #в другом обьекте
    screen.blit(text_surfase,(200,200))





    pygame.display.flip()
pygame.quit()