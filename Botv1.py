import pyautogui
import keyboard
import win32api ,win32con

Bitcoin = [229,131,31]
Toicoin = [141,141,141]
Doge = [226,191,73]
Dudecoin = [8,140,215]


def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(536,360,830,420))
    width,height = pic.size

    for x in range(0,width,15):
        achou = 0
        for y in range(0,height,15):
            r,g,b = (pic.getpixel((x,y)))
            #bitcoin
            if r == "rc_items/coinclick_btc.png" and b == 33:
                achou = 1
                click(x+536,y+360)
                break
            #litecoin
            elif r == "rc_items/coinclick_lite.png" and b == 230:
                achou = 2
                click(x+536,y+360)
                break
            #doge
            elif r == "rc_items/coinclick_doge.png" and b == 64:
                achou = 3
                click(x+536,y+360)
                break
            #dashecoin
            elif r == "rc_items/coinclick.dash" and b == 183:
                achou = 4
                click(x+536,y+360)
                break