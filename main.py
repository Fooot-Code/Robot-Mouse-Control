import pygame
import sys
import networktables

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame")

# Image(s?)
img = pygame.transform.scale(pygame.image.load("C:\\Documents\\GitHub\\Robot-Mouse-Control\\joystick.png"), (screen_width, screen_height)).convert()

# NT Table stuff
nt = networktables.NetworkTablesInstance.getDefault()
nt.startClient("127.0.0.1")
table = nt.getTable("Mouse Joystick") 

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_background(screen):
    screen.blit(img, (0, 0))

def get_mouse_from_middle(x, y):
    yPercentFrom00 = y / (screen_height / 2)
    yAmount = 1.0 - yPercentFrom00
    xPercentFrom00 = x / (screen_width / 2)
    xAmount = 1.0 - xPercentFrom00

    # You cant have each axis going more than 50% at any time, so this handles it 
    # if xAmount > 0.5 and yAmount > 0.5: # mouse is in top left quadrant
    #     xAmount, yAmount = 0.8, 0.8
    
    # elif xAmount < -0.5 and yAmount > 0.5: # mouse is in top right quadrant
    #     xAmount, yAmount = -0.8, 0.8

    # elif xAmount < -0.5 and yAmount < -0.5: # mouse is in bottom left quadrant
    #     xAmount, yAmount = -0.8, -0.8

    # elif xAmount > 0.5 and yAmount < -0.5: # mouse is in bottom right quadrant
    #     xAmount, yAmount = -0.8, -0.8

    # No else statement, becuase if it is in normal boundaries, we dont want to do anything to the value    
    return (xAmount, yAmount)

def return_mouse_100_pos(x, y):
    if x > 256 and x < 256 + 44 and y > 256 and y < 256 + 44:
        return (0, 0)
    else:
        return get_mouse_from_middle(x, y)





def main_loop():
    global screen, table

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)
    draw_background(screen)

    mousex, mousey = pygame.mouse.get_pos()
    table.putNumber("Mouse X", return_mouse_100_pos(mousex, mousey)[0])
    table.putNumber("Mouse Y", return_mouse_100_pos(mousex, mousey)[1])

    # Update the display
    pygame.display.flip()

while True:
    main_loop()

