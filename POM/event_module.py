import time

from Data.reading_objects import Readexcel

from Library.config import Configuration


class BmsPage:
    read_xl = Readexcel()
    event_locators = read_xl.read_locators(Configuration.event_locators_sheet)

    def __init__(self, driver):
        self.driver = driver


    def click_hyderbad(self):
        locator = self.event_locators["hyd_img"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def click_on_events(self):
        locator = self.event_locators["click_on_Events"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def click_on_browser_by_venue(self):
        locator = self.event_locators["click_on_browser"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def click_on_Aaromale_ccc(self):
        locator = self.event_locators["click_on_VD"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def click_on_Stand_up(self):
        locator = self.event_locators["Stand_up"]
        self.driver.find_element(*locator).click()

    def click_Book(self):
        locator = self.event_locators["Book"]
        self.driver.find_element(*locator).click()

    def click_on_Area(self):
        locator = self.event_locators["click_on_Area"]
        self.driver.find_element(*locator).click()

    def click_on_Add(self):
        locator = self.event_locators["Add_no_persons"]
        self.driver.find_element(*locator).click()

    def click_on_proceed(self):
        locator = self.event_locators["proceed"]
        self.driver.find_element(*locator).click()

    def enter_Name(self, name):
        locator = self.event_locators["Name"]
        self.driver.find_element(*locator).send_keys(name)


    def enter_phone_no(self, phoneno):
        global phone
        if isinstance(phoneno, float):
            phone = str(int(phoneno))
        assert len(phone) == 10
        locator = self.event_locators["phone_no"]
        self.driver.find_element(*locator).send_keys(phone)

    def enter_Email(self, Email):
        locator = self.event_locators["Email"]
        self.driver.find_element(*locator).send_keys(Email)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def click_on_checkbox1(self):
        locator = self.event_locators["checkbox1"]
        self.driver.find_element(*locator).click()

    def click_on_checkbox2(self):
        locator = self.event_locators["checkbox2"]
        self.driver.find_element(*locator).click()

    def click_on_submit(self):
        locator = self.event_locators["submit"]
        self.driver.find_element(*locator).click()

    def click_on_login_to_proceed(self):
        locator = self.event_locators["login_to_proceed"]
        self.driver.find_element(*locator).click()


















