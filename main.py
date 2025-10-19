
from src.bcv_webscraping.get_bcv_price import get_currency_value_from_bcv
from src.sheet.sheet_api import sheet

#Sheet
SHEET_NAME = "BCV"
bcv_worksheet = sheet.worksheet(SHEET_NAME)

#Escribir precio BCV
bcv_worksheet.update_cell(2, 2, get_currency_value_from_bcv('dolar'))
