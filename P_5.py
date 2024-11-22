import pyautogui

def draw_pyramid(levels):
    screenWidth, screenHeight = pyautogui.size()
    width, height = 20, 20  # Width and height of each block
    startX = (screenWidth - levels * width) // 2
    startY = screenHeight - levels * height  # Starting position for the pyramid
    currentX = startX
    currentY = startY
    
    for i in range(1, levels + 1):
        for j in range(i):
            pyautogui.drawPoint(currentX, currentY, color='red', size=5)  # Drawing a block
            currentX += width
        currentX = startX - (i * width) // 2
        currentY -= height

if __name__ == "__main__":
    num_levels = int(input("Enter the number of levels for the pyramid: "))
    draw_pyramid(num_levels)



