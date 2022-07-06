# Please visit http://selenium-python.readthedocs.io/ for detailed installation and instructions
# Getting started: http://docs.seleniumhq.org/docs/03_webdriver.jsp
# API details: https://github.com/SeleniumHQ/selenium#selenium

# Requests is the easiest way to make RESTful API calls in Python. You can install it by following the instructions here:
# http://docs.python-requests.org/en/master/user/install/

import unittest
from selenium import webdriver
import requests
import os
import httpx


class BasicTest(unittest.TestCase):
    def setUp(self):

        #get rid of the old way of doing auth with just an API key
        
        self.apiKey = '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6'

        self.api_session = requests.Session()

        self.test_result = None
        
        self.screenshot_dir = os.getcwd() + '/screenshots'

        self.screenshotName1 = 'SS1.png'

        #old platformName has been split into platformName and osVersion
        capabilities = {
        'bitbar_apiKey': '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6',
        'platform': 'Linux',
        'osVersion': '18.04',
        'browserName': 'firefox',
        'version': '101',
        'resolution': '2560x1920',
    }


        # start the remote browser on our server
        self.driver = webdriver.Remote(
            desired_capabilities=capabilities,
            #the hub is changed, also not sending the user and pass through the hub anymore
            #US hub url: https://appium-us.bitbar.com/wd/hub
            command_executor="https://us-west-desktop-hub.bitbar.com/wd/hub" #EU hub url
        )

        self.driver.implicitly_wait(20)

    def test_CBT(self):
        # We wrap this all in a try/except so we can set pass/fail at the end
        try:
            # load the page url
            print('Loading Url')
            self.driver.get('http://crossbrowsertesting.github.io/selenium_example_page.html')

            # maximize the window - DESKTOPS ONLY
            #print('Maximizing window')
            #self.driver.maximize_window()
            
            #check the title
            print('Checking title')
            self.assertEqual("Selenium Test Example Page", self.driver.title)

            # take a screenshot and save it locally
            print("Taking a Screenshot")
            self.driver.get_screenshot_as_file(self.screenshot_dir + '/' + self.screenshotName1)

            # change pass to SUCCEEDED
            self.test_result = 'SUCCEEDED'

        except AssertionError as e:

            # delete cbt api calls
  
            # change fail to FAILED
            self.test_result = 'FAILED'
            raise
    def uploadScreenshot(self):

            params = {
                'name': self.screenshotName1,
            }
            files = {
                #'file': open('home.png;type=image/png', 'rb'),
                'file': open(self.screenshot_dir + '/' + self.screenshotName1, 'rb'),
            }

            # this request works, but I have to use Basic auth with that wierd key I came up with
            #response = httpx.post('https://cloud.bitbar.com/api/v2/device-sessions/7288525/output-file-set/files?name=home.png', headers=headers, files=files)
            print("Uploading our Screenshot!")
            # this request works with the apiKey because of the 'me'...WHY!?!??!
            #response = httpx.post('https://cloud.bitbar.com/api/v2/me/device-sessions/' + deviceRunID + '/output-file-set/files', params=params, files=files, auth=(self.apiKey, ''))
            response = httpx.post('https://cloud.bitbar.com/api/v2/me/projects/' + projectID + '/runs/' + RunId + '/device-sessions/' + deviceRunID + 
            '/output-file-set/files', params=params, files=files, auth=(self.apiKey, ''))
            
            if response.status_code == 201:
                print("Screenshot Uploaded Successfully!")
            else:
               print("Whoops, something went wrong uploading the screenshot.")

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        if self.test_result is not None:
            #get all necessary IDs of current session
            response = requests.get('https://us-west-desktop-hub.bitbar.com/sessions/' + self.driver.session_id, auth=(self.apiKey, '')).json()
            deviceRunID = str(response["deviceRunId"])
            projectID = str(response["projectId"])
            RunId = str(response["testRunId"])

            # Here we make the api call to set the test's score
            requests.post('https://cloud.bitbar.com/api/v2/me/projects/' + projectID + '/runs/' +
            RunId + '/device-sessions/' + deviceRunID, params={'state': self.test_result},
            auth=(self.apiKey, ''))

            # let's take our locally saved screenshot and push it back to BB
            # headers = {
            # 'accept': '*/*',
            # 'authorization': 'Basic MFQ2Rzl5UzNtN2hjNjl2NlhZS0preXZlSHdSN0tldjY6',
            # # requests won't add a boundary if this header is set when you pass files=
            # #'Content-Type': 'multipart/form-data',
            # }
            

        
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')