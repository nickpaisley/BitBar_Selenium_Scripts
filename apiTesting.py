import requests
import unittest
import os
import json




deviceSessionID = "7288532"

class BitbarSeleniumSample(unittest.TestCase):
    
    def test_sample(self):

        self.apiKey = '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6'
        deviceSessionID = "7288532"

        #print(json.dumps(response, indent=4, sort_keys=True))
        #with open(r'C:\Dev\BitBar\screenshotshome.png','rb') as filedata:
        # r = requests.post('https://cloud.bitbar.com/api/v2/device-sessions/' + deviceSessionID + '/output-file-set/files?name=home.png', auth=(self.apiKey, ''), files={'file': filedata})
        
        #shots = {'file': open('home.png', 'rb')}
        #with open(r'C:\Dev\BitBar\screenshots\home.png', 'rb') as filedata:
         #requests.post('https://cloud.bitbar.com/api/v2/device-sessions/' + deviceSessionID + '/output-file-set/files?name=home.png', auth=(self.apiKey, ''), files={'file': filedata})
        #url = ('https://cloud.bitbar.com/api/v2/device-sessions/' + deviceSessionID + '/output-file-set/files?name=home.png')
        #files = ('images', ('home.png', open('home.png', 'rb'), 'image/png' ))
        #text_data = {"key":"value"}
        #files = {'Files[]': ("home.png", open(r"home.png", 'rb'), "image/png", {})}
        
        # #headers = {
        #     "accept": "*/*",
        #     "Authorization" : "Basic MFQ2Rzl5UzNtN2hjNjl2NlhZS0preXZlSHdSN0tldjY6",
        #     "Content-Type": "multipart/form-data"
        # }
        # ss = {
        #     "file":"home.png",
        #     "type":"image/png"
        # }
        # r = requests.post(url, headers=headers, files=files)
        # requests.post(url, headers=headers, files=files)     
        # print("Printing Response from file upload", r)

        # 
        #     r = requests.post(url, files=files, auth=(self.apiKey, ''))
        #     print("Printing Response from file upload", r)

        

        import requests

headers = {
    'accept': '*/*',
    'Content-Type': 'multipart/form-data',
    'authorization': 'Basic MFQ2Rzl5UzNtN2hjNjl2NlhZS0preXZlSHdSN0tldjY6',
}

params = {
    'name': 'home.png',
}

data = 'file': 'home.png'

response = requests.post('https://cloud.bitbar.com/api/v2/device-sessions/7288470/output-file-set/filesfiles?name=home.png', headers=headers, data=data)
print("Printing Response from file upload", response)
if __name__ == "__main__":
    unittest.main(warnings='ignore')