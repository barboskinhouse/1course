
import pygame
import random

def mainpage():
    #Фон главного меню
    bg = pygame.image.load('background.png')
    bg = pygame.transform.scale(bg,(width,height))
    screen.blit(bg,(0,0))
    #Зайчик 1
    bunny = pygame.image.load('bunny.png')
    bunny = pygame.transform.scale(bunny,(300,height-100))
    screen.blit(bunny,(50,50))
    #Кнопка выхода
    exit_button = pygame.image.load('exitbutton.png')
    screen.blit(exit_button,(1100,0))
    #Начало игры
    game_button = pygame.image.load('gamebutton.png')
    game_button = pygame.transform.scale(game_button,(game_button.get_width()-100,game_button.get_height()-100))
    screen.blit(game_button,(500,100))
    #Правила игры
    rules_button = pygame.image.load('rulesbutton.png')
    rules_button = pygame.transform.scale(rules_button,(rules_button.get_width()-100,rules_button.get_height()-100))
    screen.blit(rules_button,(500,250))
    #Разработчики
    dev_button = pygame.image.load('devbutton.png')
    dev_button = pygame.transform.scale(dev_button,(dev_button.get_width()-100,dev_button.get_height()-100))
    screen.blit(dev_button,(500,400))

    pygame.display.update()
    
    return exit_button, game_button, rules_button, dev_button

def devpage():
    #Фон разработки
    bg = pygame.image.load('background.png')
    bg = pygame.transform.scale(bg,(width,height))
    screen.blit(bg,(0,0))
    #Зайчик 2
    bunnydev = pygame.image.load('bunnydev.png')
    screen.blit(bunnydev,(50,50))
    #Информация
    inform = pygame.image.load('devtab.png')
    screen.blit(inform,(500,100))
    pygame.display.update()

def rulespage1():
    #Фон разработки
    bg = pygame.image.load('background.png')
    bg = pygame.transform.scale(bg,(width,height))
    screen.blit(bg,(0,0))
    #Табличка с правилами
    rules = pygame.image.load('rules1tab.png')
    rules = pygame.transform.scale(rules,(width,height))
    screen.blit(rules,(0,0))
    #Кнопка возвращения в главное меню
    back_button = pygame.image.load('backbutton.png')
    screen.blit(back_button,(0,0))
    pygame.display.update()

def rulespage2():
    #Фон разработки
    bg = pygame.image.load('background.png')
    bg = pygame.transform.scale(bg,(width,height))
    screen.blit(bg,(0,0))
    #Табличка с правилами
    rules = pygame.image.load('rules2tab.png')
    screen.blit(rules,(0,0))
    #Кнопка возвращения в главное меню
    back_button = pygame.image.load('backbutton.png')
    screen.blit(back_button,(0,0))
    pygame.display.update()

def back_button(mainmenu, page): 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    bk = pygame.image.load('backbutton.png')
    screen.blit(bk,(0,0))
    pygame.display.update()
    if 90 < mouse[0] < 160 and 35 < mouse[1] < 120:
        if click[0] == 1:
            s = pygame.mixer.Sound('change.ogg')
            s.play()
            mainpage()
            mainmenu = 1
            page = 0
    return mainmenu, page

#Игра и её алгоритм
def game_design():
    #Фон разработки
    bg = pygame.image.load('background_game.png')
    screen.blit(bg,(0,0))
    bunny_robot = pygame.image.load('bunny_robot.png')
    screen.blit(bunny_robot,(0,0))
    #Кнопки
    stone_button = pygame.image.load('stone_2.png')
    screen.blit(stone_button,(0,0))
    sciccors_button = pygame.image.load('scissors_2.png')
    screen.blit(sciccors_button,(0,0))
    paper_button = pygame.image.load('paper_2.png')
    screen.blit(paper_button,(0,0))

    pygame.display.update()

        
#создание игрового окна
width = 1280
height = 720

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
screen = pygame.display.set_mode((width,height)) #окно
pygame.display.set_caption("Кролик против робота")



menu = mainpage()
exit_button = menu[0]
game_button = menu[1]
rules_button = menu[2]
dev_button = menu[3]

pygame.mixer.music.load('game.mp3')
pygame.mixer.music.play(loops = -1, start = 0.0, fade_ms = 300)

