import numpy as np
import pandas as pd
import pymrio

io = pymrio.IOSystem()

"""

Working with Extensions

Step 5 of the Academy Course [SFI32064](https://www.openriskacademy.com/course/view.php?id=64)


"""

sectors = ['S1', 'S2']
regions = ['R1']
Z_multiindex = pd.MultiIndex.from_product(
    [regions, sectors], names=[u'region', u'sector'])

Z = pd.DataFrame(
    data=np.array([
        [150, 500],
        [200, 100]]),
    index=Z_multiindex,
    columns=Z_multiindex
)

categories = ['final demand']
fd_multiindex = pd.MultiIndex.from_product(
    [regions, categories], names=[u'region', u'category'])

Y = pd.DataFrame(
    data=np.array([[350], [1700]]),
    index=Z_multiindex,
    columns=fd_multiindex)

io.Z = Z
io.Y = Y

F = pd.DataFrame(
    data=np.array([[650, 1400]]),
    index=['Value Added'],
    columns=Z_multiindex)


factor_input = pymrio.Extension(name='Value Added', F=F)
io.factor_input = factor_input
io.factor_input.unit = pd.DataFrame(data=['USD'], index=F.index, columns=['unit'])

io.calc_all()

print(factor_input.F)


