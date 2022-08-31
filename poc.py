from turtle import left
import pyautogui as pg
import time
import os
import win32gui
import win32console
import win32con
import threading
pg.FAILSAFE = False

PROCNAME = "explorer.exe"

def kill_explorer():
    os.system("taskkill /f /IM explorer.exe")

def start_explorer():
    os.system("start explorer.exe")
    
def delete_for_everyone():
    pg.click(21, 903)
    pg.typewrite("hello")
    pg.typewrite(["enter"])

consoleWindowHandle = win32console.GetConsoleWindow()

def setOnTop():
    while True:
        win32gui.SetWindowPos(consoleWindowHandle,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE) 
        time.sleep(3)

def main():
    try:
        time.sleep(8)
       

        th = threading.Thread(target=setOnTop, daemon=True).start()

        print("the show begins")
        #time.sleep(10)
        kill_explorer()
        start_explorer()
        w,h = pg.size()
        time.sleep(2)
        pg.click(22, 903)
        time.sleep(5)
        print("ahora haz click")
        pg.click(529, 905,button='right')
        time.sleep(2)
        pg.click(524, 855)
        input("i did the work, i hope...")
    except Exception as e:
        print(e)
    input("adios...")

main()
    
