import dropbox
class Transferdata:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)   
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    accessToken = 'sl.A2KPDgQ5V7tT14VBGNkjEHD1lHx6DdjKqkSvke7v3Emqs0amki41anvQtm1JyHhZdZqhE195Jdr0T9c0_jw3RGWo1qyhiQWH53ttsleHX5i54YEIvNKEv0AmFqH-92BiU0ft3SVb'
    transferData = Transferdata(accessToken)
    file_from = 'C:/Users/Lenovo/Desktop/python/102.py'
    file_to = '/102pythonfile2/102.py'
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()