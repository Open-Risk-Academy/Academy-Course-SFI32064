import pymrio

import pandas as pd
import numpy as np

"""

Constructing the Leontief Inverse "by hand"

Step 4 of the Academy Course [SFI32064](https://www.openriskacademy.com/course/view.php?id=64)


"""

# Initialize the system (same as Step 3.2)
io = pymrio.IOSystem()

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
io.calc_all()

I = np.eye(2)
A2 = np.matmul(io.A, io.A)
A3 = np.matmul(A2, io.A)
A4 = np.matmul(A3, io.A)
L_4 = I + io.A + A2 + A3 + A4

print("4-th order approximation of Leontief Inverse\n", L_4)
print("Actual Solution\n", io.L)
