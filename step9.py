# (c) 2022 - 2026 Open Risk (https://www.openriskmanagement.com)

import pymrio

io = pymrio.IOSystem()

"""

Using a public EEIO database (OECD-ICIO)
Step 9 of the Academy Course [SFI32064](https://www.openriskacademy.com/course/view.php?id=64)


"""

oecd_folder_v2021 = "./oecd21"
# log_2021 = pymrio.download_oecd(storage_folder=oecd_folder_v2021,  years=[2020])
# print(log_2021)

oecd20 = pymrio.parse_oecd(path=oecd_folder_v2021, year=2020)

# Get the labels of sectors 45
# sectors = oecd20.get_sectors()
# print(len(sectors))
"""
['A01_02', 'A03', 'B05_06', 'B07_08', 'B09', 'C10T12', 'C13T15', 'C16', 'C17_18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31T33', 'D', 'E', 'F', 'G', 'H49', 'H50', 'H51', 'H52', 'H53', 'I', 'J58T60', 'J61', 'J62_63', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
"""
# print(list(sectors))

# Get the labels of regions 77
# regions = oecd20.get_regions()
# print(len(regions))
"""
['ARG', 'AUS', 'AUT', 'BEL', 'BGD', 'BGR', 'BLR', 'BRA', 'BRN', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COL', 'CRI', 'CYP', 'CZE', 'DEU', 'DNK', 'EGY', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HKG', 'HRV', 'HUN', 'IDN', 'IND', 'IRL', 'ISL', 'ISR', 'ITA', 'JOR', 'JPN', 'KAZ', 'KHM', 'KOR', 'LAO', 'LTU', 'LUX', 'LVA', 'MAR', 'MEX', 'MLT', 'MMR', 'MYS', 'NGA', 'NLD', 'NOR', 'NZL', 'PAK', 'PER', 'PHL', 'POL', 'PRT', 'ROU', 'ROW', 'RUS', 'SAU', 'SEN', 'SGP', 'SVK', 'SVN', 'SWE', 'THA', 'TUN', 'TUR', 'TWN', 'UKR', 'USA', 'VNM', 'ZAF']
"""
# print(list(regions))

# [3465 rows x 3465 columns]
# print("Z Table (Industry Transactions):\n", oecd20.Z, "\n")
# print(oecd20.Z.columns)

print(oecd20.Z.index)

# Isolate a region
df1 = oecd20.Z.xs("DEU", level='region', axis=1, drop_level=True)
df2 = df1.xs("DEU", level='region', axis=0, drop_level=True)

# Isolate a sector
series1 = df2.loc[:, ['K']]
series2 = df2.loc[['K'], :].transpose()
print(series2)

