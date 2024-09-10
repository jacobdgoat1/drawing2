import pygame

pygame.init()

Window_width = 600
window_height = 600
display_surface = pygame.display.set_mode((Window_width, window_height))
pygame.display.set_caption("Drawing object")

Black = (0, 0, 0)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
display_surface.fill(Black)


Top_left_x = 250
top_left_y = 75
width = 200
height = 100
rect = pygame.Rect(Top_left_x, top_left_y, width, height)
pygame.draw.rect(display_surface, Red, rect)

START= (250,75)
END = (200,600)
pygame.draw.line(display_surface, Yellow, START,END, 30)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
