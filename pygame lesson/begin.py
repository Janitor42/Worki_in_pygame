import pygame

width=500
height=500
FPS=30

pygame.init() # — это команда, которая запускает pygame
screen = pygame.display.set_mode((width,height)) # -окно программы, которое создается, когда мы задаем его размер в настройках
pygame.display.set_caption("My Game")
screen.fill((0, 55, 0))  # - выбор цвета отрисовки экрана
clock = pygame.time.Clock() # ФПС

running = True
while running:
    #Постоянное событие закрытия окна по крестику
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    clock.tick(FPS)# контроль кадров

    pygame.display.flip() # - автообновление экрана (двойная буферезация экрана) Пишеться всегда в конце

pygame.quit()