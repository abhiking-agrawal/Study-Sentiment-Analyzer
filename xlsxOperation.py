from openpyxl import load_workbook
wb = load_workbook(filename='rt-polaritydata/Manualvalidation_weather.xlsx')
ws = wb['Sheet2']

for row in ws.rows:
    for cell in row:
        print(cell.value)