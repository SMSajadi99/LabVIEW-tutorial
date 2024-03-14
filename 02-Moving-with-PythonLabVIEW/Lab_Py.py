import pygame
import serial

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Square Movement")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Square properties
square_size = 50
square_x, square_y = width // 2 - square_size // 2, height // 2 - square_size // 2
square_speed = 5

# Serial connection
ser = serial.Serial('COM9', 9600)  # Change 'COM3' to your port name

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read serial input
    if ser.in_waiting > 0:
        serial_input = ser.readline().decode().strip()
        if len(serial_input) == 4:
            up, left, down, right = map(int, serial_input)
            if up:
                square_y -= square_speed
            if down:
                square_y += square_speed
            if left:
                square_x -= square_speed
            if right:
                square_x += square_speed

    # Keep square within screen boundaries
    square_x = max(0, min(width - square_size, square_x))
    square_y = max(0, min(height - square_size, square_y))

    # Clear the screen
    screen.fill(WHITE)

    # Draw square
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Close serial connection
ser.close()
pygame.quit()
