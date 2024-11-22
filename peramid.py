import pyautogui

x = int(input())

for i in range(1,x+1):
    for j in range(0,i):
        pyautogui.write('#', interval=0.25)
    pyautogui.press('enter')

