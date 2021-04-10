import pygame
import sys
import random
import time

COLOR = {"BLACK":(0,0,0),"WHITE":(255,255,255),"RED":(255,0,0)}
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#How 2 use: COLOR["BLACK"]


class Ball:
    def __init__(self, x_speed_ball, y_speed_ball, pos_ball = [400,400]):
        self.pos_ball = pos_ball
        self.x_speed_ball = x_speed_ball
        self.y_speed_ball = y_speed_ball

    def ball_start(self):

        self.pos_ball = [400,400]
        print('ball spawn')
        #time.sleep(3)

class Bar:
    def __init__(self, bar_speed = 0.6, left_pos_bar = [40, 400], right_pos_bar = [760, 400] ):
        self.bar_speed = bar_speed
        self.left_pos_bar = left_pos_bar
        self.right_pos_bar = right_pos_bar

    def bar_move(self):
        key_event = pygame.key.get_pressed()

        if key_event[pygame.K_w]:
            self.left_pos_bar[1] -= self.bar_speed
        if key_event[pygame.K_s]:
            self.left_pos_bar[1] += self.bar_speed
        if key_event[pygame.K_UP]:
            self.right_pos_bar[1] -= self.bar_speed
        if key_event[pygame.K_DOWN]:
            self.right_pos_bar[1] += self.bar_speed

class Game():
    def __init__(self, screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)), Lp_point = 0, Rp_point = 0):

        self.screen = screen
        self.Rp_point = Rp_point
        self.Lp_point = Lp_point
        self.a_1 = Ball(0.2, 0.4)
        self.a_2 = Bar()
        pygame.init()
        pygame.display.set_caption("pygame")


    def draw(self):
        self.screen.fill(COLOR["BLACK"])
        pygame.draw.rect(self.screen, COLOR["WHITE"], pygame.Rect(self.a_2.left_pos_bar[0], self.a_2.left_pos_bar[1],5,50))
        pygame.draw.rect(self.screen, COLOR["WHITE"], pygame.Rect(self.a_2.right_pos_bar[0], self.a_2.right_pos_bar[1],5,50))
        pygame.draw.circle(self.screen, COLOR["RED"],[self.a_1.pos_ball[0],self.a_1.pos_ball[1]] ,5)
        pygame.display.update()

    def score(self):
        if self.a_1.pos_ball[0]<5:
            self.Rp_point +=1
            print('right player +1')
            self.a_1.ball_start()
            print("right player score:",self.Rp_point)
        elif self.a_1.pos_ball[0]>795:
            self.Lp_point +=1
            print('left player +1')
            self.a_1.ball_start()
            print("left player score:",self.Lp_point)
    def ball_move(self):

        if self.a_1.pos_ball[0] - self.a_2.left_pos_bar[0] <=2:
            if abs(self.a_2.left_pos_bar[1] - self.a_1.pos_ball[1])<30:
                self.a_1.x_speed_ball = abs(self.a_1.x_speed_ball)

        if self.a_2.right_pos_bar[0] - self.a_1.pos_ball[0] <=2:
            if abs(self.a_2.right_pos_bar[1] - self.a_1.pos_ball[1])<30:
                self.a_1.x_speed_ball = -abs(self.a_1.x_speed_ball)

        if self.a_1.pos_ball[1]<0:
            self.a_1.y_speed_ball = -self.a_1.y_speed_ball
        elif self.a_1.pos_ball[1]>800:
            self.a_1.y_speed_ball = -self.a_1.y_speed_ball
        self.a_1.pos_ball[0] += self.a_1.x_speed_ball
        self.a_1.pos_ball[1] += self.a_1.y_speed_ball



test = Game()
clock=pygame.time.Clock()
while True:
    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    test.a_2.bar_move()
    test.ball_move()
    test.draw()
    #print(test.a_1.pos_ball)
    test.score()

