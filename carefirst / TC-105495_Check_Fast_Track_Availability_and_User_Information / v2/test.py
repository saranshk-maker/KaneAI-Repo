
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

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://start.centralhealthadvisors.com/
    driver.get("https://start.centralhealthadvisors.com/")
    driver.implicitly_wait(6)

    # Step - 2 : Type zip code 75070
    element_locators = ["//input[@placeholder='Enter your Zip Code Here' and @type='text']", '[placeholder="Enter your Zip Code Here"]', '[placeholder="Enter your Zip Code Here"][type="text"]', "//input[contains(@placeholder,'Enter your Zip Code Here')]", '.hl_form-builder--main--custom-margin > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)', "//section[contains(@class,'hl_form-builder--main--custom-margin')]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"]
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in '75070':
            element.send_keys(char)
    else:
        element.send_keys('75070')
    driver.implicitly_wait(6)

    # Step - 3 : Click next
    element_locators = ["//div[@role='button' and @aria-label='NEXT']/span[1]", "//div[@role='button' and @aria-label='NEXT']/span[1]", "//span[text()='NEXT']", '[aria-label="NEXT"] > span', '[role="button"] > span', '[role="button"][aria-label="NEXT"] > span', '[role="button"] > span:nth-child(1)', "//span[contains(text(),'NEXT')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 4 : Click 'MySelf' option
    element_locators = ['.hl_form-builder--main--custom-margin > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//section[contains(@class,'hl_form-builder--main--custom-margin')]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 5 : Click As Soon As Possible dropdown
    element_locators = ["//label[contains(text(),'As Soon As Possible')]", '.hl_form-builder--main--custom-margin > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1)', "//section[contains(@class,'hl_form-builder--main--custom-margin')]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Check if 'Fast Track' option is available → {{fast_track_available}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 7 : If 'Fast Track' option is available then click on it
    _conditions_weUJ = [ResolvedCondition.from_string(condition) for condition in ['{{fast_track_available}} == true']]
    _connectors_weUJ = [ConcatenationOperator(connector) for connector in []]
    _condition_weUJ = Condition(_conditions_weUJ, _connectors_weUJ)
    _result_weUJ, _ = _condition_weUJ.evaluate(user_variables, get_variable_value)

    if _result_weUJ:
        driver.implicitly_wait(6)

        # Step - 8 : Click 'Fast Track' option
        element_locators = ["//span[text()='⚡ Fast Track']", "//span[contains(text(),'⚡ Fast Track')]", '[aria-label="⚡ Fast Track. See popular options right away"] > span:nth-child(2)', '[aria-label="⚡ Fast Track. See popular options right away"] > span:nth-child(2)', '[aria-label="⚡ Fast Track. See popular options right away"] > span:nth-child(2)', "//section[contains(@class,'hl_form-builder--main--custom-margin')]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]"]
        element = get_element(driver,element_locators)

        try:
            actions.move_to_element(element).click().perform()
        except:
            element.click()

    else:
        print("else is unresolved")

    driver.implicitly_wait(6)

    # Step - 9 : Check if Name is present → {{name_present}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 10 : Check if Email is present → {{email_present}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 11 : Assert ({{name_present}} equals true) AND ({{email_present}} equals true)
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 12 : assert on network calls
    network_04ed43fdbe299fbc = response = driver_query_script(driver, type = 'network_log', attributes = [{'method': 'POST', 'url': 'https://t.centralhealthadvisors.com/v1/lst/error?script=UNIFIED_TRACKING_SCRIPT', 'network_log_id': '04ed43fdbe299fbc', 'index': 2, 'is_mobile': False, 'proxy_api_port': ''}], field = 'name', max_polling_time = 10)

    print("network_04ed43fdbe299fbc:", network_04ed43fdbe299fbc)
    driver.implicitly_wait(6)

    # Step - 13 : assert on network calls
    network_04ed43fdbe299fbc = response = driver_query_script(driver, type = 'network_log', attributes = [{'method': 'POST', 'url': 'https://t.centralhealthadvisors.com/v1/lst/error?script=UNIFIED_TRACKING_SCRIPT', 'network_log_id': '04ed43fdbe299fbc', 'index': 2, 'is_mobile': False, 'proxy_api_port': ''}], field = 'name', max_polling_time = 10)

    print("network_04ed43fdbe299fbc:", network_04ed43fdbe299fbc)
    driver.implicitly_wait(6)

    # Step - 14 : executing api
    response = requests.get(url='https://countriesnow.space/api/v0.1/countries', headers={}, params={},timeout=10000)
    print("Content for the api is ",response.status_code)
    driver.implicitly_wait(6)

    # Step - 15 : Execute JavaScript snippet
    JS_Response=driver.execute_script('''return (function(){try{return (function(){
    function getNumber() {
        let number = 1;
        return number;
    }

    return getNumber();
    })()}catch(e){return {error: e.stack}}})()''')
    print("Your response is => ",JS_Response)

    driver.quit()
except Exception as e:
    driver.quit()
