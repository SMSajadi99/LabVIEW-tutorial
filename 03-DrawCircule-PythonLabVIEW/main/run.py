import pygame
import serial

# Initialize Pygame
pygame.init()

'''
    If it receives a "start" command, it enables drawing and clears the screen.
    If it receives a "pause" command, it pauses drawing.
    If it receives a "resume" command, it resumes drawing.
    If it receives a "clear" command, it clears the screen.
'''

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Serial Data Visualization")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up serial communication
ser = serial.Serial('COM30', 9600)  # Change the port and baud rate as needed

# Function to draw circle
def draw_circle(x, y):
    radius = 10
    pygame.draw.circle(screen, BLACK, (x, y), radius)

# Function to clear the screen
def clear_screen():
    screen.fill(WHITE)
    pygame.display.flip()

# Main loop
running = True
drawing_enabled = False
paused = False
clear_screen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ser.in_waiting:
        command = ser.readline().decode().strip()
        if command == "start":
            drawing_enabled = True
            clear_screen()
        elif command == "pause":
            paused = True
        elif command == "resume":
            paused = False
        elif command == "clear":
            clear_screen()

    if drawing_enabled and not paused:
        if ser.in_waiting:
            data = ser.readline().decode().strip()
            try:
                x, y = map(int, data.split(','))
                draw_circle(x, y)
                pygame.display.flip()
            except ValueError:
                pass  # Ignore if data format is incorrect or incomplete

# Close serial connection
ser.close()
pygame.quit()
