import os
import unittest
import requests
import json
import curlify

from selenium import webdriver


class BitbarSeleniumSample(unittest.TestCase):

    def setUp(self):
        #
        # IMPORTANT: Set the following parameters according to your needs.
        # You can use Capabilities creator:
        # https://cloud.bitbar.com/#public/capabilities-creator
        # Please mind bitbar_apiKey is required and can be found at
        # https://cloud.bitbar.com/#user/my-account (My Integrations > API Access)
        #

        # user-customizable parameters start here
        capabilities = {
        	'platform': 'Linux',
        	'osVersion': '18.04',
        	'browserName': 'firefox',
        	'version': '100',
        	'resolution': '2560x1920',
        	'bitbar_apiKey': '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6',
        }

        # user-customizable parameters end here

        self.screenshot_dir = os.getcwd() + '/'

        self.apiKey = '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6'

        self.driver = webdriver.Remote(command_executor='https://us-west-desktop-hub.bitbar.com/wd/hub',
                                       desired_capabilities=capabilities)


    def test_sample(self):
        # check page title
        test_url = 'https://bitbar.github.io/web-testing-target/'
        self.driver.get(test_url)
        expected_title = 'Bitbar - Test Page for Samples'
        assert self.driver.title == expected_title, 'Wrong page title'
        print(self.driver.title)
        self.driver.get_screenshot_as_file(self.screenshot_dir + '/' + 'home.png')

        # session_ID
        print("session ID = ", self.driver.session_id)

        #get all necessary IDs of current session
        response = requests.get('https://us-west-desktop-hub.bitbar.com/sessions/' + self.driver.session_id, auth=(self.apiKey, '')).json()
        print("Printing Session Information")
        print(json.dumps(response, indent=4, sort_keys=True))
        deviceRunID = str(response["deviceRunId"])
        deviceSessionID = str(response["deviceRunId"])
        projectID = str(response["projectId"])
        RunId = str(response["testRunId"])

        
        # get device session ID
        # response = requests.get('https://cloud.bitbar.com/api/v2/users/74675610/projects/' + projectID + '/runs/' +
        #     RunId + '/device-sessions/', auth=(self.apiKey, '')).json()
        # print("Printing what we hope is Device Session Stuff")
        # print(json.dumps(response, indent=4, sort_keys=True))
        # print("deviceSessionID = ", deviceSessionID)
        # print("Driver ID? = ", str(response["deviceRunId"]))
        
        # try to get a screenshot from the API
        response = requests.get('https://cloud.bitbar.com/api/v2/users/74675610/projects/' + projectID + '/runs/' + RunId + '/device-sessions/' + deviceSessionID + '/screenshots', auth=(self.apiKey, ''))
        print(curlify.to_curl(response.request))
        
        #print(json.dumps(response, indent=4, sort_keys=True))
        shots = {'file': open('home.png', 'rb')}
        #requests.post('https://cloud.bitbar.com/api/v2/device-sessions/' + deviceSessionID + '/output-file-set/files?name=home3.png', auth=(self.apiKey, ''))
        response = requests.post('https://cloud.bitbar.com/api/v2/device-sessions/' + deviceSessionID + '/output-file-set/files?name=home.png', files=shots, auth=(self.apiKey, ''))
        print("Printing Response from file upload", response)
        
        # curl.exe -X 'POST' `
        # 'https://cloud.bitbar.com/api/v2/device-sessions/7287652/output-file-set/files?name=home.png' `
        # -H 'accept: */*' `
        # -H 'authorization: Basic MFQ2Rzl5UzNtN2hjNjl2NlhZS0preXZlSHdSN0tldjY6' `
        # -H 'Content-Type: multipart/form-data' `
        # -F 'file=@home.png;type=image/png'        

        #self.driver.implicitly_wait(60)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
