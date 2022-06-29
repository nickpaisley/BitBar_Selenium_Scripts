import requests


headers = {
    #'authority': 'cloud.bitbar.com',
    'accept': '*/*',
    #'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data',
    #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryDmG5UfHAq4G2b8xY',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_mkto_trk=id:800-TIV-782&token:_mch-bitbar.com-1626100473124-28072; _fbp=fb.1.1627937642985.1335342951; __adroll_fpc=13ba8fe7385c23f9919e35024103038a-1627937643698; vsid=925vr3861139285215577; bfp_sn_rf_b10ce94cf299b167b74a6944e0aec9d4=Direct; bfp_sn_rt_b10ce94cf299b167b74a6944e0aec9d4=1638568580562; _gcl_au=1.1.937636756.1650554685; __ar_v4=%7CXTUIT4L53VGNFLFQJBZ6HZ%3A20220615%3A1%7CJ6YJ7DCZGNA2JKGV6QWMUS%3A20220615%3A1%7C5SHTLYSHKZE2RNHAGFEKY5%3A20220615%3A1; _ga_V50E7S9RPF=GS1.1.1655304174.16.0.1655304174.0; _ga=GA1.2.488662054.1626100473; _gid=GA1.2.1236543255.1656335380; XSRF-TOKEN=3149e35a-e385-4086-86da-7651cd4c6ce3; __Host-SESSION=MzM5ZGRlMzYtMjlkMy00N2Q3LTllMmEtODAxOGY2ZGY5OGQ3',
    # 'origin': 'https://cloud.bitbar.com',
    # 'referer': 'https://cloud.bitbar.com/cloud/swagger-ui.html',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
      'authorization': 'Basic MFQ2Rzl5UzNtN2hjNjl2NlhZS0preXZlSHdSN0tldjY6',
}

params = {
    'name': '?name=home.png',
}

data = '------WebKitFormBoundaryDmG5UfHAq4G2b8xY\r\nContent-Disposition: form-data; name="file"; filename="home.png"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundaryDmG5UfHAq4G2b8xY--\r\n'
files = {'media': open('home.png', 'rb')}
response = requests.post('https://cloud.bitbar.com/api/v2/device-sessions/7288470/output-file-set/files?name=home.png', headers=headers, files=files)
print('response', response)