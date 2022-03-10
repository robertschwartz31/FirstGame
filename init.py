import pygame.image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SIZE = (700, 500)
FPS = 60
isJump = False
jumpCount = 10
samusImg = pygame.image.load('./img/samus.png')
ridleyImg = pygame.image.load('./img/ridley.png')

ridleyDim = {'height': 120, 'width': 120}
ridleyDim['x'] = SIZE[0] - ridleyDim['width'] - 50
ridleyDim['y'] = SIZE[1] - ridleyDim['height'] - 100

samusDim = {'height': 40, 'width': 40}
samusDim['x'] = 0 + samusDim['width'] + 50
samusDim['y'] = SIZE[1] - samusDim['height'] - 100
