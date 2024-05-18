
import serial

def read_serial_data(port, baudrate=9600):
    try:
        # Initialize serial connection
        ser = serial.Serial(port, baudrate)
        print(f"Connected to {port} at {baudrate} baud.")

        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            # Split the line by comma
            data = line.split(',')

            # Check if the line contains exactly two values
            if len(data) == 2:
                try:
                    # Convert the values to integers (or floats if necessary)
                    number1 = int(data[0])
                    number2 = int(data[1])
                    print(f"Number 1: {number1}, Number 2: {number2}")
                except ValueError:
                    print(f"Received invalid numbers: {data}")
            else:
                print(f"Received malformed line: {line}")

    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        ser.close()
        print(f"Closed connection to {port}.")


if __name__ == "__main__":
    # Replace 'COM30' with your serial port
    read_serial_data('COM30')
