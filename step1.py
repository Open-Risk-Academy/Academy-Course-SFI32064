# (c) 2022 - 2026 Open Risk (https://www.openriskmanagement.com)

import pymrio

io = pymrio.IOSystem()

print(type(io))
print(dir(io))
print(io.meta)

E = pymrio.Extension(name="My Extension")

print(type(E))
print(dir(E))

