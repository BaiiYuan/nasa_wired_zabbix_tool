from selenium import webdriver
from selenium.webdriver.support.ui import Select
import getpass
from IPython import embed
import sys

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

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
WINDOW_SIZE = "1920,1080"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
browser = webdriver.Chrome(options = chrome_options)
browser.get("https://10.1.7.111/zabbix/hosts.php?ddreset=1")

stable_click('login')
send_str('name', 'ta221')
send_str('password', sys.argv[1])
stable_click('enter')

lst = browser.find_elements_by_tag_name('tr')[1:]
content = [i.find_elements_by_tag_name('td')[1].find_element_by_tag_name('a').text for i in lst]
to_click = [i.find_elements_by_tag_name('td')[0].find_element_by_tag_name('input') for i in lst]
mapping_dict = {a:b for a, b in zip(content, to_click)}
print('\n'.join('> ' + '\t'.join(s for s in content[i * 3 : i * 3 + 3]) for i in range(len(content) // 3 + 1)), end="\n\n")
browser.close()
