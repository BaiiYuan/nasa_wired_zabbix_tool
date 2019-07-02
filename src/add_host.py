from selenium import webdriver
from selenium.webdriver.support.ui import Select
import getpass
from selenium.webdriver.common.keys import Keys
from IPython import embed
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
WINDOW_SIZE = "1920,1080"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
browser = webdriver.Chrome(options = chrome_options)
browser.get("https://10.1.7.111/zabbix/hosts.php?ddreset=1")
def stable_click(s, repeats = 5):
	button = browser.find_element_by_name(s)
	for _ in range(repeats):
		try:
			button.click()
		except:
			break
def send_str(s1, s2, clear = False):
	inp = browser.find_element_by_name(s1)
	if clear:
		inp.clear()
	inp.send_keys(s2)
stable_click('login')
send_str('name', 'ta221')
send_str('password', getpass.getpass())
stable_click('enter')
stable_click('form')
ip = input('Please enter host name(ip address): ')
send_str('host', ip)
send_str('visiblename', input('Please enter host visible name: '))
sel = Select(browser.find_element_by_id('groups_right'))
sel.select_by_value('1')
stable_click('add')
sel.select_by_value('9')
stable_click('add')
stable_click('addSNMPInterface', 1)
lst = browser.find_elements_by_class_name('interface-ip')
tmp = lst[1].find_element_by_css_selector('*').get_attribute('name')
num = tmp.split('[')[1].split(']')[0]
send_str('interfaces[{}][ip]'.format(num), ip, clear = True)
buttons = browser.find_elements_by_class_name('ui-corner-top')
buttons[1].click()
inp = browser.find_element_by_class_name("input")
inp.send_keys("Template Net Cisco IOS SNMPv2")
available = browser.find_element_by_class_name('available')
time.sleep(1)
button = available.find_element_by_class_name('multiselect-suggest')
button.click()     
button = browser.find_elements_by_class_name('btn-link')
button[6].click()
buttons = browser.find_elements_by_class_name('ui-corner-top')
buttons[3].click()
send_str('macros[0][macro]', '{$SNMP_COMMUNITY}')
send_str('macros[0][value]', 'csiesnmp')
button = browser.find_elements_by_name('add')[-1]
button.click()
browser.close()