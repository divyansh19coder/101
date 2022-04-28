import os
import dropbox 
from dropbox.files 
import WriteMode

class TransferData:
     def __init__(self, access_token):
         self.access_token = access_token

def upload_file(self, file_from, file_to):
    dbx = dropbox.Dropbox(self.access_token)

for filename in files:
    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.BGPBRZBbCyaF9CQPx4NBGX0wsZGaUZgl3-uyNEJC7GQ2JbfqYQKmimrE-zrDWRqHTNytA1FbRbdWGoldeiRCIXaXtGcfarmFv9WN-5HAn1hKi9e3x49Fi8lSknphHQzYhlSUS-pAijmj' 
    transferData = TransferData(access_token),