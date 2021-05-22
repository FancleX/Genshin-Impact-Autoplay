import pyautogui
import re
import time

def lyricsfinder(lyrics):
    ls = []
    for rows in lyrics:
        rows = rows.replace('\n', '')
        ls.append(re.findall(r'[\w\s]+', rows))
    return ls

def main():
    try:
        with open(input('Music name: '), 'r') as f:
            lyrics = f.readlines()
            time.sleep(3)
    except:
        print('Name input error')

    try: 
        print('----Start----')
        for row in lyricsfinder(lyrics):
            for keys in row:
                if (keys == ' '):
                    time.sleep(0.01)
                elif (len(keys) == 1):
                    pyautogui.press(keys)
                    time.sleep(0.08)
                elif (len(keys) > 1 and not ' ' in keys):
                    s = []
                    for letter in keys:
                        s.append(letter)
                    pyautogui.press(s)
                    time.sleep(0.1)
                else:
                    ele = []
                    ele = list(keys)
                    for i in ele:
                        if (i == ' '):
                            time.sleep(0.005)
                        else:
                            pyautogui.press(i)
                            time.sleep(0.08)
        print('----End----')
    except:
        print('Format of lyrics is wrong')

if __name__ == '__main__':
    main()

    