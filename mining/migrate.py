import os
import xlrd

from pymongo import MongoClient
from __env__ import Env

class Migrate:
    def __init__(self, doc):
        data = xlrd.open_workbook(doc)
        sheet = data.sheet_by_index(0)

        client = MongoClient(Env('MONGODB_URL').value)

        for item in self.normalizer(sheet):
            print('Inserted => ', client.ufsc.projetos.insert_one(item).inserted_id)

    def normalizer(self, sheet):
        for i in range(sheet.nrows):
            projeto = {
                "start":       self.value(sheet.row(i), 0),        
                "finish":      self.value(sheet.row(i), 1),        
                "status":      self.value(sheet.row(i), 2),        
                "title":       self.value(sheet.row(i), 3),        
                "describe":    self.value(sheet.row(i), 4),        
                "coordinator": self.value(sheet.row(i), 5),        
                "contact":     self.value(sheet.row(i), 6),
                "department":  self.value(sheet.row(i), 7),
                "funders":     self.value(sheet.row(i), 8),
                "total":       self.value(sheet.row(i), 9)
            }
            yield projeto

    def value(self, row, i):
        return row[i].value