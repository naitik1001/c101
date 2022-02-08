from dropbox.files  import WriteMode
import os.path

import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root,dirs,files in os.walk(fileFrom):
            for fileName in files:
                localPath=os.path.join(root,fileName)
                relativePath  = os.path.relpath(localPath,fileFrom)
                dropboxPath = os.path.join(fileTo,relativePath)
                with open(localPath,'rb')as f:
                    dbx.files_upload(f.read(),dropboxPath,mode=WriteMode('overwrite'))
def main():
    accessToken = "433YlUb03a8AAAAAAAAAAfjqwuaI5F-PFOiZ6l_qogCV2UyDK1Bi2s_e8Fg6Bh_h"
    transferData = TransferData(accessToken) 
    fileFrom = str(input("enter the folder path to transfer"))
    fileTo = input("enter the full path to upload to dropbox")
    transferData.uploadFile(fileFrom,fileTo)
    print("folder has been uploaded succesfully")
main()