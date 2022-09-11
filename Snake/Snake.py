

#Importing The Modules
import pygame
import random
import os
import sys
#Initialization
pygame.mixer.init()
pygame.init()


#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
american_rose= (255,3,62)
amber = (255,191,0)
azure = (0,127,255)
snakegreen = (35, 45, 40)

#Game Backgrounds
bg1 = pygame.image.load("Screen/gamebag/bg.jpg")
bg2 = pygame.image.load("Screen/gamebag/bg2.jpg")
bg3 = pygame.image.load("Screen/gamebag/bg3.jpg")
intro = pygame.image.load("Screen/intro1S.png")
outro = pygame.image.load("Screen/outro.png")
outro1 = outro = pygame.image.load("Screen/outro.png")
#Creating The window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("Snake By Siddhant")
pygame.display.update()

#Music
pygame.mixer.music.load('music/wc.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.6)

#Variables For The Game
clock = pygame.time.Clock()
font = pygame.font.SysFont('Harrington', 35)

def text_screen(text, color, x, y):
   screen_text = font.render(text, True, color)
   gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
   for x,y in snk_list:
       pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


#Welcome Screen

def welcome():
    exit_game = False
    while not exit_game:
        initv = random.choice([3,4,5])
        mbg = random.choice([bg1,bg2,bg3])
        gameWindow.blit(intro, (0,0))
        text_screen("Theme - Technology & Toys",american_rose,300,150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.fadeout(200)
                    pygame.mixer.music.load('music/bgm.mp3')
                    pygame.mixer.music.play(100)
                    pygame.mixer.music.set_volume(.6)
                    gameloop(initv,mbg)
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop(init_velocity,mbg):

# Game specific variables
   exit_game = False
   game_over = False
   snake_x = 45
   snake_y = 55
   velocity_x = 0
   velocity_y = 0
   snk_list = []
   snk_length = 1

#Highscore Build
   if(not os.path.exists("DATA/highscore.txt")):
       with open("DATA/highscore.txt", "w") as f:
           f.write("0")
   with open("DATA/highscore.txt", "r") as f:
            highscore = f.read()

#Food
   food_x = random.randint(20, screen_width / 2)
   food_y = random.randint(20, screen_height / 2)

#Game Variables
   score = 0
   # print(init_velocity)
   snake_size = 30
   fps = 60
   while not exit_game:
       if game_over:
           with open("DATA/highscore.txt", "w") as f:
               f.write(str(highscore))

#GameOverScreen

           gameWindow.blit(outro, (0, 0))
           text_screen("Score: " + str(score ), snakegreen, 385, 350)
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit_game = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       welcome()
       else:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit_game = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RIGHT:
                       velocity_x = init_velocity
                       velocity_y = 0
                   if event.key == pygame.K_LEFT:
                       velocity_x = - init_velocity
                       velocity_y = 0
                   if event.key == pygame.K_UP:
                       velocity_y = - init_velocity
                       velocity_x = 0
                   if event.key == pygame.K_DOWN:
                       velocity_y = init_velocity
                       velocity_x = 0
                   if event.key == pygame.K_q:
                        score +=10
           snake_x = snake_x + velocity_x
           snake_y = snake_y + velocity_y
           if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
               score +=10
               food_x = random.randint(20, screen_width / 2)
               food_y = random.randint(20, screen_height / 2)
               snk_length +=5
               if score>int(highscore):
                   highscore = score
           gameWindow.blit(mbg, (0, 0))
           text_screen("Score: " + str(score) + "  Highscore: "+str(highscore),  snakegreen, 5, 5)
           pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
           head = []
           head.append(snake_x)
           head.append(snake_y)
           snk_list.append(head)


           if len(snk_list)>snk_length:
               del snk_list[0]
           if head in snk_list[:-1]:
               game_over = True
               pygame.mixer.music.load('music/bgm1.mp3')
               pygame.mixer.music.play(100)
               pygame.mixer.music.set_volume(.6)
           if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
               game_over = True
               pygame.mixer.music.load('music/bgm2.mp3')
               pygame.mixer.music.play(100)
               pygame.mixer.music.set_volume(.6)
           plot_snake(gameWindow, black, snk_list, snake_size)
       pygame.display.update()
       clock.tick(fps)
   pygame.quit()
   sys.exit()
welcome()