#Переключатели для кнопок
mainmenu = 1
game = 0
res = 0
rules1 = 0
rules2 = 0
dev = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif mainmenu == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 1160 < event.pos[0] < 1160+exit_button.get_width() and 55 < event.pos[1] < 55+exit_button.get_height()-120:
                        if mainmenu == 1:
                            s = pygame.mixer.Sound('end.ogg')
                            s.play()
                            running = False
                            pygame.quit()
                    elif 500 < event.pos[0] < 500+game_button.get_width():
                        if 230 < event.pos[1] < 360:
                            s = pygame.mixer.Sound('change.ogg')
                            s.play()
                            game_design()
                            mainmenu = 0
                            game = 1
                        elif 390 < event.pos[1] < 510:
                            s = pygame.mixer.Sound('change.ogg')
                            s.play()
                            rulespage1()
                            mainmenu = 0
                            rules1 = 1
                        elif 540 < event.pos[1] < 660:
                            s = pygame.mixer.Sound('change.ogg')
                            s.play()
                            devpage()
                            mainmenu = 0
                            dev = 1
                            
        elif dev == 1:
            mainmenu, dev = back_button(mainmenu, dev)
            
        elif rules1 == 1:
            mainmenu, rules1 = back_button(mainmenu, rules1)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    if 685 < event.pos[0] < 739 and 510 < event.pos[1] < 550:
                        s = pygame.mixer.Sound('change.ogg')
                        s.play()
                        rulespage2()
                        rules1 = 0
                        rules2 = 1
                        
        elif rules2 == 1:
            mainmenu, rules2 = back_button(mainmenu, rules2)
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    if 540 < event.pos[0] < 590 and 510 < event.pos[1] < 550:
                        s = pygame.mixer.Sound('change.ogg')
                        s.play()
                        rulespage1()
                        rules2 = 0
                        rules1 = 1
                        
        elif game == 1:
            mainmenu, game = back_button(mainmenu, game)
            
            bunny_change = 'None'
            change = ['stone','scissors','paper']
            robot_change = change[random.randint(0, len(change)-1)]
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1:
                    if 429 < event.pos[0] < 555 and 241 < event.pos[1] < 368:
                        s = pygame.mixer.Sound('change.ogg')
                        s.play()
                        bunny_change = change[0]
                        game = 0
                        res = 1                        
                    elif 405 < event.pos[0] < 710 and 416 < event.pos[1] < 505:
                        s = pygame.mixer.Sound('change.ogg')
                        s.play()
                        bunny_change = change[1]
                        game = 0
                        res = 1
                    elif 405 < event.pos[0] < 700 and 560 < event.pos[1] < 615:
                        s = pygame.mixer.Sound('change.ogg')
                        s.play()
                        bunny_change = change[2]
                        game = 0
                        res = 1
                        
        elif res == 1:
            pygame.mixer.music.pause()
            if bunny_change == robot_change:
                #Ничья
                tab = pygame.image.load('draw.png')
                screen.blit(tab,(0,0))
                s = pygame.mixer.Sound('lose.ogg')
                s.play()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1:
                        if 800 < event.pos[0] < 900 and 100 < event.pos[1] < 180:
                            s = pygame.mixer.Sound('change.ogg')
                            s.play()
                            pygame.mixer.music.unpause()
                            mainpage()
                            mainmenu = 1
                            res = 0                
            elif (bunny_change == change[0] and robot_change == change[2]) \
                 or (bunny_change == change[1] and robot_change == change[0]) \
                 or (bunny_change == change[2] and robot_change == change[1]):
                #Проигрыш
                tab = pygame.image.load('lose.png')
                screen.blit(tab,(0,0))
                s = pygame.mixer.Sound('lose.ogg')
                s.play()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1:
                        if 800 < event.pos[0] < 900 and 100 < event.pos[1] < 180:
                            s = pygame.mixer.Sound('change.ogg')
                            s.play()
                            pygame.mixer.music.unpause()
                            mainpage()
                            mainmenu = 1
                            res = 0                
            else:
                #Победа
                tab = pygame.image.load('win.png')
                screen.blit(tab,(0,0))
                s = pygame.mixer.Sound('win.ogg')
                s.play()
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1:
                        if 800 < event.pos[0] < 900 and 100 < event.pos[1] < 180:
                            s = pygame.mixer.Sound('change.ogg')
                            s.play()
                            pygame.mixer.music.unpause()
                            mainpage()
                            mainmenu = 1
                            res = 0
            pygame.display.update()
            
                
