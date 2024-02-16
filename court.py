import pyautogui
import datetime
import time

# Coordinates of the two points to click
point1 = (826, 730)  # Example coordinates
point2 = (1206, 954)  # Example coordinates

target_hour = 18  # Example: 1 PM
target_minute = 55  # Example: 5 minutes past the hour
target_second = 25

while True:
    # Get the current time
    now = datetime.datetime.now()
    print(now)
    # Check if it's the target time
    if now.hour == target_hour and now.minute == target_minute and now.second == target_second:
        # Click the first point
        time.sleep(0.05)  # Adjust this value as needed (0.05 to 0.1 seconds)
        pyautogui.click(point1)
        print(f'point 1 clicked: {point1}')
        # Short delay to simulate a slightly faster than human click
        time.sleep(0.05)  # Adjust this value as needed (0.05 to 0.1 seconds)
        
        # Click the second point
        pyautogui.click(point2)
        print(f'point 2 clicked: {point2}')
        
        # Wait until the next minute to avoid multiple clicks in the same minute
        time.sleep(60 - now.second)