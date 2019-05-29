import os
import xlrd

from utils.database import Database

PROJECTS_DOC = './research/docs/data.xls'

def run():
    data = xlrd.open_workbook(PROJECTS_DOC)
    sheet = data.sheet_by_index(0)

    for item in normalize(sheet):
        Database().insert(item['department'], item)

def normalize(sheet: str):
    for i in range(1, sheet.nrows):
        yield {
            "start":        value(sheet.row(i), 0),        
            "finish":       value(sheet.row(i), 1),        
            "status":       value(sheet.row(i), 2),        
            "title":        value(sheet.row(i), 3),       
            "describe":     value(sheet.row(i), 4),       
            "coordinator":  value(sheet.row(i), 5),        
            "contact":      value(sheet.row(i), 6),
            "department":   value(sheet.row(i), 7),
            "participants": value(sheet.row(i), 8),
            "funders":      value(sheet.row(i), 9),
            "total":        convertToFloat(value(sheet.row(i), 10))
        }

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