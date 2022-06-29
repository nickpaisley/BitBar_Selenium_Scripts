import requests
import httpx

apiKey = '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6'
headers = {
    'accept': '*/*',
    'authorization': 'Basic MFQ2Rzl5UzNtN2hjNjl2NlhZS0preXZlSHdSN0tldjY6',
    # requests won't add a boundary if this header is set when you pass files=
    #'Content-Type': 'multipart/form-data',
}

params = {
    'name': 'home.png',
}

files = {
    #'file': open('home.png;type=image/png', 'rb'),
    'file': open('home.png', 'rb'),
}

# this request works, but I have to use Basic auth with that wierd key I came up with
#response = httpx.post('https://cloud.bitbar.com/api/v2/device-sessions/7288525/output-file-set/files?name=home.png', headers=headers, files=files)

# this request works with the apiKey because of the 'me'...WHY!?!??!
response = httpx.post('https://cloud.bitbar.com/api/v2/me/device-sessions/7288525/output-file-set/files?name=home.png', files=files, auth=(apiKey, ''))



print('response', response)