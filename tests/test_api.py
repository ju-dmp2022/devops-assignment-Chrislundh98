import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class BaseTest:
    def setup_method(self):
        self.url = "http://127.0.0.1:5000/calculate"
    
    def teardown_method(self):
        self.url = None

class TestAPI(BaseTest):
    def test_calc_add(self):
        payload = {
            "operation1": 'add',
            "operand1": 1,
            "operand2": 2
        }
        response = requests.post(self.url, json=payload)

    def test_calc_sub(self):
        payload = {
            "operation1": 'sub',
            "operand1": 1,
            "operand2": 2
        }
        response = requests.post(self.url, json=payload)

    def test_calc_mul(self):
        payload = {
            "operation1": 'mul',
            "operand1": 3,
            "operand2": 6
        }
        response = requests.post(self.url, json=payload)

    def test_calc_div(self):
        payload = {
            "operation1": 'div',
            "operand1": 6,
            "operand2": 2
        }
        response = requests.post(self.url, json=payload)

    def test_gen_calc_client(self):
        client = Client(base_url="http://127.0.0.1:5000")
        response = calculate.sync(client=client, body=Calculation(operation=Opertions.ADD, operand1=1, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 3
