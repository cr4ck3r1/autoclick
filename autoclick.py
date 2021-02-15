import pyautogui, time
time.sleep(5)
filee = open("word", 'r')
for word in filee:
    pyautogui.typewrite(word)
    pyautogui.press("enter")