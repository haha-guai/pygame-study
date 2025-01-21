import pygame
from pygame.locals import *
#模块导入

#常量设置
screen_width = 1000
screen_height = 600
screen_size = (screen_width, screen_height)

#单次移动
def move1(event, rect, speed):
    if event.type == KEYDOWN:
        if event.key == K_w:
            rect.y -= speed
        elif event.key == K_s:
            rect.y += speed
        elif event.key == K_a:
            rect.x -= speed
        elif event.key == K_d:
            rect.x += speed
#连续移动
def move2(rect, speed):
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        rect.y -= speed
    if keys[K_s]:
        rect.y += speed
    if keys[K_a]:
        rect.x -= speed
    if keys[K_d]:
        rect.x += speed
#碰撞检测
def collide(rect1, rect2, func):
    if rect1.colliderect(rect2):
        func()
#图像大小设置
def image_scale(file, size):
    image = pygame.image.load(file)
    return pygame.transform.scale(image, size)
#图像、矩形返回
def _image(file):
    image = pygame.image.load(file)
    return image

class MySound:
    def __init__(self):
        self.hit1 = pygame.mixer.Sound('C:/Users/Administrator/Desktop/70个音效/Hit/Hit_Hurt5.wav')
class MyImage:
        pass

class Player:
    def __init__(self):
        self.run_image = image_scale("C:/Users/Administrator/Desktop/面具武侠/Run.png", (3200, 400))
        self.idle_image = image_scale("C:/Users/Administrator/Desktop/面具武侠/Idle.png", (1600, 400))
        self.jump_image = image_scale("C:/Users/Administrator/Desktop/面具武侠/JF.png", (1600, 400))
        self.atk_image = image_scale("C:/Users/Administrator/Desktop/面具武侠/ATK.png", (3200, 400))
        self.rect = pygame.Rect(0, 200, 400, 400)

        self.running = 0
        self.jumping = 0
        self.fighting = 0
        self.jump_turn = 0
        self.frame_counter = 0
        self.current_frame = 0

        self.attribute = {'life':15, 'atk':1}

    def fight(self, event):
        if event.key == K_j and not self.fighting:
            self.fighting = 1
    def fight_with(self, enemy):
        if self.fighting:
            if abs(self.rect.centerx - enemy.rect.centerx) <= 100 and self.rect.centery == enemy.rect.centery:
                enemy.attribute['life'] -= self.attribute['atk']
                print('温bensi：', enemy.attribute['life'])
    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.rect.x -= speed
            self.running = 1
        elif keys[K_d]:
            self.rect.x += speed
            self.running = 1
        else:
            self.running = 0
    def jump(self, event):
            if event.key == K_k and not self.jumping:
                self.current_frame = 0
                self.jumping = 1


    def bilt(self, screen):
        self.frame_counter += 1

        if self.jumping:
            if self.frame_counter >= 3:
                self.frame_counter = 0
                if self.current_frame == 3:
                    self.jumping = 0
                if self.current_frame <= 1:
                    self.rect.y -= 50
                else:
                    self.rect.y += 50
                self.current_frame = (self.current_frame + 1) % 4
            screen.blit(self.jump_image, self.rect, (400*self.current_frame, 0, 400, 400))
        elif self.fighting:
            if self.frame_counter >= 2:
                self.frame_counter = 0
                if self.current_frame == 7:
                    self.fighting = 0
                self.current_frame = (self.current_frame + 1) % 8
            screen.blit(self.atk_image, self.rect, (400 * self.current_frame, 0, 400, 400))
        else:
            if self.running:
                if self.frame_counter >= 2:
                    self.frame_counter = 0
                    self.current_frame = (self.current_frame + 1) % 8
                screen.blit(self.run_image, self.rect, (400*self.current_frame, 0, 400, 400))
            elif not self.running and not self.jumping and not self.fighting:
                if self.frame_counter >= 5:
                    self.frame_counter = 0
                    self.current_frame = (self.current_frame + 1) % 4
                screen.blit(self.idle_image, self.rect, (400*self.current_frame, 0, 400, 400))

