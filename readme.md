On June 21st 2022, SmartBear launched web application testing on our unified cloud testing solution that will include both browser and device testing on the BitBar platform! We have listened to our customers and having one product for both web and device testing will better meet your needs.

 

BitBar is a scalable, highly reliable and performant platform with multiple datacenters. On it, you will have access to the latest browsers and devices with additional deployment options to meet your needs, including private cloud and dedicated devices.

 

For more frequently asked questions about the launch of web app testing on BitBar, visit our FAQ. 

 

This Quickstart Guide is intended to walk through the conversion of your existing CrossBrowserTesting Selenium tests to use BitBar! We have updated Selenium hubs and API calls that will require conversion, though little else will be required.

 

As with CrossBrowserTesting, we have sample scripts and a Selenium Capabilities Configurator you may use to build out the specific capabilities for the desired tested device. This tool can be found here.

 

To start conversion, you will need your BitBar API key versus the CrossBrowserTesting Authkey. This is a new method to authenticate the user and to make API calls. 

 

You may find your BitBar API Key in account settings as described here.

 

Most of the Code examples and talking points for conversion are in reference to the CrossBrowserTesting Selenium Sample script that is available here. All code snippets in this article will be in Python.

 

Now that you have your BitBar API Key, let's alter the original Authkey variable with our new BitBar API key located at line 18 in the CrossBrowserTesting sample script. This step is for connection to the BitBar API for processes such as taking screenshots and setting the status of your tests.

# Old CrossBrowser Testing Sample Authkey Variable
    self.authkey  = "<"CrossBrowserTesting Authkey">"
# New Bitbar API Key Variable
    self.apiKey = "<"insert your BitBar API Key here">"
 

Note that we also pass the BitBar API Key along with the Capabilities;

capabilities = {
	'platform': 'Windows',
	'osVersion': '11',
	'browserName': 'chrome',
	'version': '102',
	'resolution': '1920x1080',
	'bitbar_apiKey': '<insert your BitBar API key here>',
}
 

With BitBar we now have four Selenium hub options to chose from. Both US and EU Selenium hubs are available to aid in performance for your location. Separate hubs are also provided depending on the type of device (Desktop vs Mobile) you wish to test against.  You may pick the applicable Desktop or Mobile hub closest to your location and replace your existing hub with the updated URL;

BitBar Desktop Selenium Hubs;
    US_WEST:DESKTOP: https://us-west-desktop-hub.bitbar.com/wd/hub
    EU:DESKTOP: https://eu-desktop-hub.bitbar.com/wd/hub
BitBar Mobile Selenium Hubs;
    US_WEST:MOBILE: https://us-west-mobile-hub.bitbar.com/wd/hub
    EU:MOBILE: https://eu-mobile-hub.bitbar.com/wd/hub
 

start the remote browser on our server
      self.driver = webdriver.Remote
          desired_capabilities=capabilities
          command_executor="https://us-west-desktop-hub.bitbar.com/wd/hub"
 

Now that we have our BitBar API Key, Capabilities and Selenium Hub setup, we can move on to altering our requests for Screenshots and Test Result Status.

 

In the CrossBrowserTesting sample script, we use standalone API requests to create Screenshots. For the BitBar sample scripts, we are doing this with the Selenium driver itself to create the Screenshot and store it locally. Afterwards use the BitBar API to push the locally saved image back to our project.

 

The swagger spec for our BitBar Cloud API can be found here.

 

In line 30 of the BitBar Selenium sample script we set a location to store Screenshots on the local machine. Note, this is setup to store files in a directory called 'Screenshots' in the root folder of your project.

self.screenshot_dir = os.getcwd() + '/screenshots'
 

To retrieve a Screenshot and store it, we perform a 'get_screenshot_as_file' call, as seen on line 45 in the BitBar Selenium example script.

self.driver.get_screenshot_as_file(self.screenshot_dir + '/' + '1_home_page.png')
 

Now we want to to take our Screenshot and push it back to our project in BitBar.

       # Let's take our locally saved screenshot and push it back to BitBar!
       # First we start by declaring the 'params' and 'files' variables to hold our Screenshot name and location.

        params = {
            'name': self.screenshotName1,
        }
        files = {
            'file': open(self.screenshot_dir + '/' + self.screenshotName1, 'rb'),
        }

       # Now we build out our API call to push our locally saved screenshot back to our BitBar Project
        print("Uploading our Screenshot")
        response = httpx.post('https://cloud.bitbar.com/api/v2/me/projects/' + self.projectID + '/runs/' + self.RunId + '/device-sessions/' + self.deviceRunID + 
        '/output-file-set/files', params=params, files=files, auth=(self.apiKey, ''))
            
        # Here we check that our upload was successfull
        if response.status_code == 201:
            print("Screenshot Uploaded Successfully")
        else:
            print("Whoops, something went wrong uploading the screenshot.")
 

The final piece of the puzzle is to set our Test Result Status. We have alternate naming conventions for test results, these are 'Succeeded' and 'Failed' for BitBar vs 'Pass' and 'Fail' for CrossBrowserTesting. 

# CrossBrowserTesting Successful test syntax
self.test_result = 'pass'
# CrossBrowserTesting Failed test syntax
self.test_result = 'fail'

# BitBar Successful test syntax
self.test_result = 'SUCCEEDED'
# BitBar Failed test syntax
self.test_result = 'FAILED'
 

Note that in the snippet provided below, we start by performing Get requests for session information. These requests are sent to the same Selenium Hub we are using for the webDriver, so make sure the hub address is set to same hub used for webDriver. We would recommend to turn this into a variable to avoid having to switch this manually for alternate hubs. These processes are found in the 'tearDown' function of the updated CrossBrowserTesting sample script found here.

#get all necessary IDs of current session
    response = requests.get('https://us-west-desktop-hub.bitbar.com/sessions/' + 
    self.driver.session_id, auth=(self.apiKey, '')).json()
    deviceRunID = str(response["deviceRunId"])
    projectID = str(response["projectId"])
    RunId = str(response["testRunId"])
 

Finally, we set the Test Result with the Post method below using session information retrieved with the Get request above. Note, the URL for the Post request will NOT need to be updated to reflect the specific Selenium hub in use.

# Here we make the api call to set the test's score
            requests.post('https://cloud.bitbar.com/api/v2/me/projects/' + projectID + '/runs/' +
            RunId + '/device-sessions/' + deviceRunID, params={'state': self.test_result},
            auth=(self.apiKey, ''))
 

Now that we have made these changes you are ready to run your test through BitBar!

 

As a summary, we replace our CrossBrowserTesting authKey with the BitBar API Key, set the new Selenium hub address, build new screenshot calls and update the test result function.

 

Quick Reference Documentation;

BitBar Web FAQ.

Complete documentation with code samples in various languages are found here.

Retrieve your BitBar API Key in account settings as described here.

BitBar Selenium Capability Configurator and Sample Scripts are found here.

CrossBrowserTesting Capability Configurator and Sample Scripts are found here.

The Swagger spec for our BitBar Cloud API can be found here.

 

Thanks for reading along, I hope this helps your conversion to BitBar! 

 

Happy Testing!