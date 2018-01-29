import pygame , time , math , sys
import pygame.event as game_events
import pygame.locals as game_locals
pygame.init()
screensize = (pygame.display.Info().current_w,pygame.display.Info().current_h)
board_image=pygame.image.load('C:/Users/agha mohammad/Desktop/Games-with-Pygame-master/Part 3/maps/map3_3.png')
menu = pygame.image.load('C:/Users/agha mohammad/Desktop/Games-with-Pygame-master/Part 3/menu.png')
menu = pygame.transform.scale(menu, (screensize[0], screensize[1]))
tank_image=pygame.image.load('C:/Users/agha mohammad/Desktop/Games-with-Pygame-master/Part 3/tank3.png')
tank2_image=pygame.image.load('C:/Users/agha mohammad/Desktop/Games-with-Pygame-master/Part 3/tank4.png')
tank3_image=pygame.image.load('C:/Users/agha mohammad/Desktop/Games-with-Pygame-master/Part 3/tank3.png')
tank_imag=0
screensize = (pygame.display.Info().current_w,pygame.display.Info().current_h)
surface = pygame.display.set_mode(screensize,pygame.FULLSCREEN)
def button(msg,btn_x,btn_y,width,height,inactive_color,active_color,action=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if btn_x+width>mouse[0]>btn_x and btn_y+height>mouse[1]>btn_y:
        pygame.draw.rect(surface,active_color,(btn_x,btn_y,width,height))
        if click[0] == 1 and action != None:
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
        button('THREE PLAYER',screensize[0]/2-400,screensize[1]/2+60,800,50,(250,0,0),(255,255,0))
        button('QUIT',screensize[0]/2-400,screensize[1]/2+120,800,50,(250,0,0),(255,255,0),quitgame)
        pygame.display.update()
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
        self.cenetrx=self.player_x+12
        self.cenetry=self.player_y+12
        self.tank_pos_1= (int(self.cenetrx + self.playervx + 12 * math.cos(math.radians(self.tankangle))),int(self.cenetry + self.playervy + 12 * math.sin(math.radians(self.tankangle))))
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
            (RU, GU, BU, OU) = surface.get_at(tank_pos_U)
            (RD, GD, BD, OD) = surface.get_at(tank_pos_D)
            (RR, GR, BR, OR) = surface.get_at(tank_pos_R)
            (RL, GL, BL, OL) = surface.get_at(tank_pos_L)
            if not ((70<RU<80 and 70<GU<80 and 70<BU<80 and OU==255) or (70<RD<80 and 70<GD<80 and 70<BD<80 and OD==255) or (70<RR<80 and 70<GR<80 and 70<BR<80 and OR==255) or (70<RL<80 and 70<GL<80 and 70<BL<80 and OL==255)):
                self.player_y += self.playervy
                self.player_x += self.playervx
        if self.down_down:
            self.playervx = math.cos(math.radians(self.tankangle)) * self.move_speed
            self.playervy = math.sin(math.radians(self.tankangle)) * self.move_speed
            tank_pos_U = (int(center[0] - self.playervx),int(center[1] -radius - self.playervy))
            tank_pos_D = (int(center[0] - self.playervx),int(center[1] +radius - self.playervy))
            tank_pos_R = (int(center[0] + radius - self.playervx), int(center[1] - self.playervy))
            tank_pos_L = (int(center[0] - radius - self.playervx), int(center[1] - self.playervy))
            (RU, GU, BU, OU) = surface.get_at(tank_pos_U)
            (RD, GD, BD, OD) = surface.get_at(tank_pos_D)
            (RR, GR, BR, OR) = surface.get_at(tank_pos_R)
            (RL, GL, BL, OL) = surface.get_at(tank_pos_L)
            if not ((70<RU<80 and 70<GU<80 and 70<BU<80 and OU==255) or (70<RD<80 and 70<GD<80 and 70<BD<80 and OD==255) or (70<RR<80 and 70<GR<80 and 70<BR<80 and OR==255) or (70<RL<80 and 70<GL<80 and 70<BL<80 and OL==255)):
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
        center = (self.boss.player_x + 12, self.boss.player_y + 12)
        tank_pos_1 = (int(center[0] + self.boss.playervx + 17.5 * math.cos(math.radians(self.boss.tankangle))),
                      int(center[1] + self.boss.playervy + 17.5 * math.sin(math.radians(self.boss.tankangle))))
        self.bull_x = tank_pos_1[0]
        self.bull_y = tank_pos_1[1]
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
        (RU, GU, BU, OU) = surface.get_at(bull_pos_U)
        (RD, GD, BD, OD) = surface.get_at(bull_pos_D)
        (RR, GR, BR, OR) = surface.get_at(bull_pos_R)
        (RL, GL, BL, OL) = surface.get_at(bull_pos_L)
        if (70 < RU < 80 and 70 < GU < 80 and 70 < BU < 80 and OU == 255) or (70<RD<80 and 70<GD<80 and 70<BD<80 and OD==255):
            self.bull_vy=-self.bull_vy
        elif (70<RR<80 and 70<GR<80 and 70<BR<80 and OR==255) or (70<RL<80 and 70<GL<80 and 70<BL<80 and OL==255):
            self.bull_vx =-self.bull_vx
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
def barkhord_be_kodoom_tank(bullet,tank,tank2):
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
        tank.status = 'dead'
        tank.player_x = 100
        tank.player_y = 100
        bullet.bull_x, bullet.bull_y = 0, 0
    if radius_sum2 >= center_distance2 and time.time() - bullet.born_time > 0.5:
        bullet.bull_status = 'dead'
        tank2.status = 'dead'
        tank2.player_x = 100
        tank2.player_y = 100
        bullet.bull_x, bullet.bull_y = 0, 0
def two_player():
    tank = tanks(700, 600, 0,35)
    tank2 = tanks(800, 700, 0, 35)
    tank_list = [tank, tank2]
    while True:
        surface.blit(board_image, (screensize[0] / 2 - 594, screensize[1] / 2 - 400))
        for event in game_events.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tank.up_down = True
                if event.key == pygame.K_DOWN:
                    tank.down_down = True
                if event.key == pygame.K_LEFT:
                    tank.left_down = True
                if event.key == pygame.K_RIGHT:
                    tank.right_down = True
                if event.key == pygame.K_m:
                    tank.firing()
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
                if event.key == pygame.K_q:
                    tank2.firing()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    tank2.left_down = False
                if event.key == pygame.K_f:
                    tank2.right_down = False
                if event.key == pygame.K_e:
                    tank2.up_down = False
                    tank2.playervy = math.cos(math.radians(tank2.tankangle)) * tank2.move_speed
                    tank2.playervx = math.sin(math.radians(tank2.tankangle)) * tank2.move_speed
                if event.key == pygame.K_d:
                    tank2.down_down = False
                    tank2.playervy = math.cos(math.radians(tank2.tankangle)) * tank2.move_speed
                    tank2.playervx = math.sin(math.radians(tank2.tankangle)) * tank2.move_speed
        for b in tank.bullets:
            barkhord_be_kodoom_tank(b, tank, tank2)
            if time.time() - b.born_time > 15:
                b.bull_status = 'dead'
                b.bull_x, b.bull_y = 0, 0
            if b.bull_status == 'Alive':
                b.draw()
        for b in tank2.bullets:
            barkhord_be_kodoom_tank(b, tank, tank2)
            if time.time() - b.born_time > 15:
                b.bull_status = 'dead'
                b.bull_x, b.bull_y = 0, 0
            if b.bull_status == 'Alive':
                b.draw()
        if tank.status == 'alive':
            surface.blit(rot_center(tank_image, -tank.tankangle), (tank.player_x, tank.player_y))
        if tank2.status == 'alive':
            surface.blit(rot_center(tank2_image, -tank2.tankangle), (tank2.player_x, tank2.player_y))
        tank.move()
        tank2.move()
        pygame.display.flip()


def tank_rotation(tan):
    pass


intro()