import pyautogui
import time

enter = input("Welcome to the pyautogui autoclicker! \nPress enter to continue!")
user = int(input("Amount of Clicks: "))
click = str(input("Type of click(left or right)(must be exact): "))
speed = float(input("Interval per click(can be decimals): "))
print(
    click + " clicking will start clicking " + str(user) + " times in 5 seconds at the interval of " + str(speed) + ".")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(click + " clicking for " + str(user) + "times at the interval of " + str(speed) + "has started!")
pyautogui.click(clicks=user, interval=speed, button=click)
print("Thank you for using the pyautogui autoclicker!")
