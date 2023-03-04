
# from openpyxl import load_workbook
# wb = load_workbook('input.xlsx')
# print (wb.sheetnames)
# ws = wb[wb.sheetnames[0]]
# for row in ws.values:
#        for value in row:
#             print(value,"\t",end='')
#             print("")

import pandas as pd

df = pd.read_excel('input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)

data = []

for row in df.iterrows():
    row_data = []
    for value in row[1]:
        row_data.append(value)
    data.append(row_data)

print(data)
