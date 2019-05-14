import pandas as pd

class Xls:
    def __init__(self):
        print(pd.read_excel('./docs/projetos_.xls'))
