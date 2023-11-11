# 2018 to 2023

import camelot
import matplotlib.pyplot as plt
import pandas as pd
import warnings


def read_stock_pdf_convert_to_dict(file_name:str) -> list:

    column_headers = ['Asset Name', 'Transaction Type', 'Date', 'Notification Date', 'Amount'] 

    tables = camelot.read_pdf(file_name, pages='all', row_tol=20, flavor='stream', columns=['89,255,300,377,437'], split_text=True, strip_text='\n' )
        
    stocks = []

    for table in tables:
        table = table.df
        
        for row in table.itertuples():
            formatted_rows = []
            if row._3 == 'S' or row._3 == 'P':
                formatted_row = (list(row[2:]))
                formatted_rows.append(dict(zip(column_headers, formatted_row)))
        
            stocks.extend(formatted_rows)

    print(stocks)


def read_stocks(files_list):
    warnings.filterwarnings("error")
    for file in files_list:
        try:
            read_stock_pdf_convert_to_dict(file)
        except UserWarning:
            print("Can't use image based file")
            continue