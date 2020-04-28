from selenium import webdriver
from selenium.webdriver.common.keys import Keys

### login
usernameCMS = 'nwong'
passwordCMS = 'rqJ4F9mK'


### script for retrieving info from excel file#####

### 
browser = webdriver.Chrome(r'C:\Users\Nicholas\chromedriver.exe')
browser.get('https://prod-cms-gwt.sony.eu/iw-cc/command/iw.ui')
browser.find_element_by_id('iw_user').send_keys(usernameCMS)
browser.find_element_by_id('iw_password').send_keys(passwordCMS)
cmsButton = browser.find_element_by_tag_name('a')
cmsButton.click()


browser.find_element_by_id('fs_location_external').send_keys(usernameCMS)