import requests
url = "http://serverAddress:10500"
files = {
    'myFile': open('wavefile.wav', 'rb')
}
session = requests.Session()
req = session.post(url, files=files)
print(req.text)

