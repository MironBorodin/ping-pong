import pygame

win_width = 600
win_height = 500
BACK = (200, 255, 255)
game = True
speed_x = 3
speed_y = 3

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed, x, y, w, h):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(image), (w-8, h-8)
            )
        self.speed = speed
        self.rect = pygame.Rect(x, y, w, h)
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        pygame.draw.rect(window, BACK, self.rect)
        window.blit(self.image, (self.rect.x+4, self.rect.y+4))

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
ball = GameSprite('ball.png', 4, 200, 200, 58, 58)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if ball.rect.y >= win_height-50 or ball.rect.y <= 0:
        speed_y *= -1

    if pygame.sprite.collide_rect(ball, player_l) or pygame.sprite.collide_rect(ball, player_r):
        speed_x *= -1

    ball.rect.x += speed_x
    ball.rect.y += speed_y
    player_l.reset()
    player_r.reset()
    ball.reset()
    player_l.update_l()
    player_r.update_r()
    clock.tick(40)
    pygame.display.update()
