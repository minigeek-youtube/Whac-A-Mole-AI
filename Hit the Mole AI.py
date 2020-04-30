from ctypes import windll
from pynput.mouse import Controller
from pynput.mouse import Button, Controller
import time
import webbrowser

hdc = windll.user32.GetDC(0)
mouse = Controller()
webbrowser.open('https://www.classicgame.co.uk/game/Whack+a+Mole#')
time.sleep(5)
def wait_until(x, y, operation, colour, wait):
    hdc = windll.user32.GetDC(0)
    if operation == '!':
        while windll.gdi32.GetPixel(hdc, x, y) != colour:
            time.sleep(wait)
    if operation == '=':
        while windll.gdi32.GetPixel(hdc, x, y) == colour:
            time.sleep(wait)

def click_on(x, y, wait):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    time.sleep(wait)

wait_until(601, 555, '!', 107614, 1)

time.sleep(10)
mouse.scroll(0, -13)
time.sleep(1)

click_on(597, 410, 0)

wait_until(1030, 560, '=', 3156775, 2)

time.sleep(10)
mouse.position = (1030, 560)
time.sleep(0.5)
mouse.click(Button.left, 1)

wait_until(657, 401, '!', 16777215, 1)

click_on(652, 390, 1)

click_on(568, 525, 1)

click_on(687 ,460, 0)

start = time.time()
end = start + 60


x_pos = [420, 570, 715, 420, 570, 715, 420, 570, 715,]
y_pos = [310, 310, 310, 435, 435, 435, 560, 560, 560]
colour_mole = [15263718, 10277608]

time.sleep(1)


while time.time() <= end:
    for x in x_pos:
        for y in y_pos:
            if windll.gdi32.GetPixel(hdc, x, y) in colour_mole:
                mouse.position = (x, y)
                mouse.click(Button.left, 1)

mouse.scroll(0, -13)