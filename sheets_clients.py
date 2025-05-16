import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

def get_sheets_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = os.getenv("credentials")
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    return gspread.authorize(creds)