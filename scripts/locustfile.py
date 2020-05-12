from locust import HttpLocust, TaskSet, between, task

headers = {'Content-Type': 'application/json'}

class UserBehavior(TaskSet):

    @task(weight = 1)
    def root(self, **kwargs):
        return self.client.get("/", name="/", **kwargs)

    @task(weight = 1)
    def produce_json(self, **kwargs):
        return self.client.get("/produce_json", name="/produce_json", **kwargs)

    @task(weight = 1)
    def produce_avro(self, **kwargs):
        return self.client.get("/produce_avro", name="/produce_avro", **kwargs)

    # @task(weight = 1)
    # def produce(self, **kwargs):
    #     return self.client.get("/produce_protobuf", name="/produce_protobuf", **kwargs)


class User(HttpLocust):
    task_set = UserBehavior
    wait_time = between(3,5)
