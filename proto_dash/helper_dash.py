from os.path import join, dirname
from dotenv import load_dotenv
import pandas as pd
import pygsheets


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client = pygsheets.authorize()

def open_worksheet(spreadsheet_name, worksheet_title):
    """Open spreadsheet and worksheet, creating worksheet with column headers
    if it doesn't exist.

    Args:
        spreadsheet_name (str): Name of Spreadsheet document. Has to exist atm.
        worksheet_title (str): Name of worksheet within spreadsheet.
    Returns:
        wks: a pygsheets.worksheet object

    """
    client = pygsheets.authorize()
    sh = client.open(spreadsheet_name)
    wks = sh.worksheet_by_title(worksheet_title)

    return wks


def worksheet_as_df(spreadsheet_name, worksheet_title):
    wks = open_worksheet(spreadsheet_name, worksheet_title)
    df = wks.get_as_df()
    return df

def get_worksheet_titles(spreadsheet_name):
    sh = client.open(spreadsheet_name)
    worksheet_titles = sh.worksheets()
    return [str(title).split("'")[1] for title in worksheet_titles]

def get_all_worksheets_as_df(spreadsheet_name):

    worksheets = get_worksheet_titles(spreadsheet_name)

    all_df = pd.DataFrame()
    for title in worksheets:
         df = worksheet_as_df(spreadsheet_name,title)
         all_df = all_df.append(df)

    return all_df

def main():
    # testing
    columns = ['timestamp', 'col1', 'name']
    wks = open_worksheet('2019-03_environmentals', 'test1', columns)
    wks.append_table(values=['now', '123434', 'wally'])


if __name__ == '__main__':
    main()
