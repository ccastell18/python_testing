from selenium import webdriver

chrome_browser  = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert "Selenium Easy Demo" in chrome_browser.title
text_button = chrome_browser.find_element_by_class_name('btn-default')
# print(text_button.get_attribute('innerHTML'))
assert 'Show Message' in chrome_browser.page_source
 
user_message =  chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys("Hello World")

lightbox_close_x = chrome_browser.find_element_by_id("at-cv-lightbox-close")
lightbox_close_x.click()

message_button = chrome_browser.find_element_by_css_selector('#get-input > button')
message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert "Hello World" in output_message.text

chrome_browser.quit()