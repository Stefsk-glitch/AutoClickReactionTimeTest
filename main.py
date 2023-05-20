import pyautogui
from PIL import Image, ImageDraw
import keyboard

def draw_lines(image, x_start, y_start, x_end, y_end):
    draw = ImageDraw.Draw(image)
    draw.rectangle([(x_start, y_start), (x_end, y_end)], outline="red", width=2)
    del draw

def check_color_change():
    # Get the center coordinates of the screen
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2

    # Define the region to check for color changes
    x_start = center_x - 5  # 10/2
    y_start = center_y - 5  # 10/2
    x_end = center_x + 5
    y_end = center_y + 5

    print("Waitin' for user to press the 'T' key on the keyboard")
    keyboard.wait("T")

    # Get the initial color at the center
    initial_color = pyautogui.pixel(center_x, center_y)

    screenshot = pyautogui.screenshot()

    # Draw lines on the screenshot around the region being checked
    draw_lines(screenshot, x_start, y_start, x_end, y_end)

    screenshot.save("start.png")
    print("Screenshot saved as 'start.png'")

    # Display the screenshot
    # screenshot.show()

    # Continuously check for color changes
    while True:
        # Check the color at the center
        current_color = pyautogui.pixel(center_x, center_y)

        # Check if the color has changed
        if current_color != initial_color:
            print("Changed")
            # Perform a mouse click at the center location
            pyautogui.click(center_x, center_y)
            break

        # Check the color within the defined region
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                if pyautogui.pixel(x, y) != initial_color:
                    print("Changed")
                    # Perform a mouse click at the center location
                    pyautogui.click(center_x, center_y)
                    # Make a new screenshot with the highlighted area
                    screenshot2 = pyautogui.screenshot()
                    draw_lines(screenshot2, x_start, y_start, x_end, y_end)
                    screenshot2.save("end.png")
                    print("Screenshot saved as 'end.png'")
                    return

print("Started")

# Call the function to start checking for color changes
check_color_change()

print("Ended")
