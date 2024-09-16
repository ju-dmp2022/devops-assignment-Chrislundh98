from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.calculator_page import CalcPage
from tests.web.pages.register_page import RegisterPage
import time

class Test1(WebBase):
    """
    Testing registering a new user
    """

    def test_register_user(self):
        self.login_page.register_button()
        self.register_page.register(self.username, 'Testpass', 'Testpass')
        # error_message = self.register_page.get_error_msg()

        # if 'User already exists!' in error_message:
        #     assert True
        # else:
        time.sleep(5)
        assert self.calc_page.elements.username.text == self.username


class Test2(WebBase):
    """
    Testing calculations
    """
    def test_web_add(self):
        self.calc_page.add_nums()
        assert self.calc_page.elements.result.value == '3'

    def test_web_sub(self):
        self.calc_page.subtract_nums()
        assert self.calc_page.elements.result.value == '2'

    def test_web_mul(self):
        self.calc_page.multiply_nums()
        assert self.calc_page.elements.result.value == '6'

    def test_web_div(self):
        self.calc_page.divide_nums()
        assert self.calc_page.elements.result.value == '1.5'


class Test3(WebBase):
    """
    login test, history test, logout test
    """
    def test_login(self):
        if self.calc_page.elements.username.text == Test1.username:
            self.calc_page.logout()
        else:
            self.login_page.login('admin', 'Testpass')
            time.sleep(2)
            assert self.calc_page.elements.username.text == 'admin'

    def test_history(self):
        self.calc_page.divide_nums()
        self.calc_page.check_history()
        history_text = self.calc_page.elements.textarea.value.strip()  
        assert history_text == '3/2=1.5'

    def test_logout(self):
        if not self.calc_page.logout_exists():
            assert True
        else:
            assert self.calc_page.logout()
