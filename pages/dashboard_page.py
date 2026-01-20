from selenium.webdriver.common.by import By

class DashboardPage:
    CREATE_TRANSACTION_BTN = (By.ID, "createTransactionBtn")

    def __init__(self, driver):
        self.driver = driver

    def click_create_transaction(self):
        self.driver.find_element(*self.CREATE_TRANSACTION_BTN).click()
