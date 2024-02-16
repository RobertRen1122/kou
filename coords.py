import pyautogui
import time

print("Move your mouse to the first point and press Ctrl-C in this window to capture the coordinates.")

try:
    while True:
        # Print the current position of the mouse cursor
        x, y = pyautogui.position()
        print(f"Current position: x={x}, y={y}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    # Capture the first point's coordinates when Ctrl-C is pressed
    point1 = (x, y)
    print(f"\nFirst point captured: {point1}")

print("Now, move your mouse to the second point and press Ctrl-C again.")

try:
    while True:
        # Print the current position of the mouse cursor
        x, y = pyautogui.position()
        print(f"Current position: x={x}, y={y}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    # Capture the second point's coordinates when Ctrl-C is pressed
    point2 = (x, y)
    print(f"\nSecond point captured: {point2}")

print(f"Coordinates for the two points are {point1} and {point2}.")
