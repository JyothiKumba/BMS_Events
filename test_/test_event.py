import pytest
from Data.reading_objects import Readexcel
from POM.event_module import BmsPage


class TestBmsPage:
    read_xl = Readexcel()
    data = read_xl.read_test_data()

    @pytest.mark.parametrize("name, phoneno, Email",data)
    def test_Event(self, init_driver, name, phoneno, Email):
        driver = init_driver

        tp = BmsPage(driver)
        tp.click_hyderbad()
        tp.click_on_events()
        tp.click_on_browser_by_venue()
        tp.click_on_Aaromale_ccc()
        tp.click_on_Stand_up()
        tp.click_Book()
        tp.click_on_Area()
        tp.click_on_Add()
        tp.click_on_proceed()
        tp.enter_Name(name)
        tp.enter_phone_no(phoneno)
        tp.enter_Email(Email)
        tp.click_on_checkbox1()
        tp.click_on_checkbox2()
        tp.click_on_submit()
        tp.click_on_login_to_proceed()



























        # except AssertionError as msg:
        #     td = datetime.datetime.now()
        #     name = f'screenshot_{td.hour}{td.minute}{td.second}.png'
        #     driver.save_screenshot(Configuration.screenshot + name)
        #     raise msg

        # except BaseException:
        #     td = datetime.datetime.now()
        #     name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        #     path = r"C:\Users\Shankar Kadam\PycharmProjects\capg_project\screenshots"
        #     driver.save_screenshot(path + name)
















