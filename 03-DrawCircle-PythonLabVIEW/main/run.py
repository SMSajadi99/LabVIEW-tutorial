import pygame
import serial
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Serial Coordinates Display")

# Set up the serial connection
# Make sure to adjust the serial port and baud rate to match your setup
ser = serial.Serial('COM30', 9600, timeout=1)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# List to store received coordinates
coordinates = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read from the serial port
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode('utf-8').strip()
            print(f"Received data: {data}")  # Print the received data

            if data == "clear":
                # Clear the coordinates list if the "clear" command is received
                coordinates.clear()
                print("Cleared all points.")
            else:
                x_str, y_str = data.split(',')
                x = float(x_str)
                y = float(y_str)

                # Append the coordinates to the list
                coordinates.append((int(x), int(y)))
        except ValueError as e:
            print(f"Error parsing data: {e}")
        except serial.SerialException as e:
            print(f"Serial error: {e}")

    # Clear the window
    window.fill(BLACK)

    # Draw all the saved coordinates
    for coord in coordinates:
        pygame.draw.circle(window, WHITE, coord, 5)

    # Update the display
    pygame.display.flip()

    # Sleep for a short period to avoid maxing out the CPU
    time.sleep(0.01)

# Close the serial port and quit Pygame
ser.close()
pygame.quit()
