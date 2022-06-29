from appium import webdriver
import time
import unittest

desired_cap = {
    'bitbar_apiKey': '0T6G9yS3m7hc69v6XYKJkyveHwR7Kev6',
	'bitbar_device': 'Google Pixel 3 -US',
	'bitbar_app': '',
	'platformName': 'Android',
	'deviceName': 'Android Phone',
	'automationName': 'Appium',
}

def wikiTest():
    # create a webDriver to interact with the device
    driver = webdriver.Remote("https://appium-us.bitbar.com/wd/hub/", desired_cap)

    # we need to reset our app to replicate testing on a fresh BB device
    driver.reset()
    
    time.sleep(15)
    #driver.find_element_by_id('org.wikipedia:id/menu_icon').click()

    #driver.find_element_by_id('org.wikipedia:id/feed_view').click()

    driver.find_element_by_id('org.wikipedia:id/search_container').click()

    driver.find_element_by_id('org.wikipedia:id/search_src_text').send_keys("SmartBear")

    #driver.send_keys.Enter

    # click on first result
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]').click()

    time.sleep(5)
    # title of page "SmartBear Software"
    title = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.TextView[1]')
    titleName = title.text
    print("titleName:", titleName)

    if titleName == 'SmartBear Software':
        print("title matches!")
    else:
        print("title does not match!")

    assert titleName == "SmartBear Software"



wikiTest()