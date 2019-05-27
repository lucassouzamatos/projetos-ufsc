class Normalizer:
    def get(self, university: str, sheet: str, i: str):
        if university == 'ufsc':
            return {
                "start":        self.value(sheet.row(i), 0),        
                "finish":       self.value(sheet.row(i), 1),        
                "status":       self.value(sheet.row(i), 2),        
                "title":        self.value(sheet.row(i), 3),       
                "describe":     self.value(sheet.row(i), 4),       
                "coordinator":  self.value(sheet.row(i), 5),        
                "contact":      self.value(sheet.row(i), 6),
                "department":   self.value(sheet.row(i), 7),
                "participants": self.value(sheet.row(i), 8),
                "funders":      self.value(sheet.row(i), 9),
                "total":        self.convertToFloat(self.value(sheet.row(i), 10))
            }

    def value(self, row, i):
        value = row[i].value
        value = value.split('...', 1)[-1]

        a,b = value[:int(len(value)/2)], value[int(len(value)/2):]
        if a == b:
            return a 

        return value

    def convertToFloat(self, value: str) -> float:
        try:
            toFloat = float(value.replace('.', '').replace(',', '.'))
            return toFloat
        except ValueError:
            return value