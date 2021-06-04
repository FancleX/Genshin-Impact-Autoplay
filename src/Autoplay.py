import pyautogui
import time

#Autoplay via simulating pressing keys on keyboard
def autoplay(keys, t_pause, t_single, t_combo):
    #Delay of pause
    if (keys == ' '):
        return time.sleep(t_pause)
                
    #Delay of single key press
    elif (len(keys) == 1):
        return pyautogui.press(keys), time.sleep(t_single)
        
    #Delay of combo keys press
    elif (len(keys) > 1 and ' ' not in keys):
        s = []
        for letter in keys:
            s.append(letter)
        return pyautogui.press(s), time.sleep(t_combo)
                
    #Delay of single key and pause
    else:
        ele = []
        ele = list(keys)
        for i in ele:
            if (i == ' '):
                return time.sleep(t_pause)
            else:
                return pyautogui.press(i), time.sleep(t_single)