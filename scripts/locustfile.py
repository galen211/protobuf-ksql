import uuid
import json
from locust import HttpLocust, TaskSet, between, task

headers = {'Content-Type': 'application/json'}

class UserBehavior(TaskSet):

    @task(weight = 1)
    def root(self, **kwargs):
        return self.client.get("/", name="/", **kwargs)

    @task(weight = 1)
    def ping(self, **kwargs):
        return self.client.get("/ping", name="/", **kwargs)

    @task(weight = 1)
    def post_items(self, **kwargs):
        payload = json.dumps({"name": str(uuid.uuid4())})
        return self.client.post("/items", headers=headers, data=payload, **kwargs)

    @task(weight = 1)
    def get_protobuf(self, **kwargs):
        payload = json.dumps({"name": str(uuid.uuid4())})
        return self.client.get("/protobuf", headers=headers, data=payload, **kwargs)


class User(HttpLocust):
    task_set = UserBehavior
    wait_time = between(3,5)
