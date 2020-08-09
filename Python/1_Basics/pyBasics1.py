# Python Example Appendix
# Optional extras: Numpy
# TODO: Add interpolated string examples

# === Config Section [DO NOT CHANGE]===
import sys
# === End Config Section ===


# ///////////////////////////////////
# Example_1: ==Hello World==
# Description: In order to make a print statment on python, you only need to use the print statement.

print("Hello World")

# Notes

# ///////////////////////////////////
# Example_2: ==Importing Libraries==
# Description: Sometimes we need to use stuff thats not in your python script by default. This example shows how to import python libraries as well as manipulating their names.

# In this case we use the os library (installed alongside python).
import os
print(os.name)
# You can rename your imports to something else
import multiprocessing as mp

# You can also get a specific object or function from the library
from os import path
print(sys.modules['os.path'])

# ///////////////////////////////////
# Example_3: ==Try - Catch code blocks==
# Description: Using "try:" and "except:" will save you if the code fails in some sections during run time. This is a useful way to handle errors. In this case, we import the optional library Numpy. If you have the library installed (using pip) in the current environment, then you should get "Numpy was imported" in the output of this script as well as "1.0" above that.
np_in = True

try:
   import numpy as np
except ImportError:
   np_in = False
   print("Numpy was not imported")

if np_in:
    print(np.sin(np.pi/2.))
    print("Numpy was imported")
