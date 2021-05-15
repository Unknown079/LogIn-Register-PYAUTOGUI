from os import putenv
import pyautogui
from time import *

"""THE MODULE IS CALLED PYAUTOGUI SO I'M GONNA MAKE A LITTLE 
REGISTER AND LOGIN PROGRAM SO I'LL NOT BE STRUGGLING TO MAKE IT
WITH PYQT5.. :))"""

register1 = pyautogui.prompt("Register your email: ", "REGISTER")
password1 = pyautogui.password("Register your password: ", "REGISTER")

sleep(1)

register2 = pyautogui.prompt("Enter your email: ", "LOGIN")
password2 = pyautogui.password("Enter your password: ", "LOGIN")

while True:
    if register1 != register2:
        pyautogui.alert("Wrong email", "EMAIL")
        register2 = pyautogui.prompt("Enter your email: ", "LOGIN")
    else:
        break

while True:
    if password1 != password2:
        pyautogui.alert("Wrong password", "PASSWORD")
        password2 = pyautogui.password("Enter your password: ", "LOGIN")
    else:
        pyautogui.alert("CONGRATULATIONS, YOU'VE LOGGED SUCCESSFULLY", "CONGRATULATIONS")
        break