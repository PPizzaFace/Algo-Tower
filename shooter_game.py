from pygame import *

window = display.set_mode((700,500))
background = transform.scale(image.load('probel.png'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bullets = sprite.Group()

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
    # метод "выстрел"
    def fire(self):
        bullet = Bullet('laik.png', self.rect.x, self.rect.top, 5)
        bullets.add(bullet)

# создайте стрельбу в игровом цикле при помощи пробела

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

score = 0
lost = 0

from random import *
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(50, 650)
            self.rect.y = -50
            lost += 1

monsters = sprite.Group()

for i in range(5):
    monster = Enemy('diz.jpg', randint(50,650), randint(-350,0), 2)
    monsters.add(monster)

Hero = Player('NAVI_MMA.png', 350, 450, 10)
run = True

clock = time.Clock()


from random import *
class Meteor(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(50, 650)
            self.rect.y = -50

monsters = sprite.Group()

for i in range(4):
    monster = Meteor('edgar.jpg', randint(50,650), randint(-350,0), 2)
    monsters.add(monster)

Hero = Player('NAVI_MMA.png', 350, 450, 10)
run = True

clock = time.Clock()


##################################################



# создаю шрифт
font.init()
font1 = font.Font(None, 36)

monsters.draw

begaet_chel = True

while run:

    text_score = font1.render('ОЧКИ: ' + str(score), 1, (255, 140, 0))
    text_lost = font1.render('Дизлайки: ' + str(lost), 1, (255, 140, 0))

    window.blit(background, (0,0))
    window.blit(text_score, (0,0))
    window.blit(text_lost, (0,50))


    monsters.draw(window)
    monsters.update()

    monsters.draw(window)

    if begaet_chel:
        bullets.update()
        Hero.update()
        monsters.update()

    if sprite.spritecollide(Hero, monsters, False):
        window.blit(font1.render('-9 кубкAв',1,(255, 140, 0)),(300,200))
        begaet_chet = False

    if lost >= 5:
        window.blit(font1.render('-9 кубкAв',1,(255, 140, 0)),(300,200))
        begaet_chel = False

    if sprite.groupcollide(bullets, monsters, True, True):
        monster = Enemy('diz.jpg', randint(50,650), randint(-350,0), 5)
        monsters.add(monster)
        score += 168

    if score >= 10:
        window.blit(font1.render('топ Штольни',1,(255, 140, 0)),(300,200))


    bullets.draw(window)
    bullets.update()

    Hero.reset()
    Hero.update()
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                Hero.fire()

    display.update()
    clock.tick(60)    