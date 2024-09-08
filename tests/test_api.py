import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models.opertions import Opertions
from calculator_client.models import ResultResponse

class TestAPI():
    def test_calc_add(self):
        url = "http://127.0.0.1:5000/calculate"
        payload = {
            "operation1" : 'add' ,
            "operand1" : 1 ,
            "operand2" : 1 

        }
        response = requests.post(url, json=payload)
    
    def test_gen_calc_client(self):
        client = Client('http://localhost:5000')
        response = calculate.sync(client = client, body = Calculation(Opertions.ADD, operand1=1, operand2=2))
        assert isinstance(response, ResultResponse)
        assert response.result == 3