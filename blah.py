#get all necessary IDs of current session 
response = requests.get('https://appium.bitbar.com/sessions/' + self.driver.session_id, auth=(self.apiKey, '')).json() 
deviceRunID = str(response["deviceRunId"]) 
projectID = str(response["projectId"]) 
RunId = str(response["testRunId"]) 

# Here we make the api call to set the test's score 
requests.post('https://cloud.bitbar.com/api/v2/me/projects/' + projectID + '/runs/' + 
RunId + '/device-sessions/' + deviceRunID, params={'state': self.test_result}, 
auth=(self.apiKey, ''))