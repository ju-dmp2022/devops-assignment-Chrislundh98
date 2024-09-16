from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify
import time


class CalcPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//label[@id="user-name"]', self),
            'logout': Element('//button[@id="logout-button"]', self),
            'key1': Element('//button[@id="key-1"]', self),
            'key2': Element('//button[@id="key-2"]', self),
            'key3': Element('//button[@id="key-3"]', self),
            'key4': Element('//button[@id="key-4"]', self),
            'keyadd': Element('//button[@id="key-add"]', self),
            'keysubtract': Element('//button[@id="key-subtract"]', self),
            'keymultiply': Element('//button[@id="key-multiply"]', self),
            'keydivide': Element('//button[@id="key-divide"]', self),
            'keyequals': Element('//button[@id="key-equals"]', self),
            'keyclear': Element('//button[@id="key-clear"]', self),
            'keyzero': Element('//button[@id="key-0"]', self),
            'result': Element('//input[@id="calculator-screen"]', self),
            'history': Element('//button[@id="toggle-button"]', self),
            'textarea': Element('//textarea[@id="history"]', self)

        }

        self.elements = munchify(self.page_elements)

    def logout_exists(self):
        self.elements.logout.find()

    def logout(self):
        if self.logout_exists():
            self.elements.logout.click()

    def add_nums(self):
        self.clear_calc()
        time.sleep(0.1)
        self.elements.key1.click()
        time.sleep(0.1)
        self.elements.keyadd.click()
        time.sleep(0.1)
        self.elements.key2.click()
        time.sleep(0.1)
        self.elements.keyequals.click()
        time.sleep(1)
       
    def subtract_nums(self):
        self.clear_calc()
        time.sleep(0.1)
        self.elements.key3.click()
        time.sleep(0.1)
        self.elements.keysubtract.click()
        time.sleep(0.1)
        self.elements.key1.click()
        time.sleep(0.1)
        self.elements.keyequals.click()
        time.sleep(1)
        

    def multiply_nums(self):
        self.clear_calc()
        time.sleep(0.1)
        self.elements.key3.click()
        time.sleep(0.1)
        self.elements.keymultiply.click()
        time.sleep(0.1)
        self.elements.key2.click()
        time.sleep(0.1)
        self.elements.keyequals.click()
        time.sleep(1)
        
    
    def divide_nums(self):
        self.clear_calc()
        time.sleep(0.1)
        self.elements.key3.click()
        time.sleep(0.1)
        self.elements.keydivide.click()
        time.sleep(0.1)
        self.elements.key2.click()
        time.sleep(0.1)
        self.elements.keyequals.click()
        time.sleep(1)
        
    
    def check_history(self):
        time.sleep(0.5)
        self.elements.history.click()

    def clear_calc(self):
        self.elements.keyclear.click()
        



        
