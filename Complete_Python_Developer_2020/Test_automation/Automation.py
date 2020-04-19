
from selenium import webdriver

chrome_browser = webdriver.Chrome()

#chrome_browser.maximize_window()

chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

try:
    assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in chrome_browser.title
    print("Correct title found!")
except:
    print("Correct title not found!")
    end_test()

try:
    assert "Show Message" in chrome_browser.page_source
    print("Show Message found in page!")
except:
    print("Show Message not found in page!")
    end_test()


message_text_box = chrome_browser.find_element_by_id("user-message")
message_text_box.clear()
test_message = "Hello, this is test message!"
message_text_box.send_keys(test_message)

show_message_button = chrome_browser.find_element_by_xpath("//button[contains(text(),'Show Message')]")
show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")
try:
    assert test_message in output_message.text
    print("Output message asserted to be correct!")
except:
    print("Outpur message assertion failed!")
    end_test()

def end_test():
    chrome_browser.close()
    chrome_browser.quit()