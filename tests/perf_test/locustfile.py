from locust import HttpUser, task, between
import random
import json


"""
                                                    ### MY ANSWERS TO STEP 2 OF THE ASSIGNMENT ###

at 50 simultaneous users the 95th percentile is at 3ms
at 50 simultaneous users the throughput is aprox 16-17rps
                                add : ~7rps
                                div : ~3-4rps
                                mul : ~3-4rps
                                sub : ~3-4rps
at 800 users we start seeing an increase in ms at the 95th percentile, and between 1100-1200 users the program fails to return a accurate result and the program crashes.
at around 1000 users where the application is still running stable we see an throughput at approx ~320-340rps


1. Thhe response time of the add operation is most likely tied to the amount of uses the function goes through, since it recieves double the amount of requests and throughput
compared to other functions its only natural that it will have some delays at certain points. But the issue could also be network-side or server-side, if the network and server
isn't strong enough to handle the traffic, there will be delays and issues along the way. 

2. the application crashes around 1100-1200 concurrent users, the issue is that with this amount of users actively useing the functions, the network/server-side can't handle the requests
properly, causing incorrect json results from the api, the issue resulting in "if not response_data['result'] == data_to_use[2]:" being empty because it can't handle the data fast enough.
"""

class CalculatorUser(HttpUser):
    wait_time = between(2, 4)

    @task(2)
    def add(self):
        data = [[1,1,2], [2,2,4], [8,4,12], [1,3,4]]
        data_to_use = random.choice(data)
        add = {
            "operation": "add",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = response.json()
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")

    @task(1)
    def subtract(self):
        data = [[3,1,2], [2,2,0]]
        data_to_use = random.choice(data)
        sub = {
            "operation": "subtract",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=sub) as response:
            response_data = response.json()
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")

    @task(1)
    def multiply(self):
        data = [[3,7,21], [2,4,8]]
        data_to_use = random.choice(data)
        mul = {
            "operation": "multiply",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=mul) as response:
            response_data = response.json()
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")

    @task(1)
    def divide(self):
        data = [[12,6,2], [30,2,15]]
        data_to_use = random.choice(data)
        div = {
            "operation": "divide",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=div) as response:
            response_data = response.json()
            if not response_data['result'] == data_to_use[2]:
                response.failure(f"Expected result to be {data_to_use[2]} but was {response_data['result']}")

if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
