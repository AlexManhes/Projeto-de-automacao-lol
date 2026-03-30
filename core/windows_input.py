import win32api
import win32con
import time


def mover_mouse(x, y):
    win32api.SetCursorPos((x, y))


def clicar():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mover_e_clicar(x, y):
    mover_mouse(x, y)
    time.sleep(0.05)
    clicar()