import pandas as pd
import csv
from data import get_amount,get_category,get_date,get_description 
class CSV:
    CSV_FILE='finacial.csv'
    COLUMNS=["date","amount","category","description"]
    @classmethod
    def initalize(cls):
        try:
            pd.read_csv(cls.CSV_FILE)    
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")
def add():
    CSV.initalize()
    date=get_date("Enter the date or enter for todays date(dd-mm-yyyy)")
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)
add()