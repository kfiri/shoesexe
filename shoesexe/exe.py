import Shoes.exe to (accurata.py)
import subprocess
import sys
import os

yes1 = "y"
userinput1 = ""

input1_counter = 0
input1_limiter = 1

no2 = "n"
userinput2 = ""




while userinput1 != y and(userinput2 != n):
    if input1_counter < input1_limiter:
        userinput1 = input("reinstall Shoes.exe? Y/N: ")
        input1_counter += 1
    else:
        input1_reset = True

if input1_reset:
    print("invalid syntax/command")
    exit(1)
