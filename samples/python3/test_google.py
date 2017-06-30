import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ExampleTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_google_title_matches_correct_value(self):
        for i in range(1,155):
            self.driver = webdriver.Chrome()
            self.driver.get("https://willstdukannstdu.at/gif/gurke-omnomnom")

            button =  self.driver.find_element_by_class_name("js-gifVoteButton")
            # self.driver.manage().deleteAllCookies()
            button.click()
            self.driver.close()

    def tearDown(self):
        pass