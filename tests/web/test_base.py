from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tests.web.pages.login_page import LoginPage
from tests.web.pages.calculator_page import CalcPage
from tests.web.pages.register_page import RegisterPage

class WebBase:

    @classmethod
    def setup_class(cls):
        """ Setup to run once
            Initiatiung some common parameters
        """
        cls.app_url = 'http://host.docker.internal:8080'
        cls.username = "test_user7" # init new user for test

    def setup_method(self):
        """ Setup to run before every test
            Initiate a new driver.
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        #self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = chrome_options)
        self.driver = webdriver.Remote(command_executor = "http://localhost:4444", options=chrome_options)
        self.driver.set_window_size(1920,1080)
        self.driver.get(self.app_url)

        """
        Initilize the different pages for tests
        """
        self.calc_page = CalcPage(self.driver) 
        self.register_page = RegisterPage(self.driver) 
        self.login_page = LoginPage(self.driver) 

    def teardown_method(self):
        """ Teardown to run after every test
            Stop the driver
        """
        self.driver.quit()
