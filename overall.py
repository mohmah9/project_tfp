import pygame , time , math , sys,ctypes
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
