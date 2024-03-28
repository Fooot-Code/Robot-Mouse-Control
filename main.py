import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame")

# Image(s?)
img = pygame.image.load("C:\\Documents\\GitHub\\Robot-Mouse-Control\\joystick.png").convert()

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_background(screen):
    screen.blit(img, (0, 0))

def get_mouse_from_middle(x, y):
    yPercentFrom00 = y / 300
    yAmount = 1.0 - yPercentFrom00
    xPercentFrom00 = x / 300
    xAmount = 1.0 - xPercentFrom00

    # You cant have each axis going more than 50% at any time, so this handles it 
    if xAmount > 0.5 and yAmount > 0.5: # mouse is in top left quadrant
        xAmount, yAmount = 0.5, 0.5
    
    elif xAmount < -0.5 and yAmount > 0.5: # mouse is in top right quadrant
        xAmount, yAmount = -0.5, 0.5

    elif xAmount < -0.5 and yAmount < -0.5: # mouse is in bottom left quadrant
        xAmount, yAmount = -0.5, -0.5

    elif xAmount > 0.5 and yAmount < -0.5: # mouse is in bottom right quadrant
        xAmount, yAmount = -0.5, -0.5
    
    else: # mouse is in normal boundaries
        return xAmount, yAmount

def return_mouse_100_pos(x, y):
    if x > 256 and x < 256 + 44 and y > 256 and y < 256 + 44:
        print(0)
    else:
        print(get_mouse_from_middle(x, y))





def main_loop():
    global screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)
    draw_background(screen)

    mousex, mousey = pygame.mouse.get_pos()
    return_mouse_100_pos(mousex, mousey)

    # Update the display
    pygame.display.flip()

while True:
    main_loop()

