from kivgame.pygame import pygame as pg
pygame = pg.init()

class Game(object):
    def __init__(self):
        self.size = self.width, self.height = 800, 480
        self.speed = [10, 5]
        self.screen = pygame.display.set_mode(self.size)
        self.ball = pygame.image.load("img/ball.bmp")
        self.ballrect = self.ball.get_rect()

    def loop(self):
        self.ballrect = self.ballrect.move(self.speed)

        if self.ballrect.left < 0 or self.ballrect.right > self.width:
            self.speed[0] = -self.speed[0]

        if self.ballrect.top < 0 or self.ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()

def main():
    game = Game()
    pygame.set_loop(game.loop)
    pygame.run()

if __name__ == "__main__":
    main()