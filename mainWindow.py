#import module
import pygame
import random
import os

#initialize the game
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont(None, 55)
clock =pygame.time.Clock()


#Initializing the color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)


#Game Window
screen_height=900
screen_width=600
gameWindow=pygame.display.set_mode((screen_height,screen_width))
#Game specific variable

def text_screen(text, color, x, y):#function for print score on screen
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color, [x, y, snake_size, snake_size])

pygame.mixer.music.fadeout(200)
pygame.mixer.music.load('wc.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)

def main():
    pygame.mixer.music.fadeout(200)
    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play(100)
    pygame.mixer.music.set_volume(.6)

def back():
    pygame.mixer.music.fadeout(200)
    pygame.mixer.music.load('over.mp3')
    pygame.mixer.music.play(100)
    pygame.mixer.music.set_volume(.6)


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        bgimg = pygame.image.load("front.jpg")
        bgimg = pygame.transform.scale(bgimg, (900, 600)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))
        text_screen("Welcome to Snakes",Black, 260, 250)
        text_screen("Press Space Bar To Play",Black , 232, 290)
        text_screen("Created by Vishal Singh...", Red, 400, 545)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    game_loop()
        pygame.display.update()
        clock.tick(60)

    
def game_loop():#Game loop
    exit_game=False
    game_over=False
    snake_x=45#Direction of snake in x-direction
    snake_y=30#Direction of snake in x-direction
    Velocity_x=0#for giving velocity in x- direction
    Velocity_y=0#for giving velocity in y-direction
    snk_length =1
    snk_list =[]
    # for random position of food
    food_x=random.randint(20, screen_width/2)
    food_y=random.randint(20, screen_height/2)
    food_size=10
    snake_size=20
    fps=40
    init_velocity=5
    score=0
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")
    with open("high_score.txt","r") as f:
        high_score= f.read()
    pygame.display.update()
    pygame.display.set_caption("SnakegamewithVishal")
    while not exit_game:
        if game_over:
            gameWindow.fill(White)
            bgimg = pygame.image.load("back.jpg")
            bgimg = pygame.transform.scale(bgimg, (screen_height, screen_width)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Game Is Over : For Continue Press Enter",Red,screen_width/5,screen_height/4)
            text_screen("your Score: "+str(score),Red,screen_width/2,screen_height/3)
            with open("high_score.txt","w") as f:
                f.write(str(high_score))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        back()
                        welcome()          
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:#For movement of keys
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            Velocity_x=init_velocity
                            Velocity_y=0
                        if event.key == pygame.K_LEFT:
                            Velocity_x=-init_velocity
                            Velocity_y=0
                        if event.key == pygame.K_UP:
                            Velocity_x=0
                            Velocity_y=-init_velocity
                        if event.key == pygame.K_DOWN:
                            Velocity_x=0
                            Velocity_y=init_velocity
            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15: # Add score and replot food
                score+=10                       
                food_x=random.randint(20, screen_width/2)
                food_y=random.randint(20, screen_height/2)
                snk_length+=5
            snake_x=snake_x+Velocity_x
            snake_y=snake_y+Velocity_y
            gameWindow.fill(White)
            bgimg = pygame.image.load("main.jpg")
            bgimg = pygame.transform.scale(bgimg, (screen_height, screen_width)).convert_alpha()    
            gameWindow.blit(bgimg, (0, 0))
            if score>int(high_score):
                high_score=score
            text_screen("Score: " + str(score)  +" High Score="+str(high_score), Red, 5, 5)#for print the score on screen
            pygame.draw.rect(gameWindow,Red,[food_x,food_y,food_size,food_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:#For snake collsion
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over=True
                back()
                bgimg = pygame.image.load("back.jpg")
                bgimg = pygame.transform.scale(bgimg, (screen_height, screen_width)).convert_alpha()
                gameWindow.blit(bgimg, (0, 0))
            if snake_x<0 or snake_x>screen_height or snake_y<0 or snake_y>screen_width:
                game_over=True
                back()
                bgimg = pygame.image.load("back.jpg")
                bgimg = pygame.transform.scale(bgimg, (screen_height, screen_width)).convert_alpha()
                gameWindow.blit(bgimg, (0, 0))
            plot_snake(gameWindow, Black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
