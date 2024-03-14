import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Square")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Square properties
square_size = 50
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2
square_speed = 5

# Movement encoding
MOVEMENTS = {
    pygame.K_w: 0b1000,
    pygame.K_a: 0b0100,
    pygame.K_s: 0b0010,
    pygame.K_d: 0b0001
}

# Record movements
movements_record = []

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the square
    pygame.draw.rect(screen, BLACK, (square_x, square_y, square_size, square_size))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    movement = 0
    for key, value in MOVEMENTS.items():
        if keys[key]:
            movement |= value

    # Add the movement to the record
    movements_record.append(movement)

    # Apply movement
    if keys[pygame.K_w]:
        square_y -= square_speed
    if keys[pygame.K_s]:
        square_y += square_speed
    if keys[pygame.K_a]:
        square_x -= square_speed
    if keys[pygame.K_d]:
        square_x += square_speed

    # Boundary checking
    square_x = max(0, min(square_x, screen_width - square_size))
    square_y = max(0, min(square_y, screen_height - square_size))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Write movements to a file
with open("movements.txt", "w") as file:
    for movement in movements_record:
        file.write(format(movement, '04b') + "\n")

# Quit pygame
pygame.quit()
sys.exit()
