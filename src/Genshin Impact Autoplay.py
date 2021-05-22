import pyautogui
import re
import time
import os

#First filter lyrics with combo keys, single keys and space pause
def lyricsfinder(lyrics):
    ls = []
    for rows in lyrics:
        rows = rows.replace('\n', ' ')
        ls.append(re.findall(r'[\w\s]+', rows))
    return ls

#Autoplay via simulating pressing keys on keyboard
def autoplay(keys, t_pause, t_single, t_combo):
    #Delay of pause
    if (keys == ' '):
        return time.sleep(t_pause)
                
    #Delay of single key press
    elif (len(keys) == 1):
        return pyautogui.press(keys), time.sleep(t_single)
        
    #Delay of combo keys press
    elif (len(keys) > 1 and not ' ' in keys):
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

def main():
    check = False
    while (check == False):
        try:
            with open(input('Music name: '), 'r') as f:
                lyrics = f.readlines()
            check = True
        except:
            print('Name input error, please retry')
            pass

    try:
        print('Press 1 to set delay time, 2 to keep defalt')
        if (eval(input()) == 1):
            t_pause = eval(input('Please set pause delay time(s): '))
            t_single = eval(input('Please set single key delay time(s): '))
            t_combo = eval(input('Please set combo keys delay time(s): '))
        else:
            t_pause = 0.1
            t_single = 0.07
            t_combo = 0.08
    except:
        print('Input error')

    try: 
        print('{0:=^20}'.format('Start'))
        time.sleep(3)
        for row in lyricsfinder(lyrics):
            for keys in row:
                autoplay(keys, t_pause, t_single, t_combo)
        print('{0:=^20}'.format('End'))
        os.system('pause')
    except:
        print('Format of lyrics is wrong')

if __name__ == '__main__':
    main()

    