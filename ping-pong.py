import pygame

win_width = 600
win_height = 500
BACK = (200, 255, 255)
game = True

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed, x, y, w, h):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image), (w, h)
            )
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        pygame.draw.rect(window, BACK, self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y+4))

class Player(GameSprite):
    def update_r(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

    def update_l(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

window = pygame.display.set_mode((win_width, win_height))
window.fill(BACK)
clock = pygame.time.Clock()

player_l = Player('rocket.jpg', 4, 30, 200, 50, 158)
player_r = Player('rocket.jpg', 4, 520, 200, 50, 158)
ball = GameSprite('ball.png', 4, 200, 200, 50, 50)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    player_l.reset()
    player_r.reset()
    ball.reset()
    player_l.update_l()
    player_r.update_r()
    clock.tick(40)
    pygame.display.update()
