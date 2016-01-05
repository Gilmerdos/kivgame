from kivgame.pygame import pygame as pg
pygame = pg.init()

size = width, height = 800, 480
speed = [10, 5]
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

def loop():
    rect = ballrect.move(speed)
    if rect.left < 0 or rect.right > width: speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height: speed[1] = -speed[1]
    screen.blit(ball, rect)
    pygame.display.flip()

def main():
    pygame.set_loop(loop)
    pygame.run()

if __name__ == "__main__":
    main()