import pyautogui
import time
import math


def main() -> None:
    # Set the radius of the circle in pixels
    radius = 400

    # Set the number of points to draw the circle
    num_points = 60

    # Calculate the angle between each point
    angle = 360 / num_points

    # Set the center of the circle
    center_x, center_y = pyautogui.size()[0] / 2, pyautogui.size()[1] / 2

    # Set the initial position of the mouse to the center of the screen
    pyautogui.moveTo(center_x, center_y)

    # Start a loop to move the mouse around the circle
    for i in range(num_points + 10):
        # Calculate the x and y coordinates of the next point on the circle
        x = center_x + radius * math.cos(math.radians(angle * i))
        y = center_y + radius * math.sin(math.radians(angle * i))

        # Move the mouse to the next point on the circle
        pyautogui.moveTo(x, y)

        # Sleep for a short period of time to give the mouse time to move
        # time.sleep(0.01)

    # Move the mouse back to the center of the screen
    pyautogui.moveTo(center_x, center_y)


if __name__ == '__main__':
    # time.sleep(4)
    main()
