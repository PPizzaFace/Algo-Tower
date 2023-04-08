from pygame import *
'''Необходимые классы'''

clock = time.Clock()
FPS = 60
x1 = 20
y1 = 30
x2 = 10
y2 = 20
speed = 10

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
            keys = key.get_pressed()
            if keys [K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys [K_a] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys [K_s] and self.rect.y < 450:
                self.rect.y += self.speed
            if keys [K_d] and self.rect.x < 650:
                self.rect.x += self.speed   

class Enemy(GameSprite):

    direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 650:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed    

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = surface((self.wall_width, self.wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("back.png"), (win_width, win_height))

#Персонажи игры:
player = Player('spice.png', 5, win_height - 80, 4)
monster = Enemy('elban.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

game = True
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

Wall1 = Wall(56, 56, 56, 10, 350, 100, 0)
Wall2 = Wall(200, 200, 200, 200, 10, 100, 150)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0, 0))
    player.reset()
    monster.reset()
    player.update()
    monster.update()

    Wall1.draw_wall()
    Wall2.draw_wall()

    if sprite.collide_rect(player,monster):
        print ('текст')
        player.rect.x = 5
        player.rect.y = 420
        sleep(2)

    if sprite.collide_rect(player, Wall1):
        print('1, 2, 3')
        player.rect.x = 5
        player.rect.y = 420
        sleep(2)

    display.update()
    clock.tick(FPS)