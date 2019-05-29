import os
import xlrd

from utils.database import Database

PROJECTS_DOC = './research/docs/data.xls'

def run():
    data = xlrd.open_workbook(PROJECTS_DOC)
    sheet = data.sheet_by_index(0)

    for item in normalize(sheet):
        Database().insert('department', item)

def normalize(sheet: str):
    departments = set()
    for i in range(1, sheet.nrows):
        if sheet.row(i)[7].value not in departments:
            departments.add(sheet.row(i)[7].value)

            yield { 
                "name": sheet.row(i)[7].value 
            } 