class Player_:
    def __init__(self):
        self.run_image = pygame.transform.flip(image_scale("C:/Users/Administrator/Desktop/面具武侠/Run.png", (3200, 400)), True, False)
        self.idle_image = pygame.transform.flip(image_scale("C:/Users/Administrator/Desktop/面具武侠/Idle.png", (1600, 400)), True, False)
        self.jump_image = pygame.transform.flip(image_scale("C:/Users/Administrator/Desktop/面具武侠/JF.png", (1600, 400)), True, False)
        self.atk_image = pygame.transform.flip(image_scale("C:/Users/Administrator/Desktop/面具武侠/ATK.png", (3200, 400)), True, False)
        self.rect = pygame.Rect(600, 200, 400, 400)

        self.running = 0
        self.jumping = 0
        self.fighting = 0
        self.jump_turn = 0
        self.frame_counter = 0
        self.current_frame = 0

        self.attribute = {'life':15, 'atk':1}


    def fight(self, event):
        if event.key == K_KP1 and not self.fighting:
            self.fighting = 1
    def fight_with(self, enemy):
        if self.fighting:
            if abs(self.rect.centerx - enemy.rect.centerx) <= 40 and self.rect.centery == enemy.rect.centery:
                enemy.attribute['life'] -= self.attribute['atk']
                print('温shuailong：', enemy.attribute['life'])
    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= speed
            self.running = 1
        elif keys[K_RIGHT]:
            self.rect.x += speed
            self.running = 1
        else:
            self.running = 0
    def jump(self, event):
            if event.key == K_KP2 and not self.jumping:
                self.current_frame = 0
                self.jumping = 1


    def bilt(self, screen):
        self.frame_counter += 1

        if self.jumping:
            if self.frame_counter >= 3:
                self.frame_counter = 0
                if self.current_frame == 3:
                    self.jumping = 0
                if self.current_frame <= 1:
                    self.rect.y -= 50
                else:
                    self.rect.y += 50
                self.current_frame = (self.current_frame + 1) % 4
            screen.blit(self.jump_image, self.rect, (400*self.current_frame, 0, 400, 400))
        elif self.fighting:
            if self.frame_counter >= 2:
                self.frame_counter = 0
                if self.current_frame == 7:
                    self.fighting = 0
                self.current_frame = (self.current_frame + 1) % 8
            screen.blit(self.atk_image, self.rect, (400 * self.current_frame, 0, 400, 400))
        else:
            if self.running:
                if self.frame_counter >= 2:
                    self.frame_counter = 0
                    self.current_frame = (self.current_frame + 1) % 8
                screen.blit(self.run_image, self.rect, (400*self.current_frame, 0, 400, 400))
            elif not self.running and not self.jumping and not self.fighting:
                if self.frame_counter >= 5:
                    self.frame_counter = 0
                    self.current_frame = (self.current_frame + 1) % 4
                screen.blit(self.idle_image, self.rect, (400*self.current_frame, 0, 400, 400))



class Game:
    def __init__(self):
        pygame.init()
        self.sound = MySound()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('飞天胖胖猪')
        self.clock = pygame.time.Clock()
        self.bg_list = [image_scale(f"C:/Users/Administrator/Desktop/forestBackground/{i}.png", screen_size) for i in range(1, 5)]

        self.player = Player()
        self.player2 = Player_()

    def bg_load(self):
        for i in self.bg_list:
            self.screen.blit(i, (0, 0))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    self.player.fight(event)
                    self.player2.fight(event)
                    self.player.fight_with(self.player2)
                    self.player2.fight_with(self.player)
                    self.player.jump(event)
                    self.player2.jump(event)
            self.bg_load()

            self.player.move(10)
            self.player2.move(10)
            self.player.bilt(self.screen)
            self.player2.bilt(self.screen)
            pygame.display.update()

            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()