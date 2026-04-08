
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://uat.farekey.com/
    driver.get("https://uat.farekey.com/")
    driver.implicitly_wait(6)

    # Step - 2 : Click on the 'From' city selection label in the flight search form
    element_locators = ["//span[text()='From']", '.hm_destination > div:nth-child(1) > label:nth-child(1) > span:nth-child(1)', '.hm_destination > div:nth-child(1) > label:nth-child(1) > span:nth-child(1)', "//span[contains(text(),'From')]", "//div[contains(@class,'hm_destination')]/div[1]/label[1]/span[1]", "//div[contains(@class,'hm_destination')]/div[1]/label[1]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 3 : Click on Kuwait location option in the dropdown list
    element_locators = ["//span[text()='Kuwait']", '.show > a:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)', '.show > a:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)', "//div[contains(@class,'show')]/a[1]/div[1]/div[1]/span[1]", "//div[contains(@class,'show')]/a[1]/div[1]/div[1]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 4 : Click on Dubai city option in destination dropdown
    element_locators = ["//span[text()='Dubai']", "//span[contains(text(),'Dubai')]", '.show > a:nth-child(2) > div:nth-child(1) > div:nth-child(6) > span:nth-child(1)', '.show > a:nth-child(2) > div:nth-child(1) > div:nth-child(6) > span:nth-child(1)', "//div[contains(@class,'show')]/a[1]/div[1]/div[5]/span[1]", "//div[contains(@class,'show')]/a[1]/div[1]/div[5]/span[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Click on May 13th date in calendar popup
    element_locators = ["//div[@role='listbox' and @aria-label='Month May, 2026']/div[3]/div[4]", "//div[@role='listbox' and @aria-label='Month May, 2026']/div[3]/div[4]", '[aria-label="Choose Wednesday, May 13th, 2026"]', "//div[@role='option' and @aria-label='Choose Wednesday, May 13th, 2026']", '[role="option"][aria-label="Choose Wednesday, May 13th, 2026"]', '[aria-label="Choose Tuesday, May 12th, 2026"] + div', '[role="option"][aria-label="Choose Tuesday, May 12th, 2026"] + div', "//div[contains(@aria-label,'Choose Wednesday, May 13th, 2026')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Click on the Apply button in the date picker popup
    element_locators = ["//div[@role='dialog' and @aria-label='Choose Date']/div[3]/div[1]/button[2]", "//div[@role='dialog' and @aria-label='Choose Date']/div[3]/div[1]/button[2]", '[role="dialog"] > div:nth-child(5) > div:nth-child(1) > button:nth-child(2)', '[role="dialog"] > div:nth-child(5) > div:nth-child(1) > button:nth-child(2)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 7 : Click on the orange Search button in the flight search form
    element_locators = ['.searchBtn', '.button_theme.searchBtn', '.field_row > div:nth-child(4) > button:nth-child(1)', '.field_row > div:nth-child(4) > button:nth-child(1)', "//button[text()='Search']", "//button[contains(text(),'Search')]", "//button[contains(@class,'searchBtn')]", "//button[contains(@class,'button_theme') and contains(@class,'searchBtn')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 8 : Click on the price label showing KWD 58
    element_locators = ['.result_col > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > h2:nth-child(1)', "//div[contains(@class,'result_col')]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/h2[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 9 : Click on the red Book button in fare options section
    element_locators = ['.theme_btnStyle', '.brndedBookBtn', '.theme_btnStyle.brndedBookBtn', '.bramdR + button', "//button[text()='Book']", "//button[contains(@class,'theme_btnStyle')]", "//button[contains(@class,'brndedBookBtn')]", "//button[contains(@class,'theme_btnStyle') and contains(@class,'brndedBookBtn')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 10 : Click on 'Select' button in fare options section
    element_locators = ['.list_btn', "//button[text()='Select']", "//button[contains(text(),'Select')]", '.detils_lft > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > button:nth-child(1)', '.detils_lft > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > button:nth-child(1)', "//button[contains(@class,'list_btn')]", "//div[contains(@class,'detils_lft')]/div[5]/div[3]/div[2]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 11 : Scroll 30% down in viewport
    element_locators = ['//body/script[1]/ancestor::body[1]', '//body/script[2]/ancestor::body[1]', '//body/script[4]/ancestor::body[1]', '//body/script[20]/ancestor::body[1]', 'html:nth-child(1) > body:nth-child(2)', 'html:nth-child(1) > body:nth-child(2)']
    element = get_element(driver,element_locators)

    element_locators = ['//body/script[1]/ancestor::body[1]', '//body/script[2]/ancestor::body[1]', '//body/script[4]/ancestor::body[1]', '//body/script[20]/ancestor::body[1]', 'html:nth-child(1) > body:nth-child(2)', 'html:nth-child(1) > body:nth-child(2)']
    element = get_element(driver,element_locators)
    driver.implicitly_wait(6)

    # Step - 12 : Scroll 30% down in viewport
    element_locators = ['//body/script[1]/ancestor::body[1]', '//body/script[2]/ancestor::body[1]', '//body/script[4]/ancestor::body[1]', '//body/script[20]/ancestor::body[1]', 'html:nth-child(1) > body:nth-child(2)', 'html:nth-child(1) > body:nth-child(2)']
    element = get_element(driver,element_locators)

    element_locators = ['//body/script[1]/ancestor::body[1]', '//body/script[2]/ancestor::body[1]', '//body/script[4]/ancestor::body[1]', '//body/script[20]/ancestor::body[1]', 'html:nth-child(1) > body:nth-child(2)', 'html:nth-child(1) > body:nth-child(2)']
    element = get_element(driver,element_locators)
    driver.implicitly_wait(6)

    # Step - 13 : Click Ok button
    element_locators = ['[type="button"]', '.btn', '.pop_contain > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)', '.pop_contain > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)', "//input[starts-with(@type,'butto')]", "//input[contains(@class,'btn')]", "//input[contains(@type,'button')]", "//div[contains(@class,'pop_contain')]/div[1]/div[2]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 14 : Scroll 50 px down in viewport
    element_locators = ['//body/script[1]/ancestor::body[1]', '//body/script[2]/ancestor::body[1]', '//body/script[4]/ancestor::body[1]', '//body/script[20]/ancestor::body[1]', 'html:nth-child(1) > body:nth-child(2)', 'html:nth-child(1) > body:nth-child(2)']
    element = get_element(driver,element_locators)

    element_locators = ['//body/script[1]/ancestor::body[1]', '//body/script[2]/ancestor::body[1]', '//body/script[4]/ancestor::body[1]', '//body/script[20]/ancestor::body[1]', 'html:nth-child(1) > body:nth-child(2)', 'html:nth-child(1) > body:nth-child(2)']
    element = get_element(driver,element_locators)

    driver.quit()
except Exception as e:
    driver.quit()
