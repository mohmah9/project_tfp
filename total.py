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
<<<<<<< HEAD
        self.bullet_speed = 4
        self.bull_status = 'Alive'
        self.m_down=False
        self.bull_angle =self.boss.tankangle
        self.lifetime =0
        self.number = bullet.number
        self.bull_vx = math.cos(math.radians(self.bull_angle)) * self.bullet_speed
        self.bull_vy = math.sin(math.radians(self.bull_angle)) * self.bullet_speed
        self.angle = self.bull_angle
        self.born_time = time.time()
        boss.bullets.append(self)
    def kill(self,tank):
        tank.status = "dead"
    def draw(self):
        center_bullet = (int(self.bull_x), int(self.bull_y))
        radius = 5
        bull_pos_U = (int(center_bullet[0] + self.bull_vx), int(center_bullet[1] - radius + self.bull_vy))
        bull_pos_D = (int(center_bullet[0] + self.bull_vx), int(center_bullet[1] + radius + self.bull_vy))
        bull_pos_R = (int(center_bullet[0] + radius + self.bull_vx), int(center_bullet[1] + self.bull_vy))
        bull_pos_L = (int(center_bullet[0] - radius + self.bull_vx), int(center_bullet[1] + self.bull_vy))
        bull_pos_UR = (int(center_bullet[0]+(((2**0.5)/2)*radius) + self.bull_vx), int(center_bullet[1] -(((2**0.5)/2)*radius)+ self.bull_vy))
        bull_pos_DR = (int(center_bullet[0]+(((2**0.5)/2)*radius) + self.bull_vx), int(center_bullet[1] + (((2**0.5)/2)*radius) + self.bull_vy))
        bull_pos_DL = (int(center_bullet[0] -(((2**0.5)/2)*radius)  + self.bull_vx), int(center_bullet[1] +(((2**0.5)/2)*radius)+ self.bull_vy))
        bull_pos_UL = (int(center_bullet[0] - (((2**0.5)/2)*radius) + self.bull_vx), int(center_bullet[1]-(((2**0.5)/2)*radius) + self.bull_vy))
        (RU, GU, BU, OU) = surface.get_at(bull_pos_U)
        (RD, GD, BD, OD) = surface.get_at(bull_pos_D)
        (RR, GR, BR, OR) = surface.get_at(bull_pos_R)
        (RL, GL, BL, OL) = surface.get_at(bull_pos_L)
        (RUR, GUR, BUR, OUR) = surface.get_at(bull_pos_UR)
        (RDR, GDR, BDR, ODR) = surface.get_at(bull_pos_DR)
        (RUL, GUL, BUL, OUL) = surface.get_at(bull_pos_UL)
        (RDL, GDL, BDL, ODL) = surface.get_at(bull_pos_DL)
        if (70 < RU < 80 and 70 < GU < 80 and 70 < BU < 80 and OU == 255) or (70<RD<80 and 70<GD<80 and 70<BD<80 and OD==255):
            self.bull_vy=-self.bull_vy
        elif (70<RR<80 and 70<GR<80 and 70<BR<80 and OR==255) or (70<RL<80 and 70<GL<80 and 70<BL<80 and OL==255):
            self.bull_vx =-self.bull_vx
        elif (70 < RUR < 80 and 70 < GUR < 80 and 70 < BUR < 80 and OUR == 255) or (70<RDR<80 and 70<GDR<80 and 70<BDR<80 and ODR==255) or(70 < RUL < 80 and 70 < GUL < 80 and 70 < BUL < 80 and OUL == 255) or (70<RDL<80 and 70<GDL<80 and 70<BDL<80 and ODL==255):
            self.bull_vx = -self.bull_vx
            self.bull_vym = -self.bull_vy
        self.bull_y += self.bull_vy
        self.bull_x += self.bull_vx
        pygame.draw.circle(surface, (0, 0, 0), (int(self.bull_x), int(self.bull_y)), 5)
    def kill(self):
        self.bull_status = 'dead'


def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image



