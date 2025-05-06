from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.story("登入測試")
def test_login():
    driver = openBrowser()
    login(driver)
    closeBrowser(driver)


@allure.story("個人資訊可以修改")
def test_EditProfile():
    driver = openBrowser()
    login(driver)
    clickProfile(driver)
    editProfile(driver)
    closeBrowser(driver)


@allure.story("個人資訊手機號碼無法輸入過長")
def test_NumberCantLong():
    driver = openBrowser()
    login(driver)
    clickProfile(driver)
    editProfile(driver)
    numberCantLong(driver)
    closeBrowser(driver)


@allure.story("個人資訊手機號碼無法輸入非數字字元")
def test_NotNumber():
    driver = openBrowser()
    login(driver)
    clickProfile(driver)
    editProfile(driver)
    notNumber(driver)
    closeBrowser(driver)


@allure.story("密碼修改必須超過5個字元")
def test_NewPassword():
    driver = openBrowser()
    login(driver)
    clickProfile(driver)
    newPassword(driver)
    closeBrowser(driver)


@allure.step("openBrowser")
def openBrowser():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://rhinoshield.tw/")
    return driver


@allure.step("closeBrowser")
def closeBrowser(driver):
    driver.quit()


@allure.step("login")
def login(driver):
    loginElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]/div/div')
        ))
    loginElement.click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer_email"]').send_keys('{email}')
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer_password"]').send_keys('{password}')
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer_login"]/div').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="slider"]/li[1]/a/div[1]'))
    )


@allure.step("點選個人頁面")
def clickProfile(driver):
    profileElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="navigation-bar"]/div[2]/div/div[2]/div/div[2]/div/div'))
    )
    profileElement.click()


@ allure.step("編輯個人頁面")
def editProfile(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="customer-info"]/h2'))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="customer-info"]/button'))
    ).click()


@ allure.step("電話號碼不可過長")
def numberCantLong(driver):
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/div[1]/input').click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/div[1]/input').clear()
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/div[1]/input').send_keys('091234567890')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/p'))
    )
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/p')


@ allure.step("電話不能非數字")
def notNumber(driver):
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/div[1]/input').click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/div[1]/input').clear()
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/div[1]/input').send_keys('abcdefghij')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/p'))
    )
    driver.find_element(
        by=By.XPATH, value='//*[@id="customer-info"]/div[8]/div/div/div[1]/div[2]/div[3]/div/p')


@ allure.step("新密碼不得少於五字")
def newPassword(driver):
    driver.find_element(
        by=By.XPATH, value='//*[@id="reset-password"]/button').click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').click()
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').clear
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').send_keys('1')

    WebDriverWait(driver, 1, 0.5).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="reset-password"]/div[2]/div/div[2]/div[1]/p')))
    sleep(0.3)

    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').clear()
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').send_keys('12')

    WebDriverWait(driver, 1, 0.5).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="reset-password"]/div[2]/div/div[2]/div[1]/p')))
    sleep(0.3)

    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').clear()
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').send_keys('123')

    WebDriverWait(driver, 1, 0.5).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="reset-password"]/div[2]/div/div[2]/div[1]/p')))
    sleep(0.3)

    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').clear()
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').send_keys('1234')

    WebDriverWait(driver, 1, 0.5).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="reset-password"]/div[2]/div/div[2]/div[1]/p')))
    sleep(0.3)

    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').clear()
    driver.find_element(
        by=By.XPATH, value='//*[@id="new-password"]').send_keys('0123')

    WebDriverWait(driver, 1, 0.5).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="reset-password"]/div[2]/div/div[2]/div[1]/p')))
    sleep(0.3)

    driver.find_element(
        by=By.XPATH, value='//*[@id="reset-password"]/div[2]/div/div[2]/div[1]/p')
