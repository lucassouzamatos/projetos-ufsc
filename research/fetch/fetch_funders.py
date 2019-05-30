import os
import xlrd

from utils.database import Database

PROJECTS_DOC = './research/docs/data.xls'

def run():
    data = xlrd.open_workbook(PROJECTS_DOC)
    sheet = data.sheet_by_index(0)

    for item in normalize(sheet):
        Database().insert('funders', item)

"""
    Return { "name": "Lorem" }
"""
def normalize(sheet: str):
    for i in range(1, sheet.nrows):
        name = value(sheet.row(i), 9);
        if (name == True):
            continue

        yield {
            "name": name 
        }

"""
    Convert "[FunderName - 999999]" to "FunderName"
"""
def value(row, i):
    value = row[i].value
    value = value.split('-', 1)[0]
    return value.replace('[', '')
