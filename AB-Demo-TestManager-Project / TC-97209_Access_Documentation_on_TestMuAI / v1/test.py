
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
    driver.implicitly_wait(6)

    # Step - 1 : Open https://www.testmuai.com/
    driver.get("https://www.testmuai.com/")
    driver.implicitly_wait(6)

    # Step - 2 : Check pop-up presence → {{popup_present}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 3 : Hover on resources
    element_locators = ["//button[contains(text(),'Resources')]", '.chfw-header_items > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)', "//div[contains(@class,'chfw-header_items')]/div[2]/div[1]/div[1]/div[3]/button[1]"]
    element = get_element(driver,element_locators)

    actions.move_to_element(element).perform()
    driver.implicitly_wait(6)

    # Step - 4 : Click on the 'Resources' dropdown button in the top nav bar
    element_locators = ["//button[contains(text(),'Resources')]", '.chfw-header_items > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)', "//div[contains(@class,'chfw-header_items')]/div[2]/div[1]/div[1]/div[3]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Click on Documentation menu item in Developer section
    element_locators = ["//p[text()='Documentation']", "//p[contains(text(),'Documentation')]", '.chfw-dropdown_menu > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > div:nth-child(1) > p:nth-child(1)', "//div[contains(@class,'chfw-dropdown_menu')]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[1]/p[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Open https://testmuai.com
    driver.get("https://testmuai.com")
    driver.implicitly_wait(6)

    # Step - 7 : Click login button
    element_locators = ["//a[text()='Login']", "//a[contains(text(),'Login')]", '.chfw-header_items > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)', '.chfw-header_items > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)', "//div[contains(@class,'chfw-header_items')]/div[2]/div[1]/div[2]/a[1]", "//div[contains(@class,'chfw-header_items')]/div[2]/div[1]/div[2]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 8 : Check if 'login with google' button is visible → {{login_with_google_visible}}
    'This Instruction Is Carried Out By The Vision Model'

    driver.quit()
except Exception as e:
    driver.quit()
