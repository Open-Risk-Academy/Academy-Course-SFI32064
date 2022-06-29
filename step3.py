import numpy as np
import pandas as pd
import pymrio

"""
Constructing a simple IO table that involves two economic sectors

Step 3 of the Academy Course [SFI32064](https://www.openriskacademy.com/course/view.php?id=64)

"""
# Initialize the system
io = pymrio.IOSystem()

# TWO NON-INTERACTING SECTORS WITH MULTIPLE TYPES OF DEMAND (ADDITIONAL COLUMNS OF Y)

"""
The Z matrix is initialized as a numpy array (2x2) but
stored as a pandas dataframe along an index we create

"""

Z = pd.DataFrame(
    data=np.array([[1, 0], [0, 1]]),
    index=["S1", "S2"],
    columns=["S1", "S2"]
)
Y = pd.DataFrame(
    data=np.array([[1, 0], [0, 1]]),
    index=["S1", "S2"],
    columns=["Y1", "Y2"]
)

"""
The fundamental equation (2.4) is effectively bootstrapped by setting the attributes of the IO system class to the corresponding matrix values via an assignment

x = Zi + Y

"""

io.Z = Z
io.Y = Y

# We are not ready calculate everything that can be calculated
io.calc_all()

# Report
print("Z Table (Industry Transactions):\n", io.Z, "\n")  # input
print("Y Table (Demand): \n", io.Y, "\n")  # input
print("x Vector (Total Output): \n", io.x, "\n")  # x = Z + Y
print("A Table (Normalized Transactions): \n", io.A, "\n")  # A = Z / x
print("L Table (Leontief Inverse): \n", io.L, "\n")  # L = 1 / (I - A)

del io
print(80 * '=')
# Initialize a more complex system
io = pymrio.IOSystem()

# TWO INTERACTING SECTORS

Z = pd.DataFrame(
    data=np.array([[200, 100], [80, 50]]),
    index=["F", "E"],
    columns=["F", "E"]
)
Y = pd.DataFrame(
    data=np.array([[300, 100], [200, 150]]),
    index=["F", "E"],
    columns=["G", "A"]
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
print("L Table (Leontief Inverse): \n", io.L, "\n")  # L = 1 / (I - A)
