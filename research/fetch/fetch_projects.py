import os
import xlrd

from utils.database import Database

PROJECTS_DOC = './docs/data.xls'

def run():
    data = xlrd.open_workbook(PROJECTS_DOC)
    sheet = data.sheet_by_index(0)

    for item in normalize(sheet):
        Database().insert('projects', item)

def normalize(sheet: str):
    for i in range(1, sheet.nrows):
        yield {
            "start":         value(sheet.row(i), 0),
            "finish":        value(sheet.row(i), 1),
            "status":        value(sheet.row(i), 2),
            "title":         value(sheet.row(i), 3),
            "describe":      value(sheet.row(i), 4),
            "coordinator":   value(sheet.row(i), 5),
            "contact":       value(sheet.row(i), 6),
            "department_id": department(sheet.row(i)),
            "participants":  value(sheet.row(i), 8),
            "funder_id":     funder(sheet.row(i)),
            "total":         convertToFloat(value(sheet.row(i), 10))
        }

def department(row):
    value = row[7].value
    selected = Database().select("departments", { "name": value })
    if not selected:
        Database().insert("departments", { "name": value })
        department(row)
    return selected["_id"]

def funder(row):
    value = row[9].value
    value = value.split('-', 1)[0].replace('[', '')
    selected = Database().select("funders", { "name": value })
    if not selected:
        Database().insert("funders", { "name": value })
        funder(row)
    return selected["_id"]

def value(row, i):
    value = row[i].value
    value = value.split('...', 1)[-1]

    a,b = value[:int(len(value)/2)], value[int(len(value)/2):]

    if a == b:
        return a 

    return value

def convertToFloat(value: str) -> float:
    try:
        toFloat = float(value.replace('.', '').replace(',', '.'))
        return toFloat
    except ValueError:
        return value