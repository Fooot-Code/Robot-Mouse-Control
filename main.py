import pygame
import sys
import networktables

# Set up the display
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame")

# Image(s?)
img = pygame.transform.scale(pygame.image.load("C:\\Documents\\GitHub\\Robot-Mouse-Control\\joystick.png"), (screen_width, screen_height)).convert()

# NT Table stuff
nt = networktables.NetworkTablesInstance.getDefault()
nt.startClient("127.0.0.1")
table = nt.getTable("Wiimote Joystick") 

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

try:
    wiimote=pygame.joystick.Joystick(0)
except pygame.error: # This bit doesn't seem to work properly.
    print("Joystick not connected.")

wiimote.init()

def wiimote_event_handling(wiimote):
    wiimoteXandY = (round(wiimote.get_axis(0)), round(wiimote.get_axis(1)))
    return wiimoteXandY


def draw_background(screen):
    screen.blit(img, (0, 0))

def get_mouse_from_middle(x, y):
    yPercentFrom00 = y / (screen_height / 2)
    yAmount = 1.0 - yPercentFrom00
    xPercentFrom00 = x / (screen_width / 2)
    xAmount = 1.0 - xPercentFrom00
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
    table.putNumber("Wiimote X", wiimote_event_handling(wiimote)[0])
    table.putNumber("Wiimote Y", wiimote_event_handling(wiimote)[1])

    # Update the display
    pygame.display.flip()

while True:
    main_loop()

