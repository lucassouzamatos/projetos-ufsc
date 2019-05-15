import os
import xlrd

from _database_ import Database
from normalizer import Normalizer

class Migrate:
    def __init__(self, doc):
        data = xlrd.open_workbook(doc)
        sheet = data.sheet_by_index(0)

        for item in self.normalizer(sheet):
            Database().insert('projetos', item)

    def normalizer(self, sheet):
        for i in range(sheet.nrows):
            yield Normalizer().get('ufsc', sheet, i)