def barkhord_be_kodoom_tank(bullet,tank,tank2,tank3 = None):
    global bullet_counter
    if tank3 == None:
        bullet_radius = 5
        tank_radius = tank.width/2
        center_tank = (tank.player_x + tank_radius, tank.player_y + tank_radius)
        tank2_radius = tank2.width/2
        center_tank2 = (tank2.player_x + tank2_radius, tank2.player_y + tank2_radius)
        center_bullet = (int(bullet.bull_x), int(bullet.bull_y))
        center_distance1 = float((abs((center_bullet[0] - center_tank[0]) ** 2 + (center_bullet[1] - center_tank[1]) ** 2)) ** 0.5)
        center_distance2 = float((abs((center_bullet[0] - center_tank2[0]) ** 2 + (center_bullet[1] - center_tank2[1]) ** 2)) ** 0.5)
        radius_sum2 = tank2_radius + bullet_radius
        radius_sum1 = tank_radius + bullet_radius
        if radius_sum1 >= center_distance1 and time.time() - bullet.born_time > 0.5:
            bullet.bull_status = 'dead'
            bullet_counter-=1
            tank.status = 'dead'
            tank_list.remove(tank)
            tank.player_x = 100
            tank.player_y = 100
            bullet.bull_x, bullet.bull_y = 0, 0
        if radius_sum2 >= center_distance2 and time.time() - bullet.born_time > 0.5:
            bullet.bull_status = 'dead'
            bullet_counter -= 1
            tank2.status = 'dead'
            tank_list.remove(tank2)
            tank2.player_x = 100
            tank2.player_y = 100
            bullet.bull_x, bullet.bull_y = 0, 0
    else:
        bullet_radius = 5
        tank_radius = tank.width / 2
        tank3_radius = tank3.width / 2
        center_tank = (tank.player_x + tank_radius, tank.player_y + tank_radius)
        tank2_radius = tank2.width / 2
        center_tank2 = (tank2.player_x + tank2_radius, tank2.player_y + tank2_radius)
        center_tank3 = (tank3.player_x + tank3_radius, tank3.player_y + tank3_radius)
        center_bullet = (int(bullet.bull_x), int(bullet.bull_y))
        center_distance1 = float(
            (abs((center_bullet[0] - center_tank[0]) ** 2 + (center_bullet[1] - center_tank[1]) ** 2)) ** 0.5)
        center_distance3 = float(
            (abs((center_bullet[0] - center_tank3[0]) ** 2 + (center_bullet[1] - center_tank3[1]) ** 2)) ** 0.5)
        center_distance2 = float(
            (abs((center_bullet[0] - center_tank2[0]) ** 2 + (center_bullet[1] - center_tank2[1]) ** 2)) ** 0.5)
        radius_sum2 = tank2_radius + bullet_radius
        radius_sum1 = tank_radius + bullet_radius
        radius_sum3 = tank3_radius + bullet_radius
        if radius_sum3 >= center_distance3 and time.time() - bullet.born_time > 0.5:
            bullet.bull_status = 'dead'
            tank3.status = 'dead'
            bullet_counter -= 1
            tank_list.remove(tank3)
            tank3.player_x = 100
            tank3.player_y = 100
            bullet.bull_x, bullet.bull_y = 0, 0
        if radius_sum1 >= center_distance1 and time.time() - bullet.born_time > 0.5:
            bullet.bull_status = 'dead'
            tank.status = 'dead'
            bullet_counter -= 1
            tank_list.remove(tank)
            tank.player_x = 100
            tank.player_y = 100
            bullet.bull_x, bullet.bull_y = 0, 0
        if radius_sum2 >= center_distance2 and time.time() - bullet.born_time > 0.5:
            bullet.bull_status = 'dead'
            tank2.status = 'dead'
            bullet_counter -= 1
            tank_list.remove(tank2)
            tank2.player_x = 100
            tank2.player_y = 100
            bullet.bull_x, bullet.bull_y = 0, 0

def display_score(counter_tank,counter_tank2,counter_tank3=None,x=None,y=None):
    if counter_tank3 == None:
        font_tank1 = pygame.font.SysFont(None,25)
        text_tank1 = font_tank1.render(str(counter_tank),True,(0,0,0))
        surface.blit(text_tank1,(1350,900))
        font_tank2 = pygame.font.SysFont(None, 25)
        text_tank2 = font_tank2.render(str(counter_tank2), True, (0, 0, 0))
        surface.blit(text_tank2, (700, 900))
    else:
        font_tank1 = pygame.font.SysFont(None, 25)
        text_tank1 = font_tank1.render(str(counter_tank), True, (0, 0, 0))
        surface.blit(text_tank1, (1350, 900))
        font_tank2 = pygame.font.SysFont(None, 25)
        text_tank2 = font_tank2.render(str(counter_tank2), True, (0, 0, 0))
        surface.blit(text_tank2, (700, 900))
        font_tank3 = pygame.font.SysFont(None, 25)
        text_tank3 = font_tank3.render(str(counter_tank3), True, (0, 0, 0))
        surface.blit(text_tank3, (x, y))



def two_player():

    global bullet_counter
    global tank_list
    tank = tanks(725, 600, 0,35)
    tank2 = tanks(1100,200,0,35)
    tank_list = [tank,tank2]

    while True:
        surface.blit(board_image_two, (screensize[0]/2-594, screensize[1]/2-400))
        display_score(counter_tank2, counter_tank)

        for event in game_events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_UP:
                    tank.up_down = True
                if event.key == pygame.K_DOWN:
                    tank.down_down = True
                if event.key == pygame.K_LEFT:
                    tank.left_down = True
                if event.key == pygame.K_RIGHT:
                    tank.right_down = True
                if event.key == pygame.K_m and tank.status=='alive':
                    tank.firing()
                    bullet_counter+=1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    tank.left_down = False
                if event.key == pygame.K_RIGHT:
                    tank.right_down = False
                if event.key == pygame.K_UP:
                    tank.up_down = False
                    tank.playervy = math.cos(math.radians(tank.tankangle)) * tank.move_speed
                    tank.playervx = math.sin(math.radians(tank.tankangle)) * tank.move_speed
                if event.key == pygame.K_DOWN:
                    tank.down_down = False
                    tank.playervy = math.cos(math.radians(tank.tankangle)) * tank.move_speed
                    tank.playervx = math.sin(math.radians(tank.tankangle)) * tank.move_speed
            if event.type == game_locals.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    tank2.up_down = True
                if event.key == pygame.K_d:
                    tank2.down_down = True
                if event.key == pygame.K_s:
                    tank2.left_down = True
                if event.key == pygame.K_f:
                    tank2.right_down = True
                if event.key == pygame.K_q and tank2.status=='alive':
                    tank2.firing()
                    bullet_counter += 1
=======
        
>>>>>>> origin/master
