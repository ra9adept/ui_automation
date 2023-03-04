from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class BasePage:
    def __init__(self, driver, url='https://demoqa.com/'):
        self.driver = driver
        self.url = url
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def open_page(self):
        self.driver.get(self.url)

    def __get_selenium_by(self, find_by: str) -> str:
        find_by = find_by.lower()
        locators = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'id': By.ID,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'partial_link': By.PARTIAL_LINK_TEXT,
            'link': By.LINK_TEXT,
            'class': By.CLASS_NAME
        }
        return locators[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name=None) -> list[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name=None) -> list[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def get_text_from_webelements(self, elements: list[WebElement]) -> list[str]:
        return [element.text.lower() for element in elements]

    def go_to_element(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_by_text(self, elements: list[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def delete_cookie(self, cookie_name: str) -> None:
        self.driver.delete_cookie(cookie_name)

    def action_doubleclick(self, element: WebElement) -> None:
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element: WebElement) -> None:
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_tab_by_handle(self, handle: int) -> None:
        self.driver.switch_to.window(self.driver.window_handles[handle])

    def check_state_after_time(self, find_by: str, locator: str, condition: str, timeout: int = 10) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        if condition == 'visible':
            try:
                wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))
                return True
            except TimeoutException as error:
                print(f'{error}\n Approximate elapsed time until element is visible is greater then {timeout} seconds')
                return False
        elif condition == 'present':
            try:
                wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))
                return True
            except TimeoutException as error:
                print(f'{error}\n Approximate elapsed time until element is present is greater then {timeout} seconds')
                return False
        elif condition == 'clickable':
            try:
                wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))
                return True
            except TimeoutException as error:
                print(
                    f'{error}\n Approximate elapsed time until element is clickable is greater then {timeout} seconds')
                return False
        else:
            return False
