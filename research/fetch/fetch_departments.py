import os
import xlrd

from utils.database import Database

PROJECTS_DOC = './docs/data.xls'

def run():
    data = xlrd.open_workbook(PROJECTS_DOC)
    sheet = data.sheet_by_index(0)

    for item in normalize(sheet):
        Database().insert("departments", item, unique=True)

def normalize(sheet: str):
    for i in range(1, sheet.nrows):
        yield { 
            "name": sheet.row(i)[7].value 
        } 