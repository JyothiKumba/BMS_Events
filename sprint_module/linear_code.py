import time
from selenium import webdriver
path = r'C:\Users\LENOVO\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://in.bookmyshow.com/")
driver.implicitly_wait(20)
driver.maximize_window()

driver.find_element("xpath",'//img[@alt="HYD"]').click()
driver.find_element("xpath",'//a[text()="Events"]').click()
driver.find_element("xpath",'(//div[text()="Browse by Venues"])[1]').click()
driver.find_element("xpath",'(//button[text()="VIEW DETAILS"])[2]').click()
driver.find_element("xpath",'//img[@alt="Vivek Samtani Live: A Stand-up Comedy Show"]').click()
driver.find_element("xpath",'//button[text()="Book"]').click()
driver.find_element("xpath",'//div[text()="Aaromale - Cafe & Creative Community: Hyderabad"]').click()
driver.find_element("xpath",'(//div[text()="Add"])[1]').click()
driver.find_element("xpath",'//button[text()="Proceed"]').click()
driver.find_element("xpath",'//input[@name="name"]').send_keys("Jyi Priya")
driver.find_element("xpath",'//input[@name="primary_phoneNo"]').send_keys("7995291931")
driver.find_element("xpath",'//input[@name="primary_email"]').send_keys("kumb222@gmail.com")
driver.find_element("xpath",'(//input[@type="checkbox"])[1]').click()
driver.find_element("xpath",'(//input[@type="checkbox"])[2]').click()
driver.find_element("id",'registration-submit-button').click()
driver.find_element("xpath",'//button[text()="Login to Proceed"]').click()






























# import time
#
# from selenium import webdriver
# path = r'C:\Users\LENOVO\Downloads\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(path)
# driver.get("https://in.bookmyshow.com/")
# driver.implicitly_wait(20)
# driver.maximize_window()
# # driver.find_element("xpath",'//input[@type="text"]').send_keys("Hyderabad")
# # driver.find_element("xpath",'//strong[text()="Hyderabad"]').click()
# driver.find_element("xpath",'//img[@alt="HYD"]').click()
# driver.find_element("xpath",'//a[text()="Events"]').click()
# driver.find_element("xpath",'(//div[text()="Browse by Venues"])[1]').click()
# driver.find_element("xpath",'(//button[text()="VIEW DETAILS"])[1]').click()
# driver.find_element("xpath",'//img[@alt="Johnny Ka Sandesh"]').click()
# driver.find_element("xpath",'//button[text()="Book"]').click()
# driver.find_element("xpath",'(//div[text()="Add"])[1]').click()
# driver.find_element("xpath",'//button[text()="Proceed"]').click()
# driver.find_element("xpath",'//button[text()="Login to Proceed"]').click()