from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class RegisterPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver=driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password1': Element('//input[@id="password1"]', self),
            'password2': Element('//input[@id="password2"]', self),
            'register': Element('//button[@id="register"]', self),
            'error_message': Element('//div[@id="errormsg"]', self)
        }

        self.elements = munchify(self.page_elements)

    def register(self, username, password1, password2):
        self.elements.username.set(username)
        self.elements.password1.set(password1)
        self.elements.password2.set(password2)
        self.elements.register.click()
    
    def get_error_msg(self):
        return self.elements.error_message.text
