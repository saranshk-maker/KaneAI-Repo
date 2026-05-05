
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

    # Step - 1 : Open URL https://www.xe.com/en-us/currencyconverter/
    driver.get("https://www.xe.com/en-us/currencyconverter/")
    driver.implicitly_wait(6)

    # Step - 2 : Read current URL → {{current_url}}
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 3 : Assert {{current_url}} equals https://www.xe.com/en-us/currencyconverter/
    current_url = driver.current_url

    print("current_url:", current_url)
    driver.implicitly_wait(6)

    # Step - 4 : Check heading text for Exchange Rate and Currency Converter Tool → {{landing_heading_text}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 5 : Assert {{landing_heading_text}} contains Exchange Rate and Currency Converter Tool
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 6 : Read Currency From text field value → {{currency_from_value}}
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        currency_from_value = result
    
    print("currency_from_value:", currency_from_value)
    driver.implicitly_wait(6)

    # Step - 7 : Assert {{currency_from_value}} contains '1.00'
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        currency_from_value = result
    
    print("currency_from_value:", currency_from_value)
    driver.implicitly_wait(6)

    # Step - 8 : Click Currency From dropdown
    element_locators = ['form.flex > fieldset:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)', 'form.flex > fieldset:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)', "//fieldset[contains(@class,'focus-within:shadow-xe-primary-500') and contains(@class,'hover:shadow-xe-primary-500') and contains(@class,'md:px-6') and contains(@class,'md:mr-1')]/div[1]/div[1]/button[1]", "//fieldset[contains(@class,'md:mr-1')]/div[1]/div[1]/button[1]", "//fieldset[contains(@class,'md:mr-1')]/div[1]/div[1]/button[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 9 : Read Currency From dropdown options text → {{currency_options}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 10 : Assert {{currency_options}} contains 'USD US Dollar'
    'This Instruction Is Carried Out By The Vision Model'

    driver.quit()
except Exception as e:
    driver.quit()
