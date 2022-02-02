import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))

First_dot_x = random.randrange(500)
First_dot_y = random.randrange(100)

Second_dot_x = random.randrange(200)
Second_dot_y = random.randrange(100, 400)

Third_dot_x = random.randrange(300, 500)
Third_dot_y = random.randrange(100, 400)

New_dot_x = 250
New_dot_y = 250

First_dot = pygame.draw.circle(win, (255, 255, 255), (First_dot_x, First_dot_y ), 1)

Second_dot = pygame.draw.circle(win, (255, 255, 255), (Second_dot_x, Second_dot_y), 1)

third_dot = pygame.draw.circle(win, (255, 255, 255), (Third_dot_x, Third_dot_y), 1)
while 1:
    pygame.display.update()
    pygame.time.delay(1)
    random_numb = random.randrange(1, 4)
    if random_numb == 1:
        New_dot_x = (New_dot_x+First_dot_x)//2
        New_dot_y = (New_dot_y+First_dot_y)//2
        New_dot = pygame.draw.circle(win, (255, 255, 255), (New_dot_x, New_dot_y), 1)
    if random_numb == 2:
        New_dot_x = (New_dot_x+Second_dot_x)//2
        New_dot_y = (New_dot_y+Second_dot_y)//2
        New_dot = pygame.draw.circle(win, (255, 255, 255), (New_dot_x, New_dot_y), 1)
    if random_numb == 3:
        New_dot_x = (New_dot_x+Third_dot_x)//2
        New_dot_y = (New_dot_y+Third_dot_y)//2
        New_dot = pygame.draw.circle(win, (255, 255, 255), (New_dot_x, New_dot_y), 1)


