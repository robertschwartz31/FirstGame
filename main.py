import pygame
from init import *
from time import sleep


class myGame:

    def __init__(self):

        pygame.init()
        self.WIN = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("My Game")

    @staticmethod
    def draw_window(self, char1, char2):

        samus = pygame.transform.scale(samusImg, (samusDim['width'], samusDim['height']))
        ridley = pygame.transform.scale(ridleyImg, (ridleyDim['width'], ridleyDim['height']))
        self.WIN.fill(WHITE)
        self.WIN.blit(samus, (char1.x, char1.y))
        self.WIN.blit(ridley, (char2.x, char2.y))
        pygame.display.update()

    def main(self):

        def getRectCoords(dict):
            return dict['x'], dict['y'], dict['width'], dict['height']

        samus = pygame.Rect(getRectCoords(samusDim))
        ridley = pygame.Rect(getRectCoords(ridleyDim))
        clock = pygame.time.Clock()
        done = False
        counter = 0

        while not done:

            clock.tick(FPS)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    done = True

            buttonPresses = pygame.key.get_pressed()
            spacePress = buttonPresses[pygame.K_SPACE]
            leftPress = buttonPresses[pygame.K_LEFT]
            rightPress = buttonPresses[pygame.K_RIGHT]

            if spacePress and samus.y > 310:
                while counter < 10:
                    samus.y -= 1
                    counter += 1
                counter = 0

            if leftPress:
                samus.x -= 3

            if rightPress:
                samus.x += 3

            if samus.y < 360:
                samus.y += 3

            self.draw_window(self, samus, ridley)

        pygame.quit()


if __name__ == "__main__":
    app = myGame()
    app.main()
