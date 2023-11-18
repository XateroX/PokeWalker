import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((240, 240))
        self.clock = pygame.time.Clock()
        self.running = True

    def tick(self):
        if self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("black")
            pygame.display.flip()
        return self.running
        

if __name__ == "__main__":
    game = Game()
    while True:
        game.tick()
