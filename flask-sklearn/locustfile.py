import time
from locust import HttpUser, task, TaskSet, between

class MTaskSet(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_home(self):
        self.client.get("/")

    @task(3)
    def get_predictions(self):
        self.client.post("/predict", json={"CHAS":{"0":0}, "RM":{"0":6.575}, "TAX":{"0":296.0}, "PTRATIO":{"0":15.3}, "B":{"0":396.9}, "LSTAT":{"0":4.98}})
