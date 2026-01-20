from selenium.webdriver.common.by import By

class TransactionFormPage:
    TRANSACTION_TYPE_DROPDOWN = (By.ID, "transactionType")
    AMOUNT_INPUT = (By.ID, "amount")
    DESCRIPTION_INPUT = (By.ID, "description")
    DATE_INPUT = (By.ID, "transactionDate")
    SUBMIT_BUTTON = (By.ID, "submitBtn")
    CANCEL_BUTTON = (By.ID, "cancelBtn")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'success-message')]")
    ERROR_TYPE = (By.ID, "transactionTypeError")
    ERROR_AMOUNT = (By.ID, "amountError")
    ERROR_DESCRIPTION = (By.ID, "descriptionError")

    def __init__(self, driver):
        self.driver = driver

    def select_transaction_type(self, type_text):
        dropdown = self.driver.find_element(*self.TRANSACTION_TYPE_DROPDOWN)
        dropdown.click()
        option = self.driver.find_element(By.XPATH, f"//option[text()='{type_text}']")
        option.click()

    def enter_amount(self, amount):
        input_field = self.driver.find_element(*self.AMOUNT_INPUT)
        input_field.clear()
        input_field.send_keys(str(amount))

    def enter_description(self, description):
        input_field = self.driver.find_element(*self.DESCRIPTION_INPUT)
        input_field.clear()
        input_field.send_keys(description)

    def enter_date(self, date_str):
        input_field = self.driver.find_element(*self.DATE_INPUT)
        input_field.clear()
        input_field.send_keys(date_str)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def cancel(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def get_inline_error(self, field):
        if field == "type":
            return self.driver.find_element(*self.ERROR_TYPE).text
        elif field == "amount":
            return self.driver.find_element(*self.ERROR_AMOUNT).text
        elif field == "description":
            return self.driver.find_element(*self.ERROR_DESCRIPTION).text
        return ""
