import pygame
import pygame.event as game_events
import pygame.locals as game_locals
import sys
import math
window_width = 400
window_height = 500
class tanks:
    def __init__(self,player_x,player_y,player_color='blue',angle=0):
        self.player_x = player_x
        self.player_y = player_y
        self.move_speed = 0.5
        self.status = 'alive'
        self.down_down = False
        self.up_down = False
        self.left_down = False
        self.right_down = False
        self.degree_speed = 1
        self.player_size=10
        self.tankangle=angle
        self.playervx=0
        self.playervy=0
    def up_down(self):
        return self.up_down
    def down_down(self):
        return self.down_down
    def move(self):
        if self.tankangle == 0:
            if self.up_down:
                if self.playervy > 0:
                    self.playervy = self.move_speed
                    self.playervy = -self.playervy
                if self.player_y > 0:
                    self.player_y += self.playervy
            if self.down_down:
                if self.playervy < 0:
                    self.playervy = self.move_speed
                    self.playervy = -self.playervy
                if self.player_y + self.player_size < window_height:
                    self.player_y += self.playervy
        m = math.tan(math.radians(self.tankangle))
        if m>0 and math.cos(math.radians(self.tankangle))>0:
            if self.up_down:
                if self.playervy > 0:
                    self.playervy = math.cos(math.radians(self.tankangle)) *self.move_speed
                    self.playervy = -self.playervy
                if self.player_y <window_height:
                    self.player_y += self.playervy
                if self.playervx<0:
                    self.playervx = math.sin(math.radians(self.tankangle)) *self.move_speed
                    self.playervx = -self.playervx
                if self.player_x + self.player_size< window_width:
                    self.player_x += self.playervx
