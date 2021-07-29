import pandas as pd

class pandass:
    def __init__ (self, list):
        self.list = list
        self.df = ''
    def dataframe (self):
        self.df = pd.DataFrame(self.list)
        print(self.df)