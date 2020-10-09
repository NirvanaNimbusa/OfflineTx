from urllib.parse import urlparse, parse_qs
from flask import Flask, request, json, Response
import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(r'FULL PATH\client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("OfflineTx").sheet1

all = sheet.get_all_values()
index = len(all) + 1

app = Flask(__name__)

@app.route('/offlinetx', methods=['POST'])

def savedata():
    s = request.data
    t = parse_qs(s)
    flag = 0

    #row = [t['sender'][0],t['content'][0]]
    row = ["+911234567891","START TEST WORDS",flag]

    if "START" in row[1]:
        sheet.insert_row(row, index)
    elif "END" in row[1]:
        cell = sheet.find("0") # check if FLAG is 0

        num = sheet.cell(cell.row, 1).value
        #if (num==t['sender'][0]):
        if (num=="+911234567891"):
        #sheet.update_cell(cell.row, 2, sheet.cell(cell.row, 2).value + t['content'][0])
        sheet.update_cell(cell.row, 2, sheet.cell(cell.row, 2).value + " TEST WORDS END")
        sheet.update_cell(cell.row, 3, "1") # Update FLAG


    else:
        cell = sheet.find("0") # check if FLAG is 0

        num = sheet.cell(cell.row, 1).value
        #if (num==t['sender'][0]):
        if (num=="+911234567891"):
            #sheet.update_cell(cell.row, 2, sheet.cell(cell.row, 2).value + t['content'][0])
            sheet.update_cell(cell.row, 2, sheet.cell(cell.row, 2).value + " MORE TEST WORDS")


    return Response(json.dumps(t), mimetype='application/json')


if  __name__ == '__main__':
    app.run(debug=True)
