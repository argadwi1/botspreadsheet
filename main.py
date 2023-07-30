import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Fungsi untuk membaca data dari sel tertentu di Google Spreadsheet
def read_data_from_cell(spreadsheet_id, sheet_name, cell):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    data = sheet.acell(cell).value
    return data

# Fungsi untuk menulis data ke sel tertentu di Google Spreadsheet
def write_data_to_cell(spreadsheet_id, sheet_name, cell, data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    sheet.update_acell(cell, data)

# Contoh penggunaan fungsi untuk membaca dan menulis data di Google Spreadsheet
spreadsheet_id = "your_spreadsheet_id"
source_sheet_name = "Sheet1"
source_cell = "A1"

destination_sheet_name = "Sheet2"
destination_cell = "B2"

data_to_copy = read_data_from_cell(spreadsheet_id, source_sheet_name, source_cell)
write_data_to_cell(spreadsheet_id, destination_sheet_name, destination_cell, data_to_copy)

print("Data berhasil diambil dari", source_sheet_name, "sel", source_cell, "dan ditulis ke", destination_sheet_name, "sel", destination_cell)
