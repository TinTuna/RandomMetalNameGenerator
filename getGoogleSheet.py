from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1-OmDNP24Ed2Jfi1Awi954CjApDIvYuwLCw_MC1ph7m0'
RANGE_NAME = '!A3:H62'


def main(YEAR: str):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        # check if token is expiry and refresh if needed
        # open token.json and check expiry
        # TODO

        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=YEAR + RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        arr = []
        for row in values:
            if row[0] != '':
                arr.append([
                        row[0].strip(),
                        row[1].strip(),
                        row[2].strip(),
                        row[3].strip()+' '+YEAR,
                        row[4],
                        row[5],
                        row[6],
                        row[7]
                    ])
        return arr
    except HttpError as err:
        print(err)
