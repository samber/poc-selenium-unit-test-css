from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pathlib import Path
import os


selenium_grid_url = "http://127.0.0.1:4444/wd/hub"
capabilities = DesiredCapabilities.CHROME.copy()

driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)
html = Path(os.getcwd() + '/index.html').read_text()
css = Path(os.getcwd() + '/style.css').read_text()
html = html.replace('</head>', '<style>' + css + '</style></head>')

driver.get("data:text/html;charset=utf-8," + html);

p = driver.find_element_by_css_selector('body p')
print('white', p.value_of_css_property('color'))
print('red', p.value_of_css_property('background-color'))
print('900', p.value_of_css_property('font-weight'))
print('42px', p.value_of_css_property('font-size'))

driver.quit()
