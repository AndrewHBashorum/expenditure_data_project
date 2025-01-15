
import pandas as pd


if __name__ == '__main__':
    
    # read by default 1st sheet of an excel file
    df = pd.read_excel('public/Exp.xlsx')

    # for row in df:
    print(df['Total'])