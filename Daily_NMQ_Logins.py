### Daily NMQ Logins

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\Users\Nicholas\AppData\Local\Google\Chrome\User")
chrome_options.add_argument('--profile-directory=Profile 1')


##ID and PASSWORD#####################################################################

usernameSF = 'nicholas.wong@sony.com'
passwordSF = 'Nicholas$1234'

usernameNMQticket = 'nicholas.wong@nmqdigital.com'
passwordNMQticket = 'Nichol@s123'

usernameCMS = 'nwong'
passwordCMS = 'rqJ4F9mK'

usernamePIM = 'NICHOLAS.WONG'
passwordPIM = 'Nicholas@123'

################################################################################################

browser = webdriver.Chrome(r'C:\Users\Nicholas\chromedriver.exe')


##Google Drive
window_googledrive = browser.window_handles[0]
browser.get('https://docs.google.com/spreadsheets/d/1CoNMPOluAjyn2OmqvYP0IemFXGESeoZ8Tf62YcRG4T0/edit#gid=1553068545')

##Salesforce
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
browser.get('https://sony-int.my.salesforce.com/home/home.jsp?sdtd=1')
browser.find_element_by_id('username').send_keys(usernameSF)
browser.find_element_by_id('password').send_keys(passwordSF)
sfButton = browser.find_element_by_id('Login')
sfButton.click()

##NMQ ticketing
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window("tab3")
browser.get('https://sony.nmq.digital/tickets')
browser.find_element_by_id('user_email').send_keys(usernameNMQticket)
browser.find_element_by_id('user_password').send_keys(passwordNMQticket)
nmqTicketButton = browser.find_element_by_name('commit')
nmqTicketButton.click()

##CMS
browser.execute_script("window.open('about:blank', 'tab4');")
browser.switch_to.window("tab4")
browser.get('https://prod-cms-gwt.sony.eu/iw-cc/command/iw.ui')
browser.find_element_by_id('iw_user').send_keys(usernameCMS)
browser.find_element_by_id('iw_password').send_keys(passwordCMS)
cmsButton = browser.find_element_by_tag_name('a')
cmsButton.click()

##PIM
os.startfile(path)


