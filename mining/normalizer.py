class Normalizer:
    def get(self, university, sheet, i):
        if university == 'ufsc':
            return {
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

    def value(self, row, i):
        return row[i].value