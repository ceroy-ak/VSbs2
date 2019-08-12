from win10toast import ToastNotifier
import pyautogui
import time
import cv2
import numpy


flag = True
img = ""
img2 = ""
location = "D:\image"
x = 0
toaster = ToastNotifier()
toaster.show_toast("VSbs2", "Service is Starting, you have 10 seconds")
time.sleep(11)
print("Main Running")
pagesToPrint = 3
while x < pagesToPrint:
    time.sleep(5)
    p1 = pyautogui.screenshot(region=(637, 107, 702, 894))
    p1.save(location + str(x) + ".png")
    x += 1
    img = img2
    img2 = x
    pyautogui.press('right')
    if x % 10 == 0:
        op1 = location + str(img) + ".png"
        op2 = location + str(img2) + ".png"
        chk = cv2.imread(op1, 0)
        chk2 = cv2.imread(op2, 0)
        diff = cv2.subtract(chk,chk2)
        if numpy.count_nonzero(diff) > 10:
            toaster.show_toast("VSbs2", "Duplication Error")
            break


toaster.show_toast("VSbs2", "Service has Ended: Enjoy!!")
