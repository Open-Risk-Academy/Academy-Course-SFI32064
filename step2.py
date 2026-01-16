# (c) 2022 - 2026 Open Risk (https://www.openriskmanagement.com)

import numpy as np
import pandas as pd
import pymrio

"""
Constructing a very simple IO table that involves only one economic sector

Step 2 of the Academy Course [SFI32064](https://www.openriskacademy.com/course/view.php?id=64)

"""

# Initialize the system

io = pymrio.IOSystem()

# SINGLE SECTOR

Z = pd.DataFrame(
    data=np.array([[1]]),  # initialize with value=1
    index=["S1"],
    columns=["S1"]
)
Y = pd.DataFrame(
    data=np.array([[2]]),  # initialize with value=2
    index=["S1"],
    columns=["Y1"]
)

io.Z = Z
io.Y = Y

# Calculate everything that can be calculated
io.calc_all()

# Report
print("Z Table (Industry Transactions):\n", io.Z, "\n")  # input
print("Y Table (Demand): \n", io.Y, "\n")  # input
print("x Vector (Total Output): \n", io.x, "\n")  # x = Z + Y
print("A Table (Normalized Transactions): \n", io.A, "\n")  # A = Z / x
print("B Table (Normalized Transactions): \n", io.B, "\n")  # B = Z / x
print("L Table (Leontief Inverse): \n", io.L, "\n")  # L = 1 / (I - A)
print("G Table (Ghosh Inverse): \n", io.G, "\n")  # L = 1 / (I - B)

# Recalculate everything except the coefficients
io.reset_all_to_coefficients()

# Update the final demand value
Y = pd.DataFrame(
    data=np.array([[1]]),
    index=["S1"],
    columns=["Y1"]
)
io.Y = Y

io.calc_all()

# Report
print("Z Table (Industry Transactions):\n", io.Z, "\n")  # input
print("Y Table (Demand): \n", io.Y, "\n")  # input
print("x Vector (Total Output): \n", io.x, "\n")  # x = Z + Y
print("A Table (Normalized Transactions): \n", io.A, "\n")  # A = Z / x
print("L Table (Leontief Inverse): \n", io.L, "\n")  # L = 1 / (I - A)

print(io.meta)
