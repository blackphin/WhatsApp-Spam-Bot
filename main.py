import pyautogui as auto
import time

string = str(input("Enter Spam Word: "))
frequency = int(input("Enter Number of Messages to send: "))
time.sleep(int(input("Enter Delay (in seconds): ")))
for x in range(frequency):
    auto.write(message=string)
    auto.press("enter")
