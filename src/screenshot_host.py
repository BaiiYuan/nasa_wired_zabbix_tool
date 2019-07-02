from selenium import webdriver
from selenium.webdriver.support.ui import Select
import getpass
from IPython import embed

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

browser=webdriver.Chrome()
browser.get("https://10.1.7.111/zabbix/charts.php?ddreset=1")

stable_click('login')
send_str('name', 'ta221')
send_str('password', getpass.getpass())
stable_click('enter')


sel = Select(browser.find_element_by_id('hostid'))
content = [option.text for option in sel.options][1:]
value = [option.get_attribute('value') for option in sel.options][1:]
mapping_dict = {a:b for a, b in zip(content, value)}
print('[-] Select one host')
print('\n'.join('> ' + '\t'.join(s for s in content[i * 3 : i * 3 + 3]) for i in range(len(content) // 3 + 1)), end="\n\n")
target = input('Please enter the hostname: ')
sel.select_by_value(mapping_dict[target])


sel = Select(browser.find_element_by_id('graphid'))
content = [option.text for option in sel.options][1:]
value = [option.get_attribute('value') for option in sel.options][1:]
mapping_dict = {a:b for a, b in zip(content, value)}
print('[-] Select one graph')
print('\n'.join('> ' + s for s in content))
target = input('Please enter the graph type: ')
sel.select_by_value(mapping_dict[target])

screenshot_name = input('Please enter the screenshot name: ')
browser.save_screenshot(screenshot_name)
browser.close()