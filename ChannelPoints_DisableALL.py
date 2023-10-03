import webbrowser
import pyautogui
import pyperclip
import time
import os

url = "https://www.twitch.tv/popout/lucypyre/reward-queue"
webbrowser.open(url, new=0, autoraise=True)
time.sleep(3)
repeats = 29
currentrepeat = 0
tabnum = 4
tabcurrent = 0
Click_variable_x = 45 
Click_variable_y = 68
pyautogui.press('f11')
time.sleep(0.1)
pyautogui.moveTo(45, 183)
while currentrepeat < repeats:
    
    # while tabcurrent<tabnum:
    #     pyautogui.press('tab')
    #     tabcurrent = tabcurrent+1
    # tabcurrent = 0
    # pyautogui.press('enter')
    if currentrepeat == 16:
        pyautogui.moveTo(45, 407)
        pyautogui.scroll(-5000, x=50, y=407)
        time.sleep(0.2)
        Click_variable_y = 374    
    pyautogui.doubleClick(x=Click_variable_x, y=Click_variable_y)
    pyautogui.rightClick(x=383, y=24)
    pyautogui.press('up')
    pyautogui.press('enter')
    #time.sleep(0.5 )
    pyautogui.click(x=1787, y=567)
    pyautogui.click(x=1589, y=594)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite('checked')
    pyautogui.doubleClick(x=1498, y=635)
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    #time.sleep(0.5)
    if text == 'false':
        pyautogui.moveTo(386, 21)
        pyautogui.click(x=386, y=21)
    if currentrepeat == 0:
        pyautogui.doubleClick(x=Click_variable_x, y=Click_variable_y)
        pyautogui.rightClick(x=383, y=24)
        pyautogui.press('up')
        pyautogui.press('enter')
        #time.sleep(0.5 )
        pyautogui.click(x=1787, y=567)
        pyautogui.click(x=1589, y=594)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite('checked')
        pyautogui.doubleClick(x=1498, y=635)
        pyautogui.hotkey('ctrl', 'c')
        text = pyperclip.paste()
        #time.sleep(0.5)
        if text == 'false':
            pyautogui.moveTo(386, 21)
            pyautogui.click(x=386, y=21)

                                                                                              
    Click_variable_y = Click_variable_y + 56
    currentrepeat = currentrepeat+1
    
