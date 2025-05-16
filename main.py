from sheets_clients import get_sheets_client
from collector import collect_names
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    client = get_sheets_client()
    sheet_name = os.getenv("GOOGLE_SHEET_NAME")
    worksheet_name = os.getenv("GOOGLE_SHEET_WORKSHEET")

    sheet = client.open(sheet_name).worksheet(worksheet_name)
    names = collect_names(sheet)

    print("Nomes encontrados:", names)

if __name__ == "__main__":
    main()