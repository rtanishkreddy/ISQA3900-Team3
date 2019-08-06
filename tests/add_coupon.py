import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class addcoupon_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addcoupon(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://3900team3.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Logged In"
        # Clicks add coupon
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[2]/table/tbody/tr/td[1]/a").click()
        # Fills in information
        elem = driver.find_element_by_id("id_code")
        elem.send_keys("testcoupon")
        elem = driver.find_element_by_id("id_discount")
        elem.send_keys("10")
        elem = driver.find_element_by_xpath("//*[@id=\"coupon_form\"]/div/fieldset/div[2]/div/p/span[1]/a[1]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"coupon_form\"]/div/fieldset/div[2]/div/p/span[2]/a[1]").click()
        elem = driver.find_element_by_id("id_valid_to_0")
        elem.send_keys("2150-08-06")
        elem = driver.find_element_by_xpath("//*[@id=\"coupon_form\"]/div/fieldset/div[3]/div/p/span[2]/a[1]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"id_active\"]").click()
        # Clicks save
        elem = driver.find_element_by_xpath("//*[@id=\"coupon_form\"]/div/div/input[1]").click()
        time.sleep(2)
        #Delete coupon
        elem = driver.find_element_by_id("searchbar")
        elem.send_keys("testcoupon")
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-search\"]/div/input[2]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select").click()
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select/option[2]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr/td[1]/input").click()
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/button").click()
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[4]").click()
        time.sleep(1)
        driver.get("http://3900team3.pythonanywhere.com/admin/coupons/coupon/")
        assert "Coupon Deleted"

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()