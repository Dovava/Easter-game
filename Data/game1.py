import pygame, random,time

pygame.init()
screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
pygame.display.set_caption('Easter catchers 2020')
done = False
char = pygame.image.load('PLAYER.png')
egg = pygame.image.load('Egg.png')
eggx, eggy = (((random.randint(6,156)/10))*100,80)
x = 960
pygame.mixer.music.load('Energy.mp3')# Copyright bensounds
icon = pygame.image.load('iCON.png')
pygame.display.set_icon(icon)
pygame.mixer.music.play(-1)
font = pygame.font.SysFont("comicsansms", 72)
points = 0
text = font.render(f"NAN", True, (0, 128, 0))
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                        if not x == 60:
                                        x -= 100
                elif pressed[pygame.K_RIGHT]:
                        if not x == 1560:
                                        x += 100
        screen.blit(char,(x,280))
        screen.blit(egg,(eggx, eggy))
        screen.blit(text,(1920-text.get_width(),0))
        clock.tick(30)
        pygame.display.update()
        screen.fill((153, 217, 234))
        eggy += 7.5
        if eggy >= 1080:
                eggx, eggy = (((random.randint(6,156)/10))*100,80)
                points -= 1
        if x >= eggx-65 and x <= eggx+65:
                if eggy >= 160 and eggy <= 490:
                        points += 1
                        eggx, eggy = (((random.randint(6,156)/10))*100,80)
        font = pygame.font.SysFont("comicsansms", 72)
        text = font.render(f"Score: {points}", True, (0, 13, 0))
pygame.quit()
