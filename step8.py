import numpy as np
import pandas as pd
import pymrio

io = pymrio.IOSystem()

"""

An actual IO model (US 2003 Aggregated Data)
Step 8 of the Academy Course [SFI32064](https://www.openriskacademy.com/course/view.php?id=64)


"""

sectors = ['Agriculture',
           'Mining',
           'Construction',
           'Manufacturing',
           'Transportation',
           'Services',
           'Other']
regions = ['US']

# create a pandas multi-index and give names to the two index components
A_multiindex = pd.MultiIndex.from_product([regions, sectors], names=[u'region', u'sector'])

A = pd.DataFrame(
    data=np.array([[.2008, .0000, .0011, .0338, .0001, .0018, .0009],
                   [.0010, .0658, .0035, .0219, .0151, .0001, .0026],
                   [.0034, .0002, .0012, .0021, .0035, .0071, .0214],
                   [.1247, .0684, .1801, .2319, .0339, .0414, .0726],
                   [.0855, .0529, .0914, .0952, .0645, .0315, .0528],
                   [.0897, .1668, .1332, .1255, .1647, .2712, .1873],
                   [.0093, .0129, .0095, .0197, .0190, .0184, .0228]]),
    index=A_multiindex,
    columns=A_multiindex
)

categories = ['final demand']

fd_multiindex = pd.MultiIndex.from_product(
    [regions, categories], names=[u'region', u'category'])

Y = pd.DataFrame(
    data=np.array([[1.2], [0], [0], [6.8], [0], [0], [0]]),
    index=A_multiindex,
    columns=fd_multiindex)

io.A = A
io.Y = Y

# Calculate the missing components of the IO System
io.calc_all()


# Report
print("Z Table (Industry Transactions):\n", io.Z, "\n")
print("Y Table (Demand): \n", io.Y, "\n")
print("x Vector (Total Output): \n", io.x, "\n")
print("A Table (Normalized Transactions): \n", io.A, "\n")
print("L Table (Leontief Inverse): \n", io.L, "\n")

# Solution to exercise
print(io.L.values.sum(axis=0))
