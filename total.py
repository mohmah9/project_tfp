import pygame , time
import pygame.event as game_events
import pygame.locals as game_locals
import sys
import math
counter_tank =0
counter_tank2 = 0
counter_tank3 = 0
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screensize = (pygame.display.Info().current_w,pygame.display.Info().current_h)
board_image_two=pygame.image.load('map2_2 (2).png')
board_image_three=pygame.image.load('map2_3 (2).png')
menu = pygame.image.load('menu.png')
menu = pygame.transform.scale(menu, (screensize[0], screensize[1]))
tank_image=pygame.image.load('tank1.png')
tank2_image=pygame.image.load('tank2.png')
tank3_image=pygame.image.load('tank3.png')
tank_imag=0
screensize = (pygame.display.Info().current_w,pygame.display.Info().current_h)
surface = pygame.display.set_mode(screensize,pygame.FULLSCREEN)
global bullet_counter
bullet_counter =0
pygame.mixer.music.load('Crysis_1_full_soundtrack.134 - Segment1(00_01_51.668-00_03_27.093).mp3')
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(-1)
def button(msg,btn_x,btn_y,width,height,inactive_color,active_color,action=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if btn_x+width>mouse[0]>btn_x and btn_y+height>mouse[1]>btn_y:
        pygame.draw.rect(surface,active_color,(btn_x,btn_y,width,height))
        if click[0] == 1 and action != None:
            pygame.mixer.quit()
            pygame.mixer.init()
            pygame.mixer.music.load('Blood Bag.mp3')
            pygame.mixer.music.set_volume(50)
            pygame.mixer.music.play(-1)
            action()
    else:
        pygame.draw.rect(surface,inactive_color,(btn_x,btn_y,width,height))
    text = pygame.font.Font('freesansbold.ttf',30)
    textsurf = text.render(msg, False, (0, 0, 0))
    text_welcome = textsurf.get_rect(center=(btn_x+width/2, btn_y+height/2))
    surface.blit(textsurf,text_welcome)
def quitgame():
    pygame.quit()
    quit()




def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        surface.blit(menu,(0,0))
        largetext = pygame.font.Font('freesansbold.ttf',75)
        textsurface = largetext.render('welcome to alter tank', False, (10, 10, 10))
        text_welcome = textsurface.get_rect(center=(screensize[0]/2, screensize[1]/4))
        surface.blit(textsurface, text_welcome)
        button('TWO PLAYER',screensize[0]/2-400,screensize[1]/2,800,50,(250,0,0),(255,255,0),two_player)
        button('THREE PLAYER',screensize[0]/2-400,screensize[1]/2+60,800,50,(250,0,0),(255,255,0),three_player)
        button('QUIT',screensize[0]/2-400,screensize[1]/2+120,800,50,(250,0,0),(255,255,0),quitgame)
        pygame.display.flip()


window_width = screensize[0]
window_height = screensize[1]

class tanks:
    def __init__(self,player_x,player_y,angle,width):
        self.bullets=[]
        self.player_x = player_x
        self.player_y = player_y
        self.move_speed = 4
        self.status = 'alive'
        self.down_down = False
        self.up_down = False
        self.left_down = False
        self.right_down = False
        self.degree_speed = 4
        self.player_size=20
        self.tankangle=angle
        self.playervx=0
        self.playervy=0
        self.width = width
        self.m_down=False
        self.cenetrx=self.player_x+self.width/2
        self.cenetry=self.player_y+self.width/2
        self.tank_pos_1= (int(self.cenetrx + self.playervx + self.width/2 * math.cos(math.radians(self.tankangle))),int(self.cenetry + self.playervy + self.width/2 * math.sin(math.radians(self.tankangle))))
    def up_down(self):
        return self.up_down
    def down_down(self):
        return self.down_down
    def move(self):
        if self.left_down:
            self.tankangle-=self.degree_speed
            self.tankangle = self.tankangle % 360
        if self.right_down:
            self.tankangle +=self.degree_speed
            self.tankangle = self.tankangle % 360
        radius=(self.width)/2
        center=(self.player_x+radius,self.player_y+radius)
        if self.up_down:
            self.playervx = math.cos(math.radians(self.tankangle)) * self.move_speed
            self.playervy = math.sin(math.radians(self.tankangle)) * self.move_speed
            tank_pos_U = (int(center[0]+self.playervx), int(center[1]-radius+self.playervy))
            tank_pos_D = (int(center[0]+self.playervx), int(center[1]+radius+self.playervy))
            tank_pos_R = (int(center[0]+radius+self.playervx), int(center[1] + self.playervy))
            tank_pos_L = (int(center[0]-radius +self.playervx), int(center[1]+ self.playervy))
            tank_pos_UR = (int(center[0] + (((2 ** 0.5) / 2) * radius) + self.playervx),int(center[1] - (((2 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_DR = (int(center[0] + (((2 ** 0.5) / 2) * radius) + self.playervx),int(center[1] + (((2 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_DL = (int(center[0] - (((2 ** 0.5) / 2) * radius) + self.playervx),int(center[1] + (((2 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_UL = (int(center[0] - (((2 ** 0.5) / 2) * radius) + self.playervx),int(center[1] - (((2 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_UR60 = (int(center[0] + ((1 / 2) * radius) + self.playervx),int(center[1] - (((3 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_DR60 = (int(center[0] + (((1 ** 0.5) / 2) * radius) + self.playervx),int(center[1] + (((3 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_DL60 = (int(center[0] - ((1 / 2) * radius) + self.playervx),int(center[1] + (((3 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_UL60 = (int(center[0] - ((1 / 2) * radius) + self.playervx),int(center[1] - (((3 ** 0.5) / 2) * radius) + self.playervy))
            tank_pos_UR30 = (int(center[0] + (((3 ** 0.5) / 2) * radius) + self.playervx),int(center[1] - (((1) / 2) * radius) + self.playervy))
            tank_pos_DR30 = (int(center[0] + (((3 ** 0.5) / 2) * radius) + self.playervx),int(center[1] + (((1) / 2) * radius) + self.playervy))
            tank_pos_DL30 = (int(center[0] - (((3 ** 0.5) / 2) * radius) + self.playervx),int(center[1] + (((1) / 2) * radius) + self.playervy))
            tank_pos_UL30 = (int(center[0] - (((3 ** 0.5) / 2) * radius) + self.playervx),int(center[1] - (((1) / 2) * radius) + self.playervy))

            (RU, GU, BU, OU) = surface.get_at(tank_pos_U)
            (RD, GD, BD, OD) = surface.get_at(tank_pos_D)
            (RR, GR, BR, OR) = surface.get_at(tank_pos_R)
            (RL, GL, BL, OL) = surface.get_at(tank_pos_L)
            (RUR, GUR, BUR, OUR) = surface.get_at(tank_pos_UR)
            (RDR, GDR, BDR, ODR) = surface.get_at(tank_pos_DR)
            (RUL, GUL, BUL, OUL) = surface.get_at(tank_pos_UL)
            (RDL, GDL, BDL, ODL) = surface.get_at(tank_pos_DL)
            (RUR60, GUR60, BUR60, OUR60) = surface.get_at(tank_pos_UR60)
            (RDR60, GDR60, BDR60, ODR60) = surface.get_at(tank_pos_DR60)
            (RUL60, GUL60, BUL60, OUL60) = surface.get_at(tank_pos_UL60)
            (RDL60, GDL60, BDL60, ODL60) = surface.get_at(tank_pos_DL60)
            (RUR30, GUR30, BUR30, OUR30) = surface.get_at(tank_pos_UR30)
            (RDR30, GDR30, BDR30, ODR30) = surface.get_at(tank_pos_DR30)
            (RUL30, GUL30, BUL30, OUL30) = surface.get_at(tank_pos_UL30)
            (RDL30, GDL30, BDL30, ODL30) = surface.get_at(tank_pos_DL30)

            if not (((70<RU<80 and 70<GU<80 and 70<BU<80 and OU==255) or (70<RD<80 and 70<GD<80 and 70<BD<80 and OD==255) or (70<RR<80 and 70<GR<80 and 70<BR<80 and OR==255) or (70<RL<80 and 70<GL<80 and 70<BL<80 and OL==255)) \
                    or((70<RUR<80 and 70<GUR<80 and 70<BUR<80 and OUR==255) or (70<RDR<80 and 70<GDR<80 and 70<BDR<80 and ODR==255)or (70<RUL<80 and 70<GUL<80 and 70<BUL<80 and OUL==255) or (70<RDL<80 and 70<GDL<80 and 70<BDL<80 and ODL==255))\
                    or((70<RUR60<80 and 70<GUR60<80 and 70<BUR60<80 and OUR60==255) or (70<RDR60<80 and 70<GDR60<80 and 70<BDR60<80 and ODR60==255)or (70<RUL60<80 and 70<GUL60<80 and 70<BUL60<80 and OUL60==255) or (70<RDL60<80 and 70<GDL60<80 and 70<BDL60<80 and ODL60==255))
                    or((70<RUR30<80 and 70<GUR30<80 and 70<BUR30<80 and OUR30==255) or (70<RDR30<80 and 70<GDR30<80 and 70<BDR30<80 and ODR30==255)or (70<RUL30<80 and 70<GUL30<80 and 70<BUL30<80 and OUL30==255) or (70<RDL30<80 and 70<GDL30<80 and 70<BDL30<80 and ODL30==255))):

                self.player_y += self.playervy
                self.player_x += self.playervx
        if self.down_down:
            self.playervx = math.cos(math.radians(self.tankangle)) * self.move_speed
            self.playervy = math.sin(math.radians(self.tankangle)) * self.move_speed
            tank_pos_U = (int(center[0] - self.playervx),int(center[1] -radius - self.playervy))
            tank_pos_D = (int(center[0] - self.playervx),int(center[1] +radius - self.playervy))
            tank_pos_R = (int(center[0] + radius - self.playervx), int(center[1] - self.playervy))
            tank_pos_L = (int(center[0] - radius - self.playervx), int(center[1] - self.playervy))
            tank_pos_UR = (int(center[0] + (((2 ** 0.5) / 2) * radius) - self.playervx),int(center[1] - (((2 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_DR = (int(center[0] + (((2 ** 0.5) / 2) * radius) - self.playervx),int(center[1] + (((2 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_DL = (int(center[0] - (((2 ** 0.5) / 2) * radius) - self.playervx),int(center[1] + (((2 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_UL = (int(center[0] - (((2 ** 0.5) / 2) * radius) - self.playervx),int(center[1] - (((2 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_UR60 = (int(center[0] + ((1 / 2) * radius) - self.playervx),int(center[1] - (((3 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_DR60 = (int(center[0] + (((1 ** 0.5) / 2) * radius) - self.playervx),int(center[1] + (((3 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_DL60 = (int(center[0] - ((1 / 2) * radius) - self.playervx),int(center[1] + (((3 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_UL60 = (int(center[0] - ((1 / 2) * radius) - self.playervx),int(center[1] - (((3 ** 0.5) / 2) * radius) - self.playervy))
            tank_pos_UR30 = (int(center[0] + (((3 ** 0.5) / 2) * radius) - self.playervx),int(center[1] - (((1) / 2) * radius) - self.playervy))
            tank_pos_DR30 = (int(center[0] + (((3 ** 0.5) / 2) * radius) - self.playervx),int(center[1] + (((1) / 2) * radius) - self.playervy))
            tank_pos_DL30 = (int(center[0] - (((3 ** 0.5) / 2) * radius) - self.playervx),int(center[1] + (((1) / 2) * radius) - self.playervy))
            tank_pos_UL30 = (int(center[0] - (((3 ** 0.5) / 2) * radius) - self.playervx),int(center[1] - (((1) / 2) * radius) - self.playervy))

            (RU, GU, BU, OU) = surface.get_at(tank_pos_U)
            (RD, GD, BD, OD) = surface.get_at(tank_pos_D)
            (RR, GR, BR, OR) = surface.get_at(tank_pos_R)
            (RL, GL, BL, OL) = surface.get_at(tank_pos_L)
            (RUR, GUR, BUR, OUR) = surface.get_at(tank_pos_UR)
            (RDR, GDR, BDR, ODR) = surface.get_at(tank_pos_DR)
            (RUL, GUL, BUL, OUL) = surface.get_at(tank_pos_UL)
            (RDL, GDL, BDL, ODL) = surface.get_at(tank_pos_DL)
            (RUR60, GUR60, BUR60, OUR60) = surface.get_at(tank_pos_UR60)
            (RDR60, GDR60, BDR60, ODR60) = surface.get_at(tank_pos_DR60)
            (RUL60, GUL60, BUL60, OUL60) = surface.get_at(tank_pos_UL60)
            (RDL60, GDL60, BDL60, ODL60) = surface.get_at(tank_pos_DL60)
            (RUR30, GUR30, BUR30, OUR30) = surface.get_at(tank_pos_UR30)
            (RDR30, GDR30, BDR30, ODR30) = surface.get_at(tank_pos_DR30)
            (RUL30, GUL30, BUL30, OUL30) = surface.get_at(tank_pos_UL30)
            (RDL30, GDL30, BDL30, ODL30) = surface.get_at(tank_pos_DL30)
            if not (((70<RU<80 and 70<GU<80 and 70<BU<80 and OU==255) or (70<RD<80 and 70<GD<80 and 70<BD<80 and OD==255) or (70<RR<80 and 70<GR<80 and 70<BR<80 and OR==255) or (70<RL<80 and 70<GL<80 and 70<BL<80 and OL==255)) \
                    or((70<RUR<80 and 70<GUR<80 and 70<BUR<80 and OUR==255) or (70<RDR<80 and 70<GDR<80 and 70<BDR<80 and ODR==255)or (70<RUL<80 and 70<GUL<80 and 70<BUL<80 and OUL==255) or (70<RDL<80 and 70<GDL<80 and 70<BDL<80 and ODL==255))\
                    or((70<RUR60<80 and 70<GUR60<80 and 70<BUR60<80 and OUR60==255) or (70<RDR60<80 and 70<GDR60<80 and 70<BDR60<80 and ODR60==255)or (70<RUL60<80 and 70<GUL60<80 and 70<BUL60<80 and OUL60==255) or (70<RDL60<80 and 70<GDL60<80 and 70<BDL60<80 and ODL60==255))
                    or((70<RUR30<80 and 70<GUR30<80 and 70<BUR30<80 and OUR30==255) or (70<RDR30<80 and 70<GDR30<80 and 70<BDR30<80 and ODR30==255)or (70<RUL30<80 and 70<GUL30<80 and 70<BUL30<80 and OUL30==255) or (70<RDL30<80 and 70<GDL30<80 and 70<BDL30<80 and ODL30==255))):

                self.player_y -= self.playervy
                self.player_x -= self.playervx
    def firing(self):
        B=bullet(self)
        B.draw()
class bullet():
    maxlifetime = 10
    number=0
    def __init__(self,boss):
        self.boss = boss
        center = (self.boss.player_x + self.boss.width/2, self.boss.player_y + self.boss.width/2)
        tank_pos_1 = (int(center[0] + self.boss.playervx + self.boss.width/2 * math.cos(math.radians(self.boss.tankangle))),int(center[1] + self.boss.playervy + self.boss.width/2 * math.sin(math.radians(self.boss.tankangle))))
        self.bull_x = tank_pos_1[0]
        self.bull_y = tank_pos_1[1]
        